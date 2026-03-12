import json
from typing import Any, Dict, List, Optional
from pathlib import Path
import sys

import pytest
import pytest_asyncio

project_root = Path(__file__).parent.parent
tests_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(tests_root))

from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.memory_workflow_integration import MemoryWorkflowIntegration
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from modules.memory_management.adapter import MemoryManagementAdapter
from modules.memory_management.core.memory_manager import MemoryManager
from modules.text_processing.core.text_processor import TextProcessor
from goal_stack_gate_registry import (
    CANONICAL_20_CASE_GATE,
    L1_BASIC_DIRECT_20_CASE_GATE,
    L1_DIRECT_CONFIDENCE_PROBES,
    L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE,
    SUPPLEMENTAL_20_CASE_GATE,
)


_DUMMY_SCREENSHOT_B64 = "ZmFrZS13ZWJwLXNjcmVlbnNob3Q="


class _StatefulFakeDB:
    def __init__(self):
        self.short = ""
        self.long = ""
        self.updates = 0

    async def get_user_memory(self, hardware_id: str):
        return {"short": self.short, "long": self.long}

    async def update_user_memory(self, hardware_id: str, short_memory: str, long_memory: str):
        self.short = short_memory
        self.long = long_memory
        self.updates += 1
        return True


class _FactAwareTextModule:
    def __init__(self):
        self.is_initialized = True
        self.name = "text_processing"
        self.requests: List[Dict[str, str]] = []

    async def process(self, payload):
        user_text = str(payload.get("text", ""))
        runtime_memory = str(payload.get("runtime_memory_context", ""))
        lowered = user_text.lower()
        self.requests.append(
            {
                "text": user_text,
                "runtime_memory_context": runtime_memory,
            }
        )

        if "что ты помнишь" in lowered:
            response = "Я помню, что тебя зовут Сергей и ты любишь спорт."
        elif "софия" in lowered and "отправь сообщение" in runtime_memory.lower():
            response = "Понял, формирую сообщение для Софии: как у тебя дела?"
        else:
            response = "Принял. Продолжаем."

        async def _gen():
            # Возвращаем строку с пунктуацией, чтобы поток TTS гарантированно разбился на сегмент.
            yield response

        return _gen()


class _AudioChunkModule:
    def __init__(self):
        self.is_initialized = True
        self.name = "audio_generation"

    async def process(self, payload):
        async def _gen():
            yield b"a" * 1024
            yield b"b" * 768

        return _gen()


class _MessagingFollowupProvider:
    def __init__(self):
        self.classifier_calls: List[Dict[str, Any]] = []
        self.process_calls: List[Dict[str, Any]] = []

    async def classify_intent_decision(self, user_input: str = "", classifier_context: Optional[Dict[str, str]] = None, **kwargs):
        input_text = str(user_input or kwargs.get("user_input", "") or "")
        short_term = str((classifier_context or {}).get("short_term_memory", ""))
        self.classifier_calls.append(
            {
                "user_input": input_text,
                "short_term_memory": short_term,
            }
        )

        lowered = input_text.lower()
        if "send a message to sophia" in lowered:
            return {"category": "messages"}
        if (
            "how are you doing today" in lowered
            and "send a message to sophia" in short_term.lower()
            and "what message would you like to send to sophia?" in short_term.lower()
        ):
            return {"category": "messages"}
        return {"category": "none"}

    async def process(
        self,
        user_input: str,
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        use_google_search: Optional[bool] = None,
        route: Optional[str] = None,
        system_prompt_override: Optional[str] = None,
        hardware_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        _retry_with_fallback_key: bool = True,
    ):
        input_text = str(user_input or "")
        runtime_memory = str(runtime_memory_context or "")
        route = str(route or "none")
        self.process_calls.append(
            {
                "user_input": input_text,
                "route": route,
                "runtime_memory_context": runtime_memory,
                "session_id": session_id,
            }
        )

        lowered = input_text.lower()
        if "send a message to sophia" in lowered:
            response = {
                "session_id": session_id,
                "text": "What message would you like to send to Sophia?",
            }
        elif (
            route == "messages"
            and "how are you doing today" in lowered
            and "send a message to sophia" in runtime_memory.lower()
            and "what message would you like to send to sophia?" in runtime_memory.lower()
        ):
            response = {
                "session_id": session_id,
                "text": "Sending your message to Sophia.",
                "command": "send_message",
                "args": {
                    "contact": "Sophia",
                    "message": "how are you doing today",
                },
            }
        else:
            response = {
                "session_id": session_id,
                "text": "Who should I send this message to?",
            }

        yield json.dumps(response)


class _RealProcessorTextModule:
    def __init__(self, provider: _MessagingFollowupProvider):
        self.is_initialized = True
        self.name = "text_processing"
        self._processor = TextProcessor()
        self._processor.is_initialized = True
        self._processor.live_provider = provider
        self.provider = provider
        self.requests: List[Dict[str, Any]] = []

    async def process(self, payload):
        text = payload.get("text", "")
        image_data = payload.get("image_data")
        session_id = payload.get("session_id")
        use_google_search = payload.get("use_google_search")
        hardware_id = payload.get("hardware_id")
        runtime_memory_context = payload.get("runtime_memory_context")
        prepared_request = payload.get("prepared_request")
        self.requests.append(
            {
                "text": text,
                "image_data": image_data,
                "session_id": session_id,
                "use_google_search": use_google_search,
                "hardware_id": hardware_id,
                "runtime_memory_context": runtime_memory_context,
                "prepared_request": prepared_request,
            }
        )

        async def _gen():
            async for chunk in self._processor.process_text_streaming(
                text=text,
                image_data=image_data,
                session_id=session_id,
                use_google_search=use_google_search,
                hardware_id=hardware_id,
                runtime_memory_context=runtime_memory_context,
                prepared_request=prepared_request,
            ):
                yield {"text": chunk, "type": "text_chunk"}

        return _gen()

    def get_processor(self):
        return self._processor


class _MatrixProvider:
    def __init__(self):
        self.classifier_calls: List[Dict[str, Any]] = []
        self.process_calls: List[Dict[str, Any]] = []

    @staticmethod
    def _norm(value: str) -> str:
        return " ".join(str(value or "").lower().split())

    @staticmethod
    def _allowed_commands() -> set[str]:
        try:
            from config.command_allowlist import get_allowed_commands_runtime
        except ImportError:
            from server.server.config.command_allowlist import get_allowed_commands_runtime
        return set(get_allowed_commands_runtime())

    def _response(
        self,
        *,
        session_id: Optional[str],
        text: str,
        command: Optional[str] = None,
        args: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        response: Dict[str, Any] = {"session_id": session_id, "text": text}
        if command and command in self._allowed_commands():
            response["command"] = command
            response["args"] = args or {}
        return response

    async def classify_intent_decision(self, user_input: str = "", classifier_context: Optional[Dict[str, str]] = None, **kwargs):
        input_text = str(user_input or kwargs.get("user_input", "") or "")
        short_term = str((classifier_context or {}).get("short_term_memory", ""))
        current_goal = str((classifier_context or {}).get("current_goal", ""))
        lowered = self._norm(input_text)
        short_norm = self._norm(short_term)
        goal_norm = self._norm(current_goal)
        category = "none"

        if lowered in {
            "send a message to sophia",
            "i need to send sophia a message",
            "drop sophia a note",
            "could you help me text sophia",
            "i wanna ping sophia",
            "send hello to sophia",
            "snd her im outside",
            "snd her ill b outside in 2",
            "msg her im downstairs now",
            "txt her im downstairs",
            "tell her im here",
            "text john running late",
            "tell her i'm running behind",
            "tell her i'll be late tonight",
            "tell her traffic's bad",
            "let her know i'll be there in ten",
        }:
            category = "messages"
        elif lowered == "how are you doing today" and ("send a message to sophia" in short_norm or "send sophia a message" in short_norm):
            category = "messages"
        elif lowered in {"tell her i will be late", "tell her i am on my way", "tell her i'll be late tonight"} and ("send a message to sophia" in goal_norm or "send sophia a message" in goal_norm or "to sophia" in goal_norm):
            category = "messages"
        elif lowered in {"nvm lost news insted", "nah just world headlines insted", "actually world headlines instead", "actually global headlines instead", "nah europe headlines instead"}:
            category = "google_search"
        elif lowered == "yes" and ("send a message to sophia" in goal_norm or "send sophia a message" in goal_norm):
            category = "messages"
        elif lowered in {
            "send a whatsapp message to mom",
            "can you whatsapp mom for me",
            "message mom on whatsapp",
            "i need to whatsapp mom",
            "whatsapp mom",
            "tell mom i arrived safely",
            "tell mom i got here safely",
            "say i made it home",
            "tell mom i'm outside",
            "tell mom dinner's ready",
        }:
            category = "whatsapp"
        elif lowered == "yes" and "whatsapp message to mom" in goal_norm:
            category = "whatsapp"
        if lowered in {
            "open youtube",
            "open youtube and play jazz",
            "go to youtube and put on some jazz",
            "pull up youtube and spin some jazz",
            "hop onto youtube and play some jazz",
            "open youtube and start jazz",
            "open reddit",
            "go to reddit",
            "opn yotube n ply lofi",
            "yt lofi insted",
            "yt lofi beats insted",
            "yt ambient rain swap",
            "yt rain ambi insted",
            "yt ocean noise swap",
            "yt sleep mix",
            "youtube rain sounds",
            "youtube",
        }:
            category = "browser"
        elif lowered == "youtube" and "open" in short_norm:
            category = "browser"
        elif lowered in {"sleep music", "rain sounds", "make it sleep music instead", "make it rain sounds instead", "switch it to sleep sounds", "switch it to sleep music", "swap it over to sleep sounds", "swap it over to rain sounds", "change it to sleep tracks", "change it to rain tracks"} and "youtube" in goal_norm:
            category = "browser"
        elif lowered == "yes" and "youtube" in goal_norm:
            category = "browser"
        elif lowered in {
            "find latest world news",
            "what's the latest world news",
            "what's the latest world news?",
            "whats the latest world news",
            "catch me up on world news",
            "world headlines",
            "global affairs",
            "give me the latest world headlines",
            "show me current world news",
            "world politics",
            "europe headlines",
            "latest news today",
            "lost news",
            "btc price now",
            "w e a t h e r toronto",
            "weather tornto",
        }:
            category = "google_search"
        elif lowered in {"world news", "world headlines", "world politics", "global affairs", "europe headlines", "bitcoin news"} and "news" in goal_norm:
            category = "google_search"
        elif lowered == "yes" and ("news" in goal_norm or "bitcoin price" in goal_norm):
            category = "google_search"
        elif lowered in {
            "what on screen now",
            "deskribe my scren",
            "wts on my scrn rn",
            "whats on my screen rn",
            "what's on screen atm",
            "wuts on screen rn",
            "screen rn what is there",
        }:
            category = "describe"
        elif lowered in {
            "open telegram",
            "open notes",
            "open notes app",
            "close spotify",
            "open safari",
            "could you open safari",
            "could you open safari?",
            "launch safari for me",
            "please launch safari",
            "start safari",
            "safari please",
            "safari app",
            "safari browser",
            "safari one",
        }:
            category = "system_control"
        elif lowered in {"safari", "safari please", "safari app", "safari browser", "safari one"} and ("open an app" in goal_norm or "open a program" in goal_norm or "open some app" in goal_norm or "open an application" in goal_norm):
            category = "system_control"
        elif lowered == "yes" and ("open safari" in goal_norm or "open an app" in goal_norm or "open a program" in goal_norm):
            category = "system_control"
        elif lowered == "safr" and ("open an app" in goal_norm or "open a program" in goal_norm):
            category = "system_control"
        elif lowered in {
            "what can you do",
            "what all can you help with",
            "what all can you help with?",
            "what are you able to do",
            "what sort of things can you do",
            "what sort of things can you do?",
            "what can you handle",
        }:
            category = "capability"
        elif lowered in {
            "how are you?",
            "how are you",
            "how's it going?",
            "how's it going",
            "how've you been?",
            "how've you been",
            "hows it going?",
            "hows it going",
            "you doing okay?",
            "you doing okay",
            "you alright today?",
            "you alright today",
        }:
            category = "none"
        elif lowered in {
            "helo",
            "qzx",
        }:
            category = "none"
        elif lowered in {"open", "open something for me", "open a program for me", "open some app", "open an application"}:
            category = "none"
        elif lowered in {
            "no",
            "not now",
            "no, never mind",
            "no, drop it",
            "forget that task",
            "cancel that",
            "forget that",
            "no, i am not interested now",
            "no, leave it",
            "no, i do not want to send a message",
            "no, i just want to know how are you doing",
        }:
            category = "none"
        elif lowered in {"no, open safari instead", "actually, open safari instead", "actually just launch safari", "scrap that, launch safari", "actually start safari"}:
            category = "system_control"
        elif lowered == "i want something else, find world news":
            category = "google_search"
        elif lowered in {"no, send a message to sophia instead", "actually, message sophia instead", "actually text sophia instead", "skip that, text sophia", "actually ping sophia"}:
            category = "messages"
        elif lowered == "actually open youtube instead":
            category = "browser"

        self.classifier_calls.append(
            {
                "user_input": input_text,
                "short_term_memory": short_term,
                "current_goal": current_goal,
                "category": category,
            }
        )
        return {"category": category}

    async def process(
        self,
        user_input: str,
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        use_google_search: Optional[bool] = None,
        route: Optional[str] = None,
        system_prompt_override: Optional[str] = None,
        hardware_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        _retry_with_fallback_key: bool = True,
    ):
        input_text = str(user_input or "")
        runtime_memory = str(runtime_memory_context or "")
        lowered = self._norm(input_text)
        runtime_goal = self._norm(TextProcessor._extract_memory_section(runtime_memory, "Current goal"))
        route = str(route or "none")
        self.process_calls.append(
            {
                "user_input": input_text,
                "route": route,
                "runtime_memory_context": runtime_memory,
                "current_goal": runtime_goal,
                "session_id": session_id,
            }
        )

        response = self._response(session_id=session_id, text="Can you clarify what you want?")

        if lowered == "send hello to sophia":
            response = self._response(
                session_id=session_id,
                text="Sending your message to Sophia.",
                command="send_message",
                args={"contact": "Sophia", "message": "hello"},
            )
        elif lowered in {"snd her im outside", "snd her ill b outside in 2", "txt her im downstairs", "msg her im downstairs now", "tell her im here"}:
            response = self._response(
                session_id=session_id,
                text="Sending your message to Sophia.",
                command="send_message",
                args={
                    "contact": "Sophia",
                    "message": (
                        "ill b outside in 2"
                        if lowered == "snd her ill b outside in 2"
                        else ("im downstairs" if lowered in {"txt her im downstairs", "msg her im downstairs now"} else ("im here" if lowered == "tell her im here" else "im outside"))
                    ),
                },
            )
        elif lowered == "text john running late":
            response = self._response(
                session_id=session_id,
                text="Sending your message to John.",
                command="send_message",
                args={"contact": "John", "message": "running late"},
            )
        elif lowered in {"send a message to sophia", "i need to send sophia a message", "could you help me text sophia", "drop sophia a note", "i wanna ping sophia"}:
            response = self._response(session_id=session_id, text="What message would you like to send to Sophia?")
        elif lowered == "how are you doing today" and route == "messages":
            response = self._response(
                session_id=session_id,
                text="Sending your message to Sophia.",
                command="send_message",
                args={"contact": "Sophia", "message": "how are you doing today"},
            )
        elif lowered in {"tell her i will be late", "tell her i'll be late tonight", "let her know i'll be there in ten", "tell her i'm running behind", "tell her traffic's bad"} and route == "messages" and ("sophia" in runtime_goal and "message" in runtime_goal):
            response = self._response(
                session_id=session_id,
                text="Sending your message to Sophia.",
                command="send_message",
                args={
                    "contact": "Sophia",
                    "message": (
                        "I'm running behind"
                        if lowered == "tell her i'm running behind"
                        else ("traffic's bad" if lowered == "tell her traffic's bad" else ("I'll be late tonight" if lowered == "tell her i'll be late tonight" else ("I'll be there in ten" if lowered == "let her know i'll be there in ten" else "I will be late")))
                    ),
                },
            )
        elif lowered == "tell her i am on my way" and route == "messages" and ("sophia" in runtime_goal and "message" in runtime_goal):
            response = self._response(
                session_id=session_id,
                text="Sending your message to Sophia.",
                command="send_message",
                args={"contact": "Sophia", "message": "I am on my way"},
            )
        elif lowered == "yes" and route == "messages" and ("sophia" in runtime_goal and "message" in runtime_goal):
            response = self._response(
                session_id=session_id,
                text="Sending your message to Sophia.",
                command="send_message",
                args={"contact": "Sophia", "message": "I am on my way"},
            )
        elif lowered in {"send a whatsapp message to mom", "can you whatsapp mom for me", "i need to whatsapp mom", "message mom on whatsapp", "whatsapp mom"}:
            response = self._response(session_id=session_id, text="What message do you want to send to Mom?")
        elif lowered in {"tell mom i arrived safely", "tell mom i got here safely", "tell mom dinner's ready", "say i made it home", "tell mom i'm outside"} and route == "whatsapp" and "whatsapp message to mom" in runtime_goal:
            response = self._response(
                session_id=session_id,
                text="Sending your WhatsApp message to Mom.",
                command="send_whatsapp_message",
                args={
                    "contact": "Mom",
                    "message": (
                        "I made it home"
                        if lowered == "say i made it home"
                        else ("I'm outside" if lowered == "tell mom i'm outside" else ("I got here safely" if lowered == "tell mom i got here safely" else ("Dinner's ready" if lowered == "tell mom dinner's ready" else "I arrived safely")))
                    ),
                },
            )
        elif lowered == "yes" and route == "whatsapp" and "whatsapp message to mom" in runtime_goal:
            response = self._response(
                session_id=session_id,
                text="Sending your WhatsApp message to Mom.",
                command="send_whatsapp_message",
                args={"contact": "Mom", "message": "I arrived safely"},
            )
        elif lowered == "open youtube":
            response = self._response(
                session_id=session_id,
                text="Opening YouTube.",
                command="browser_use",
                args={"task": "open youtube"},
            )
        elif lowered in {"open youtube and play jazz", "go to youtube and put on some jazz", "hop onto youtube and play some jazz", "pull up youtube and spin some jazz", "open youtube and start jazz"}:
            response = self._response(
                session_id=session_id,
                text=(
                    "Opening YouTube and starting jazz."
                    if lowered == "open youtube and start jazz"
                    else ("Opening YouTube and spinning some jazz." if lowered == "pull up youtube and spin some jazz" else ("Opening YouTube and putting on some jazz." if lowered == "go to youtube and put on some jazz" else ("Opening YouTube and playing some jazz." if lowered == "hop onto youtube and play some jazz" else "Opening YouTube and playing jazz.")))
                ),
                command="browser_use",
                args={
                    "task": (
                        "open youtube and start jazz"
                        if lowered == "open youtube and start jazz"
                        else ("pull up youtube and spin some jazz" if lowered == "pull up youtube and spin some jazz" else ("go to youtube and put on some jazz" if lowered == "go to youtube and put on some jazz" else ("hop onto youtube and play some jazz" if lowered == "hop onto youtube and play some jazz" else "open youtube and play jazz")))
                    )
                },
            )
        elif lowered == "opn yotube n ply lofi":
            response = self._response(
                session_id=session_id,
                text="Opening YouTube and playing lofi.",
                command="browser_use",
                args={"task": "open youtube and play lofi"},
            )
        elif lowered in {"yt lofi insted", "yt lofi beats insted", "yt rain ambi insted", "yt ambient rain swap", "yt ocean noise swap"}:
            response = self._response(
                session_id=session_id,
                text=(
                    "Opening YouTube and playing ambient rain."
                    if lowered == "yt ambient rain swap"
                    else ("Opening YouTube and playing ocean noise." if lowered == "yt ocean noise swap" else ("Opening YouTube and playing lofi beats." if lowered == "yt lofi beats insted" else ("Opening YouTube and playing rain ambience." if lowered == "yt rain ambi insted" else "Opening YouTube and playing lofi.")))
                ),
                command="browser_use",
                args={
                    "task": (
                        "open youtube and play ambient rain"
                        if lowered == "yt ambient rain swap"
                        else ("open youtube and play ocean noise" if lowered == "yt ocean noise swap" else ("open youtube and play lofi beats" if lowered == "yt lofi beats insted" else ("open youtube and play rain ambience" if lowered == "yt rain ambi insted" else "open youtube and play lofi")))
                    )
                },
            )
        elif lowered == "yt sleep mix":
            response = self._response(
                session_id=session_id,
                text="Opening YouTube sleep mix.",
                command="browser_use",
                args={"task": "open youtube sleep mix"},
            )
        elif lowered == "youtube rain sounds":
            response = self._response(
                session_id=session_id,
                text="Opening YouTube rain sounds.",
                command="browser_use",
                args={"task": "open youtube rain sounds"},
            )
        elif lowered in {"open reddit", "go to reddit"}:
            response = self._response(
                session_id=session_id,
                text="Opening Reddit.",
                command="browser_use",
                args={"task": "open reddit"},
            )
        elif lowered in {"open", "open something for me", "open a program for me", "open some app", "open an application"}:
            response = self._response(session_id=session_id, text="What do you want to open?")
        elif lowered in {"open youtube and find", "open youtube and find something for me"}:
            response = self._response(session_id=session_id, text="What should I find on YouTube?")
        elif lowered == "youtube" and route == "browser":
            response = self._response(
                session_id=session_id,
                text="Opening YouTube.",
                command="browser_use",
                args={"task": "open youtube"},
            )
        elif lowered in {"sleep music", "rain sounds", "make it sleep music instead", "make it rain sounds instead", "switch it to sleep sounds", "switch it to sleep music", "swap it over to sleep sounds", "swap it over to rain sounds", "change it to sleep tracks", "change it to rain tracks"} and route == "browser" and "youtube" in runtime_goal:
            response = self._response(
                session_id=session_id,
                text=(
                    "Opening YouTube to find sleep tracks."
                    if lowered == "change it to sleep tracks"
                    else ("Opening YouTube to find sleep music." if lowered in {"make it sleep music instead", "switch it to sleep sounds", "switch it to sleep music", "swap it over to sleep sounds"} else "Opening YouTube.")
                ),
                command="browser_use",
                args={
                    "task": (
                        "open youtube and find sleep tracks"
                        if lowered == "change it to sleep tracks"
                        else ("open youtube and find sleep music" if lowered in {"switch it to sleep sounds", "switch it to sleep music", "make it sleep music instead", "swap it over to sleep sounds"} else ("open youtube and find rain sounds" if lowered in {"make it rain sounds instead", "swap it over to rain sounds", "change it to rain tracks"} else f"open youtube and play {lowered}"))
                    )
                },
            )
        elif lowered == "yes" and route == "browser" and "youtube" in runtime_goal:
            response = self._response(
                session_id=session_id,
                text="Opening YouTube.",
                command="browser_use",
                args={"task": "open youtube"},
            )
        elif lowered == "latest news today":
            response = self._response(session_id=session_id, text="Here are the latest news headlines today.")
        elif lowered in {"find latest world news", "what's the latest world news", "what's the latest world news?", "whats the latest world news", "give me the latest world headlines", "catch me up on world news", "show me current world news"}:
            response = self._response(session_id=session_id, text="Here are the latest world news headlines.")
        elif lowered == "world politics":
            response = self._response(session_id=session_id, text="Here are the latest world politics headlines.")
        elif lowered == "europe headlines":
            response = self._response(session_id=session_id, text="Here are the latest Europe headlines.")
        elif lowered == "lost news":
            response = self._response(session_id=session_id, text="Here are the latest news headlines.")
        elif lowered in {"nvm lost news insted", "nah just world headlines insted", "nah jus global headlines insted", "actually world headlines instead", "actually global headlines instead"}:
            response = self._response(
                session_id=session_id,
                text="Here are the latest global headlines." if lowered in {"nah jus global headlines insted", "actually global headlines instead"} else "Here are the latest world news headlines.",
            )
        elif lowered == "nah europe headlines instead":
            response = self._response(session_id=session_id, text="Here are the latest Europe headlines.")
        elif lowered == "btc price now":
            response = self._response(session_id=session_id, text="Here is the current Bitcoin price.")
        elif lowered in {"world news", "world headlines", "global affairs"} and route == "google_search":
            response = self._response(session_id=session_id, text="Here are the latest world news headlines.")
        elif lowered == "world politics" and route == "google_search":
            response = self._response(session_id=session_id, text="Here are the latest world politics headlines.")
        elif lowered == "bitcoin news" and route == "google_search":
            response = self._response(session_id=session_id, text="Here are the latest bitcoin news headlines.")
        elif lowered == "yes" and route == "google_search":
            response = self._response(session_id=session_id, text="Here are the latest bitcoin price results.")
        elif lowered == "w e a t h e r toronto":
            response = self._response(session_id=session_id, text="Here is the weather for Toronto.")
        elif lowered == "weather tornto":
            response = self._response(session_id=session_id, text="Here is the weather for Toronto.")
        elif lowered == "what on screen now":
            response = self._response(session_id=session_id, text="Describing what is currently on the screen.")
        elif lowered in {"deskribe my scren", "wts on my scrn rn", "whats on my screen rn", "wuts on screen rn", "what's on screen atm", "screen rn what is there"}:
            response = self._response(session_id=session_id, text="Describing your screen.")
        elif lowered in {"open safari", "could you open safari", "could you open safari?", "safari please", "please launch safari", "safari app", "launch safari for me", "start safari", "safari browser", "safari one"}:
            response = self._response(
                session_id=session_id,
                text="Opening Safari.",
                command="open_app",
                args={"app_name": "Safari"},
            )
        elif lowered == "safr":
            response = self._response(
                session_id=session_id,
                text="Opening Safari.",
                command="open_app",
                args={"app_name": "Safari"},
            )
        elif lowered == "open telegram":
            response = self._response(
                session_id=session_id,
                text="Opening Telegram.",
                command="open_app",
                args={"app_name": "Telegram"},
            )
        elif lowered in {"open notes", "open notes app"}:
            response = self._response(
                session_id=session_id,
                text="Opening Notes.",
                command="open_app",
                args={"app_name": "Notes"},
            )
        elif lowered == "close spotify":
            response = self._response(
                session_id=session_id,
                text="Closing Spotify.",
                command="close_app",
                args={"app_name": "Spotify"},
            )
        elif lowered in {"safari", "safari please", "safari browser", "safari one"} and route == "system_control":
            response = self._response(
                session_id=session_id,
                text="Opening Safari.",
                command="open_app",
                args={"app_name": "Safari"},
            )
        elif lowered == "yes" and route == "system_control":
            response = self._response(
                session_id=session_id,
                text="Opening Safari.",
                command="open_app",
                args={"app_name": "Safari"},
            )
        elif lowered in {"what can you do", "what all can you help with", "what all can you help with?", "what sort of things can you do", "what sort of things can you do?", "what are you able to do", "what can you handle"}:
            response = self._response(
                session_id=session_id,
                text="I can help with apps, browser, messages, search, screen description, and device actions.",
            )
        elif lowered in {"how are you?", "how are you", "how's it going?", "how's it going", "hows it going?", "hows it going", "you doing okay?", "you doing okay", "how've you been?", "how've you been", "you alright today?", "you alright today"}:
            response = self._response(session_id=session_id, text="I am doing well, thanks for asking.")
        elif lowered in {"helo", "qzx"}:
            response = self._response(session_id=session_id, text="Can you clarify what you mean?")
        elif lowered in {
            "no",
            "not now",
            "no, never mind",
            "no, drop it",
            "forget that",
            "forget that task",
            "cancel that",
            "no, i am not interested now",
            "no, leave it",
            "no, i do not want to send a message",
        }:
            response = self._response(session_id=session_id, text="Okay, I will not continue that task.")
        elif lowered == "no, i just want to know how are you doing":
            response = self._response(session_id=session_id, text="I am doing well, thanks for asking.")
        elif lowered in {"no, open safari instead", "actually, open safari instead", "actually just launch safari", "scrap that, launch safari", "actually start safari"}:
            response = self._response(
                session_id=session_id,
                text="Opening Safari.",
                command="open_app",
                args={"app_name": "Safari"},
            )
        elif lowered == "i want something else, find world news":
            response = self._response(session_id=session_id, text="Here are the latest world news headlines.")
        elif lowered in {"no, send a message to sophia instead", "actually, message sophia instead", "actually text sophia instead", "skip that, text sophia", "actually ping sophia"}:
            response = self._response(session_id=session_id, text="What message would you like to send to Sophia?")
        elif lowered == "actually open youtube instead":
            response = self._response(
                session_id=session_id,
                text="Opening YouTube.",
                command="browser_use",
                args={"task": "open youtube"},
            )

        yield json.dumps(response)

    async def process_with_image(
        self,
        user_input: str,
        image_data: Optional[str] = None,
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        use_google_search: Optional[bool] = None,
        route: Optional[str] = None,
        system_prompt_override: Optional[str] = None,
        hardware_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        _retry_with_fallback_key: bool = True,
    ):
        # Matrix describe flow must use the same route owner as runtime:
        # image path exists only for describe, but response semantics stay identical.
        async for chunk in self.process(
            user_input=user_input,
            session_id=session_id,
            use_search=use_search,
            use_google_search=use_google_search,
            route=route,
            system_prompt_override=system_prompt_override,
            hardware_id=hardware_id,
            runtime_memory_context=runtime_memory_context,
            _retry_with_fallback_key=_retry_with_fallback_key,
        ):
            yield chunk


@pytest_asyncio.fixture
async def matrix_flow_stack():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = None

    memory_adapter = MemoryManagementAdapter()
    memory_adapter._manager = manager

    memory_workflow = MemoryWorkflowIntegration(memory_manager=memory_adapter)
    await memory_workflow.initialize()

    provider = _MatrixProvider()
    text_module = _RealProcessorTextModule(provider)
    audio_module = _AudioChunkModule()

    streaming = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    await streaming.initialize()

    service = GrpcServiceIntegration(
        streaming_workflow=streaming,
        memory_workflow=memory_workflow,
        interrupt_workflow=None,
    )
    await service.initialize()

    return {
        "db": db,
        "manager": manager,
        "memory_workflow": memory_workflow,
        "provider": provider,
        "text_module": text_module,
        "service": service,
    }


def _text_outputs(items: List[Dict[str, Any]]) -> str:
    return " ".join(str(item.get("text_response", "")).strip() for item in items if item.get("text_response")).strip()


async def _seed_snapshot(
    db: _StatefulFakeDB,
    hardware_id: str,
    *,
    current_goal: str,
    short_current: str,
    short_previous: Optional[List[str]] = None,
    factual_long: str = "",
):
    snapshot = {
        "schema": "memory_v2",
        "updated_at": "2026-03-07T02:30:00+00:00",
        "current_goal": current_goal,
        "short_current": short_current,
        "short_previous": list(short_previous or []),
        "medium": "",
        "medium_updated_at": "",
        "factual_long": factual_long,
    }
    db.short = json.dumps(snapshot, ensure_ascii=True)
    db.long = factual_long


def _build_registry_matrix_cases(cases) -> List[Dict[str, Any]]:
    matrix_cases: List[Dict[str, Any]] = []
    for index, gate_case in enumerate(cases, start=1):
        if gate_case.deterministic_request is None:
            raise RuntimeError(f"Deterministic contract missing for {gate_case.case_id}")
        matrix_cases.append(
            {
                "id": gate_case.case_id,
                "hardware_id": f"hw-matrix-{index:02d}",
                "setup": list(gate_case.deterministic_setup),
                "seed_goal": gate_case.deterministic_seed_goal,
                "seed_turn": gate_case.deterministic_seed_turn,
                "request": gate_case.deterministic_request,
                "expected_category": gate_case.deterministic_expected_category,
                "expected_route": gate_case.deterministic_expected_route,
                "expected_command": gate_case.deterministic_expected_command,
                "expected_args": gate_case.deterministic_expected_args or {},
                "expected_text": gate_case.deterministic_expected_text,
            }
        )
    return matrix_cases

MATRIX_CASES = _build_registry_matrix_cases(CANONICAL_20_CASE_GATE)
SUPPLEMENTAL_MATRIX_CASES = _build_registry_matrix_cases(SUPPLEMENTAL_20_CASE_GATE)
L1_BASIC_DIRECT_MATRIX_CASES = _build_registry_matrix_cases(L1_BASIC_DIRECT_20_CASE_GATE)
L2_CLARIFICATION_SLOT_FILL_MATRIX_CASES = _build_registry_matrix_cases(L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE)
L1_DIRECT_CONFIDENCE_MATRIX_CASES = _build_registry_matrix_cases(L1_DIRECT_CONFIDENCE_PROBES)


SEQUENTIAL_FLOW_CASES = [
    {
        "id": "turn-01-capability",
        "request": "what can you do",
        "expected_category": "capability",
        "expected_route": "capability",
        "expected_text": "I can help with apps, browser, messages, search, screen description, and device actions.",
    },
    {
        "id": "turn-02-open-fragment",
        "request": "open",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "What do you want to open?",
    },
    {
        "id": "turn-03-browser-followup",
        "request": "youtube",
        "expected_category": "browser",
        "expected_route": "browser",
        "expected_command": "browser_use",
        "expected_args": {"task": "open youtube"},
        "expected_text": "Opening YouTube.",
        "memory_must_contain": ["open", "What do you want to open?"],
    },
    {
        "id": "turn-04-search-news",
        "request": "latest news today",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here are the latest news headlines today.",
    },
    {
        "id": "turn-05-search-noisy-news",
        "request": "lost news",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here are the latest news headlines.",
    },
    {
        "id": "turn-06-search-weather-fragment",
        "request": "w e a t h e r toronto",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here is the weather for Toronto.",
    },
    {
        "id": "turn-07-describe-clean",
        "request": "what on screen now",
        "expected_category": "describe",
        "expected_route": "describe",
        "expected_text": "Describing what is currently on the screen.",
    },
    {
        "id": "turn-08-system-open-app",
        "request": "open telegram",
        "expected_category": "system_control",
        "expected_route": "system_control",
        "expected_command": "open_app",
        "expected_args": {"app_name": "Telegram"},
        "expected_text": "Opening Telegram.",
    },
    {
        "id": "turn-09-system-close-app",
        "request": "close spotify",
        "expected_category": "system_control",
        "expected_route": "system_control",
        "expected_command": "close_app",
        "expected_args": {"app_name": "Spotify"},
        "expected_text": "Closing Spotify.",
    },
    {
        "id": "turn-10-message-contact",
        "request": "send a message to Sophia",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_text": "What message would you like to send to Sophia?",
    },
    {
        "id": "turn-11-message-followup",
        "request": "how are you doing today",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_command": "send_message",
        "expected_args": {"contact": "Sophia", "message": "how are you doing today"},
        "expected_text": "Sending your message to Sophia.",
        "memory_must_contain": [
            "send a message to Sophia",
            "What message would you like to send to Sophia?",
        ],
    },
    {
        "id": "turn-12-message-direct",
        "request": "send hello to Sophia",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_command": "send_message",
        "expected_args": {"contact": "Sophia", "message": "hello"},
        "expected_text": "Sending your message to Sophia.",
    },
    {
        "id": "turn-13-browser-noisy-lofi",
        "request": "opn yotube n ply lofi",
        "expected_category": "browser",
        "expected_route": "browser",
        "expected_command": "browser_use",
        "expected_args": {"task": "open youtube and play lofi"},
        "expected_text": "Opening YouTube and playing lofi.",
    },
    {
        "id": "turn-14-browser-short-music",
        "request": "yt sleep mix",
        "expected_category": "browser",
        "expected_route": "browser",
        "expected_command": "browser_use",
        "expected_args": {"task": "open youtube sleep mix"},
        "expected_text": "Opening YouTube sleep mix.",
    },
    {
        "id": "turn-15-describe-noisy",
        "request": "deskribe my scren",
        "expected_category": "describe",
        "expected_route": "describe",
        "expected_text": "Describing your screen.",
    },
    {
        "id": "turn-16-search-btc",
        "request": "btc price now",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here is the current Bitcoin price.",
    },
    {
        "id": "turn-17-search-weather-typo",
        "request": "weather tornto",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here is the weather for Toronto.",
    },
    {
        "id": "turn-18-message-compact",
        "request": "text john running late",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_command": "send_message",
        "expected_args": {"contact": "John", "message": "running late"},
        "expected_text": "Sending your message to John.",
    },
    {
        "id": "turn-19-unknown",
        "request": "qzx",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "Can you clarify what you mean?",
    },
    {
        "id": "turn-20-capability-repeat",
        "request": "what can you do",
        "expected_category": "capability",
        "expected_route": "capability",
        "expected_text": "I can help with apps, browser, messages, search, screen description, and device actions.",
    },
]


CURRENT_GOAL_FULL_CYCLE_CASES = [
    {
        "id": "goal-message-payload",
        "request": "tell her I will be late",
        "seed_goal": "User wants to send a message to Sophia. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:20:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_text": "Sending your message to Sophia.",
        "expected_command": "send_message",
        "expected_args": {"contact": "Sophia", "message": "I will be late"},
        "goal_fragment": "send a message to sophia",
    },
    {
        "id": "goal-message-confirm-yes",
        "request": "yes",
        "seed_goal": "User wants to send a message to Sophia.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:21:00 UTC\nUSER: send a message to Sophia saying I am on my way\nASSISTANT: Do you want me to send it now?",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_text": "Sending your message to Sophia.",
        "expected_command": "send_message",
        "expected_args": {"contact": "Sophia", "message": "I am on my way"},
        "goal_fragment": "send a message to sophia",
    },
    {
        "id": "goal-browser-query",
        "request": "sleep music",
        "seed_goal": "User wants to search YouTube. Missing detail: search query.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:22:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
        "expected_category": "browser",
        "expected_route": "browser",
        "expected_text": "Opening YouTube.",
        "expected_command": "browser_use",
        "expected_args": {"task": "open youtube and play sleep music"},
        "goal_fragment": "youtube",
    },
    {
        "id": "goal-browser-confirm-yes",
        "request": "yes",
        "seed_goal": "User wants to open YouTube.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:23:00 UTC\nUSER: open YouTube\nASSISTANT: Do you want me to open YouTube now?",
        "expected_category": "browser",
        "expected_route": "browser",
        "expected_text": "Opening YouTube.",
        "expected_command": "browser_use",
        "expected_args": {"task": "open youtube"},
        "goal_fragment": "youtube",
    },
    {
        "id": "goal-search-topic",
        "request": "world news",
        "seed_goal": "User wants news. Missing detail: topic.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:24:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here are the latest world news headlines.",
        "goal_fragment": "news",
    },
    {
        "id": "goal-search-confirm-yes",
        "request": "yes",
        "seed_goal": "User wants latest bitcoin price.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:25:00 UTC\nUSER: find latest bitcoin price\nASSISTANT: Do you want me to search for the latest bitcoin price now?",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here are the latest bitcoin price results.",
        "goal_fragment": "bitcoin price",
    },
    {
        "id": "goal-system-target",
        "request": "Safari",
        "seed_goal": "User wants to open an app. Missing detail: app name.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:26:00 UTC\nUSER: open\nASSISTANT: What app do you want to open?",
        "expected_category": "system_control",
        "expected_route": "system_control",
        "expected_text": "Opening Safari.",
        "expected_command": "open_app",
        "expected_args": {"app_name": "Safari"},
        "goal_fragment": "open an app",
    },
    {
        "id": "goal-system-confirm-yes",
        "request": "yes",
        "seed_goal": "User wants to open Safari.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:27:00 UTC\nUSER: open Safari\nASSISTANT: Do you want me to open Safari now?",
        "expected_category": "system_control",
        "expected_route": "system_control",
        "expected_text": "Opening Safari.",
        "expected_command": "open_app",
        "expected_args": {"app_name": "Safari"},
        "goal_fragment": "open safari",
    },
    {
        "id": "goal-whatsapp-payload",
        "request": "tell Mom I arrived safely",
        "seed_goal": "User wants to send a WhatsApp message to Mom. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:28:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
        "expected_category": "whatsapp",
        "expected_route": "whatsapp",
        "expected_text": "Sending your WhatsApp message to Mom.",
        "expected_command": "send_whatsapp_message",
        "expected_args": {"contact": "Mom", "message": "I arrived safely"},
        "goal_fragment": "whatsapp message to mom",
    },
    {
        "id": "goal-whatsapp-confirm-yes",
        "request": "yes",
        "seed_goal": "User wants to send a WhatsApp message to Mom.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:29:00 UTC\nUSER: send a WhatsApp message to Mom saying I arrived safely\nASSISTANT: Do you want me to send it now?",
        "expected_category": "whatsapp",
        "expected_route": "whatsapp",
        "expected_text": "Sending your WhatsApp message to Mom.",
        "expected_command": "send_whatsapp_message",
        "expected_args": {"contact": "Mom", "message": "I arrived safely"},
        "goal_fragment": "whatsapp message to mom",
    },
    {
        "id": "goal-message-cancel",
        "request": "no, I do not want to send a message",
        "seed_goal": "User wants to send a message to Sophia. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:30:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "Okay, I will not continue that task.",
        "goal_fragment": "send a message to sophia",
    },
    {
        "id": "goal-message-topic-switch-smalltalk",
        "request": "no, I just want to know how are you doing",
        "seed_goal": "User wants to send a message to Sophia. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:31:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "I am doing well, thanks for asking.",
        "goal_fragment": "send a message to sophia",
    },
    {
        "id": "goal-message-pivot-system",
        "request": "no, open Safari instead",
        "seed_goal": "User wants to send a message to Sophia. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:32:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
        "expected_category": "system_control",
        "expected_route": "system_control",
        "expected_text": "Opening Safari.",
        "expected_command": "open_app",
        "expected_args": {"app_name": "Safari"},
        "goal_fragment": "send a message to sophia",
    },
    {
        "id": "goal-browser-cancel",
        "request": "no, never mind",
        "seed_goal": "User wants to search YouTube. Missing detail: search query.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:33:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "Okay, I will not continue that task.",
        "goal_fragment": "youtube",
    },
    {
        "id": "goal-browser-pivot-messages",
        "request": "no, send a message to Sophia instead",
        "seed_goal": "User wants to search YouTube. Missing detail: search query.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:34:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
        "expected_category": "messages",
        "expected_route": "messages",
        "expected_text": "What message would you like to send to Sophia?",
        "goal_fragment": "youtube",
    },
    {
        "id": "goal-search-cancel",
        "request": "no, I am not interested now",
        "seed_goal": "User wants news. Missing detail: topic.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:35:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "Okay, I will not continue that task.",
        "goal_fragment": "news",
    },
    {
        "id": "goal-search-pivot-browser",
        "request": "actually open YouTube instead",
        "seed_goal": "User wants news. Missing detail: topic.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:36:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
        "expected_category": "browser",
        "expected_route": "browser",
        "expected_text": "Opening YouTube.",
        "expected_command": "browser_use",
        "expected_args": {"task": "open youtube"},
        "goal_fragment": "news",
    },
    {
        "id": "goal-system-cancel",
        "request": "no, leave it",
        "seed_goal": "User wants to open an app. Missing detail: app name.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:37:00 UTC\nUSER: open\nASSISTANT: What app do you want to open?",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "Okay, I will not continue that task.",
        "goal_fragment": "open an app",
    },
    {
        "id": "goal-whatsapp-cancel",
        "request": "not now",
        "seed_goal": "User wants to send a WhatsApp message to Mom. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:38:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
        "expected_category": "none",
        "expected_route": "none",
        "expected_text": "Okay, I will not continue that task.",
        "goal_fragment": "whatsapp message to mom",
    },
    {
        "id": "goal-whatsapp-pivot-search",
        "request": "I want something else, find world news",
        "seed_goal": "User wants to send a WhatsApp message to Mom. Missing detail: message text.",
        "seed_turn": "CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:39:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
        "expected_category": "google_search",
        "expected_route": "google_search",
        "expected_text": "Here are the latest world news headlines.",
        "goal_fragment": "whatsapp message to mom",
    },
]


@pytest.mark.asyncio
@pytest.mark.parametrize("case", MATRIX_CASES, ids=[case["id"] for case in MATRIX_CASES])
async def test_classifier_generator_matrix_20_of_20(case, matrix_flow_stack):
    service = matrix_flow_stack["service"]
    provider = matrix_flow_stack["provider"]
    text_module = matrix_flow_stack["text_module"]
    db = matrix_flow_stack["db"]

    if case.get("seed_goal") and case.get("seed_turn"):
        await _seed_snapshot(
            db,
            case["hardware_id"],
            current_goal=case["seed_goal"],
            short_current=case["seed_turn"],
        )

    for index, setup_text in enumerate(case.get("setup", []), start=1):
        setup_items = await _run_request(
            service,
            {
                "text": setup_text,
                "session_id": f'{case["id"]}-setup-{index}',
                "hardware_id": case["hardware_id"],
            },
        )
        assert _count_audio_chunks(setup_items) > 0

    items = await _run_request(
        service,
        {
            "text": case["request"],
            "session_id": f'{case["id"]}-main',
            "hardware_id": case["hardware_id"],
            "screenshot": _DUMMY_SCREENSHOT_B64,
        },
    )

    assert _count_audio_chunks(items) > 0
    assert provider.classifier_calls, f'classifier was not called for {case["id"]}'
    assert provider.process_calls, f'generator was not called for {case["id"]}'

    classifier_call = provider.classifier_calls[-1]
    process_call = provider.process_calls[-1]
    text_module_call = text_module.requests[-1]
    assert classifier_call["user_input"] == case["request"]
    assert process_call["route"] == case["expected_route"]
    if case.get("setup"):
        assert classifier_call["short_term_memory"], f'short-term memory missing for {case["id"]}'
        assert process_call["runtime_memory_context"], f'runtime memory missing for {case["id"]}'

    expected_search = case["expected_route"] == "google_search"
    assert bool(text_module_call["use_google_search"]) is expected_search

    expected_image = case["expected_route"] == "describe"
    assert bool(text_module_call["image_data"]) is expected_image

    text_output = _text_outputs(items)
    assert case["expected_text"] in text_output

    prepared_request = text_module_call["prepared_request"] or {}
    assert str(prepared_request.get("route", "none") or "none") == case["expected_route"]
    assert bool(prepared_request.get("use_google_search", False)) is expected_search

    expected_command = case.get("expected_command")
    command_payloads = [
        item.get("command_payload")
        for item in items
        if isinstance(item.get("command_payload"), dict)
    ]
    if expected_command:
        assert command_payloads, f'command payload missing for {case["id"]}'
        final_payload = command_payloads[-1]["payload"]
        assert final_payload.get("command") == expected_command
        for key, value in case.get("expected_args", {}).items():
            assert final_payload.get("args", {}).get(key) == value
    else:
        assert not command_payloads, f'unexpected command payload for {case["id"]}'


@pytest.mark.asyncio
@pytest.mark.parametrize("case", SUPPLEMENTAL_MATRIX_CASES, ids=[case["id"] for case in SUPPLEMENTAL_MATRIX_CASES])
async def test_classifier_generator_additional_20(case, matrix_flow_stack):
    await test_classifier_generator_matrix_20_of_20(case, matrix_flow_stack)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", L1_BASIC_DIRECT_MATRIX_CASES, ids=[case["id"] for case in L1_BASIC_DIRECT_MATRIX_CASES])
async def test_classifier_generator_l1_basic_direct_campaign(case, matrix_flow_stack):
    await test_classifier_generator_matrix_20_of_20(case, matrix_flow_stack)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", L2_CLARIFICATION_SLOT_FILL_MATRIX_CASES, ids=[case["id"] for case in L2_CLARIFICATION_SLOT_FILL_MATRIX_CASES])
async def test_classifier_generator_l2_clarification_slot_fill_campaign(case, matrix_flow_stack):
    await test_classifier_generator_matrix_20_of_20(case, matrix_flow_stack)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", L1_DIRECT_CONFIDENCE_MATRIX_CASES, ids=[case["id"] for case in L1_DIRECT_CONFIDENCE_MATRIX_CASES])
async def test_classifier_generator_l1_direct_confidence_probes(case, matrix_flow_stack):
    await test_classifier_generator_matrix_20_of_20(case, matrix_flow_stack)


@pytest.mark.asyncio
async def test_classifier_generator_sequential_memory_flow_20_of_20(matrix_flow_stack):
    service = matrix_flow_stack["service"]
    provider = matrix_flow_stack["provider"]
    text_module = matrix_flow_stack["text_module"]

    hardware_id = "hw-sequential-20-flow-01"
    start_classifier_calls = len(provider.classifier_calls)
    start_process_calls = len(provider.process_calls)
    start_text_requests = len(text_module.requests)

    for index, case in enumerate(SEQUENTIAL_FLOW_CASES, start=1):
        items = await _run_request(
            service,
            {
                "text": case["request"],
                "session_id": f"seq20-turn-{index:02d}",
                "hardware_id": hardware_id,
                "screenshot": _DUMMY_SCREENSHOT_B64,
            },
        )

        assert _count_audio_chunks(items) > 0, f"audio missing for {case['id']}"
        assert len(provider.classifier_calls) == start_classifier_calls + index
        assert len(provider.process_calls) == start_process_calls + index
        assert len(text_module.requests) == start_text_requests + index

        classifier_call = provider.classifier_calls[-1]
        process_call = provider.process_calls[-1]
        text_module_call = text_module.requests[-1]
        text_output = _text_outputs(items)
        prepared_request = text_module_call["prepared_request"] or {}

        assert classifier_call["user_input"] == case["request"]
        assert classifier_call["category"] == case["expected_category"]
        assert process_call["route"] == case["expected_route"]
        assert str(prepared_request.get("route", "none") or "none") == case["expected_route"]
        assert case["expected_text"] in text_output

        expected_search = case["expected_route"] == "google_search"
        expected_image = case["expected_route"] == "describe"
        assert bool(text_module_call["use_google_search"]) is expected_search
        assert bool(prepared_request.get("use_google_search", False)) is expected_search
        assert bool(text_module_call["image_data"]) is expected_image

        expected_command = case.get("expected_command")
        command_payloads = [
            item.get("command_payload")
            for item in items
            if isinstance(item.get("command_payload"), dict)
        ]
        if expected_command:
            assert command_payloads, f"command payload missing for {case['id']}"
            final_payload = command_payloads[-1]["payload"]
            assert final_payload.get("command") == expected_command
            for key, value in case.get("expected_args", {}).items():
                assert final_payload.get("args", {}).get(key) == value
        else:
            assert not command_payloads, f"unexpected command payload for {case['id']}"

        if index > 1:
            assert classifier_call["short_term_memory"], f"short-term memory missing for {case['id']}"
            assert process_call["runtime_memory_context"], f"runtime memory missing for {case['id']}"

        for expected_memory_item in case.get("memory_must_contain", []):
            assert expected_memory_item in classifier_call["short_term_memory"]
            assert expected_memory_item in process_call["runtime_memory_context"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "case",
    CURRENT_GOAL_FULL_CYCLE_CASES,
    ids=[case["id"] for case in CURRENT_GOAL_FULL_CYCLE_CASES],
)
async def test_classifier_generator_current_goal_lifecycle_full_cycle_20_of_20(case, matrix_flow_stack):
    service = matrix_flow_stack["service"]
    provider = matrix_flow_stack["provider"]
    text_module = matrix_flow_stack["text_module"]
    db = matrix_flow_stack["db"]

    hardware_id = f'hw-goal-cycle-{case["id"]}'
    await _seed_snapshot(
        db,
        hardware_id,
        current_goal=case["seed_goal"],
        short_current=case["seed_turn"],
    )

    items = await _run_request(
        service,
        {
            "text": case["request"],
            "session_id": f'{case["id"]}-main',
            "hardware_id": hardware_id,
            "screenshot": _DUMMY_SCREENSHOT_B64,
        },
    )

    assert _count_audio_chunks(items) > 0
    assert provider.classifier_calls, f'classifier was not called for {case["id"]}'
    assert provider.process_calls, f'generator was not called for {case["id"]}'

    classifier_call = provider.classifier_calls[-1]
    process_call = provider.process_calls[-1]
    text_module_call = text_module.requests[-1]
    prepared_request = text_module_call["prepared_request"] or {}

    assert classifier_call["user_input"] == case["request"]
    assert classifier_call["category"] == case["expected_category"]
    assert case["goal_fragment"] in str(classifier_call["current_goal"]).lower()

    assert process_call["route"] == case["expected_route"]
    assert case["goal_fragment"] in str(process_call["current_goal"]).lower()
    assert case["seed_goal"] in str(process_call["runtime_memory_context"])
    assert str(prepared_request.get("route", "none") or "none") == case["expected_route"]

    text_output = _text_outputs(items)
    assert case["expected_text"] in text_output

    expected_command = case.get("expected_command")
    command_payloads = [
        item.get("command_payload")
        for item in items
        if isinstance(item.get("command_payload"), dict)
    ]
    if expected_command:
        assert command_payloads, f'command payload missing for {case["id"]}'
        final_payload = command_payloads[-1]["payload"]
        assert final_payload.get("command") == expected_command
        for key, value in case.get("expected_args", {}).items():
            assert final_payload.get("args", {}).get(key) == value
    else:
        assert not command_payloads, f'unexpected command payload for {case["id"]}'


@pytest_asyncio.fixture
async def factual_stack():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    # Фактический режим: без LLM-анализатора, только deterministic memory path.
    manager.memory_analyzer = None

    memory_adapter = MemoryManagementAdapter()
    memory_adapter._manager = manager

    memory_workflow = MemoryWorkflowIntegration(memory_manager=memory_adapter)
    await memory_workflow.initialize()

    text_module = _FactAwareTextModule()
    audio_module = _AudioChunkModule()

    streaming = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    await streaming.initialize()

    service = GrpcServiceIntegration(
        streaming_workflow=streaming,
        memory_workflow=memory_workflow,
        interrupt_workflow=None,
    )
    await service.initialize()

    return {
        "db": db,
        "manager": manager,
        "memory_workflow": memory_workflow,
        "text_module": text_module,
        "service": service,
    }


@pytest_asyncio.fixture
async def messaging_followup_stack():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = None

    memory_adapter = MemoryManagementAdapter()
    memory_adapter._manager = manager

    memory_workflow = MemoryWorkflowIntegration(memory_manager=memory_adapter)
    await memory_workflow.initialize()

    provider = _MessagingFollowupProvider()
    text_module = _RealProcessorTextModule(provider)
    audio_module = _AudioChunkModule()

    streaming = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    await streaming.initialize()

    service = GrpcServiceIntegration(
        streaming_workflow=streaming,
        memory_workflow=memory_workflow,
        interrupt_workflow=None,
    )
    await service.initialize()

    return {
        "db": db,
        "manager": manager,
        "memory_workflow": memory_workflow,
        "provider": provider,
        "service": service,
    }


async def _run_request(service: GrpcServiceIntegration, request_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    async for item in service.process_request_complete(request_data):
        items.append(item)
    return items


def _count_audio_chunks(items: List[Dict[str, Any]]) -> int:
    return sum(1 for item in items if isinstance(item.get("audio_chunk"), (bytes, bytearray)))


@pytest.mark.asyncio
async def test_full_cycle_memory_db_cache_and_audio_chunks(factual_stack):
    service = factual_stack["service"]
    db = factual_stack["db"]
    text_module = factual_stack["text_module"]
    memory_workflow = factual_stack["memory_workflow"]

    hardware_id = "hw-factual-cycle-1"

    req1_items = await _run_request(
        service,
        {
            "text": "Запомни: меня зовут Сергей, и я люблю спорт",
            "session_id": "sess-factual-1",
            "hardware_id": hardware_id,
        },
    )
    assert _count_audio_chunks(req1_items) > 0
    assert db.updates >= 1
    assert "серг" in db.long.lower()

    req2_items = await _run_request(
        service,
        {
            "text": "Что ты помнишь про меня?",
            "session_id": "sess-factual-2",
            "hardware_id": hardware_id,
        },
    )
    assert _count_audio_chunks(req2_items) > 0

    # Проверяем, что генератор реально получил memory context (не "магию").
    second_call = text_module.requests[-1]
    runtime_memory = second_call["runtime_memory_context"]
    assert "Short-term memory:" in runtime_memory
    assert "Long-term memory:" in runtime_memory
    assert "серг" in runtime_memory.lower()

    # Проверяем, что write-through кэш реально заполнен.
    cache_key = memory_workflow._variant_key(hardware_id, None, True)
    assert cache_key in memory_workflow.memory_cache


@pytest.mark.asyncio
async def test_ragged_requests_are_persisted_and_replayed_in_short_term_memory(factual_stack):
    service = factual_stack["service"]
    manager = factual_stack["manager"]
    text_module = factual_stack["text_module"]

    hardware_id = "hw-factual-ragged-1"

    ragged_inputs = [
        ("sess-ragged-1", "Отправь сообщение"),
        ("sess-ragged-2", "София как у тебя дела"),
        ("sess-ragged-3", "И скажи ей я буду через 10"),
    ]

    for session_id, text in ragged_inputs:
        items = await _run_request(
            service,
            {
                "text": text,
                "session_id": session_id,
                "hardware_id": hardware_id,
            },
        )
        assert _count_audio_chunks(items) > 0

    context = await manager.get_memory_context(
        hardware_id=hardware_id,
        user_input="Что у нас было в последних сообщениях?",
        apply_medium_gate=False,
    )
    short_ctx = str(context.get("short_term_context", ""))
    assert "CURRENT_TURN:" in short_ctx
    assert "PREVIOUS_TURN_1:" in short_ctx
    assert "софия как у тебя дела" in short_ctx.lower() or "софия" in short_ctx.lower()

    # На следующем запросе runtime memory должен прийти в text module и содержать рванный след.
    _ = await _run_request(
        service,
        {
            "text": "София и ещё про сообщение",
            "session_id": "sess-ragged-4",
            "hardware_id": hardware_id,
        },
    )

    last_runtime_memory = text_module.requests[-1]["runtime_memory_context"].lower()
    assert "short-term memory:" in last_runtime_memory
    assert "previous_turn_" in last_runtime_memory
    assert "отправь сообщение" in last_runtime_memory or "софия" in last_runtime_memory

    # Дополнительно проверяем, что DB short blob реально содержит short_current/short_previous.
    decoded = json.loads(factual_stack["db"].short)
    assert decoded.get("schema") == "memory_v2"
    assert decoded.get("short_current")
    assert isinstance(decoded.get("short_previous"), list)


@pytest.mark.asyncio
async def test_messages_followup_uses_saved_short_term_memory_for_generation(
    messaging_followup_stack,
):
    service = messaging_followup_stack["service"]
    manager = messaging_followup_stack["manager"]
    provider = messaging_followup_stack["provider"]

    hardware_id = "hw-msg-followup-1"

    first_items = await _run_request(
        service,
        {
            "text": "send a message to Sophia",
            "session_id": "sess-msg-1",
            "hardware_id": hardware_id,
        },
    )
    assert _count_audio_chunks(first_items) > 0

    saved_after_first = await manager.get_memory_context(
        hardware_id=hardware_id,
        user_input="follow-up check",
        apply_medium_gate=False,
    )
    first_short = str(saved_after_first.get("short_term_context", ""))
    assert "send a message to Sophia" in first_short
    assert "What message would you like to send to Sophia?" in first_short

    second_items = await _run_request(
        service,
        {
            "text": "how are you doing today",
            "session_id": "sess-msg-2",
            "hardware_id": hardware_id,
        },
    )
    assert _count_audio_chunks(second_items) > 0

    assert len(provider.classifier_calls) >= 2
    second_classifier_call = provider.classifier_calls[-1]
    assert second_classifier_call["user_input"] == "how are you doing today"
    assert "send a message to Sophia" in second_classifier_call["short_term_memory"]
    assert "What message would you like to send to Sophia?" in second_classifier_call["short_term_memory"]

    assert len(provider.process_calls) >= 2
    second_process_call = provider.process_calls[-1]
    assert second_process_call["route"] == "messages"
    assert "Short-term memory:" in second_process_call["runtime_memory_context"]
    assert "send a message to Sophia" in second_process_call["runtime_memory_context"]
    assert "What message would you like to send to Sophia?" in second_process_call["runtime_memory_context"]

    action_payloads = [
        item.get("command_payload")
        for item in second_items
        if isinstance(item.get("command_payload"), dict)
    ]
    assert action_payloads
    final_payload = action_payloads[-1].get("payload", {})
    assert final_payload.get("command") == "send_message"
    assert final_payload.get("args", {}).get("contact") == "Sophia"
    assert final_payload.get("args", {}).get("message") == "how are you doing today"
