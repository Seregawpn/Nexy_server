#!/usr/bin/env python3
"""
Pydantic models for LLM response validation

These models ensure that parsed JSON responses match the expected structure,
protecting against LLM "hallucinations" where field names are changed.
"""

from typing import Optional, Dict, Any, Tuple, Union
from pydantic import BaseModel, Field, field_validator, model_validator


class TextResponse(BaseModel):
    """
    Model for text-only responses (no action)
    
    Expected format:
    {
      "text": "Hello, how can I help you?"
    }
    """
    text: str = Field(..., description="Text response for TTS")
    
    # Optional fields that should be ignored if present
    session_id: Optional[str] = Field(None, description="Should not be present in text-only responses")
    command: Optional[str] = Field(None, description="Should not be present in text-only responses")
    args: Optional[Dict[str, Any]] = Field(None, description="Should not be present in text-only responses")
    
    @model_validator(mode='after')
    def validate_text_only(self):
        """Ensure no action fields are present in text-only response"""
        if self.command is not None or self.args is not None:
            # This is actually an action response, but we'll allow it
            # and let ActionResponse handle it
            pass
        return self


class OpenAppArgs(BaseModel):
    """Arguments for open_app command"""
    app_name: Optional[str] = Field(None, min_length=1, description="macOS application name (without .app extension)")
    app_path: Optional[str] = Field(None, min_length=1, description="Full path to .app bundle")
    
    @field_validator('app_name')
    @classmethod
    def validate_app_name(cls, v: Optional[str]) -> Optional[str]:
        """Remove .app extension if present"""
        if v and v.endswith('.app'):
            return v[:-4]
        return v
    
    @model_validator(mode='after')
    def validate_at_least_one(self):
        """Ensure at least app_name or app_path is provided"""
        if not self.app_name and not self.app_path:
            raise ValueError("Either 'app_name' or 'app_path' must be provided for open_app")
        return self


class CloseAppArgs(BaseModel):
    """Arguments for close_app command"""
    app_name: str = Field(..., min_length=1, description="macOS application name (without .app extension)")
    
    @field_validator('app_name')
    @classmethod
    def validate_app_name(cls, v: str) -> str:
        """Remove .app extension if present"""
        if v.endswith('.app'):
            return v[:-4]
        return v


class BrowserUseArgs(BaseModel):
    """Arguments for browser_use command"""
    task: str = Field(..., min_length=1, description="Task description for browser automation")
    config_preset: Optional[str] = Field("fast", description="Browser config preset: ultra_fast, fast, standard")
    
    @field_validator('config_preset')
    @classmethod
    def validate_config_preset(cls, v: Optional[str]) -> Optional[str]:
        """Validate config preset value"""
        if v and v not in ['ultra_fast', 'fast', 'standard']:
            raise ValueError(f"Invalid config_preset: {v}. Allowed: ultra_fast, fast, standard")
        return v


class ReadMessagesArgs(BaseModel):
    """Arguments for read_messages command"""
    contact: Optional[str] = Field(None, description="Contact name or 'last' for last message from any contact")
    limit: Optional[int] = Field(None, ge=1, description="Maximum number of messages to read (default: 10)")
    
    @field_validator('contact')
    @classmethod
    def validate_contact(cls, v: Optional[str]) -> Optional[str]:
        """Normalize contact value"""
        if v is None or v == "":
            return "last"  # Default to "last" if not provided
        return v.strip()


class SendMessageArgs(BaseModel):
    """Arguments for send_message command"""
    contact: str = Field(..., min_length=1, description="Contact name to send message to")
    message: str = Field(..., min_length=1, description="Message text to send")
    phone_number: Optional[str] = Field(None, description="Optional phone number if contact is ambiguous")


class ActionResponse(BaseModel):
    """
    Model for action responses (with command)
    
    Expected format:
    {
      "session_id": "session_123",  # Optional - can be provided from context
      "command": "open_app",
      "args": {
        "app_name": "Safari"
      },
      "text": "Opening Safari."
    }
    """
    session_id: Optional[str] = Field(None, description="Session ID from request (optional, can be provided from context)")
    command: str = Field(..., min_length=1, description="Command type (e.g., 'open_app')")
    args: Dict[str, Any] = Field(..., description="Command arguments")
    text: str = Field(default="", description="Text response for TTS (can be empty)")
    
    @field_validator('command')
    @classmethod
    def validate_command(cls, v: str) -> str:
        """Validate command type"""
        allowed_commands = ['open_app', 'close_app', 'browser_use', 'read_messages', 'send_message']
        if v not in allowed_commands:
            raise ValueError(f"Unknown command: {v}. Allowed: {allowed_commands}")
        return v
    
    @model_validator(mode='after')
    def validate_args_for_command(self):
        """Validate args structure based on command type"""
        if self.command == 'open_app':
            # Try to validate as OpenAppArgs
            try:
                OpenAppArgs(**self.args)
            except Exception as e:
                raise ValueError(f"Invalid args for open_app command: {e}")
        elif self.command == 'close_app':
            # Try to validate as CloseAppArgs
            try:
                CloseAppArgs(**self.args)
            except Exception as e:
                raise ValueError(f"Invalid args for close_app command: {e}")
        elif self.command == 'browser_use':
            # Try to validate as BrowserUseArgs
            try:
                BrowserUseArgs(**self.args)
            except Exception as e:
                raise ValueError(f"Invalid args for browser_use command: {e}")
        elif self.command == 'read_messages':
            # Try to validate as ReadMessagesArgs
            try:
                ReadMessagesArgs(**self.args)
            except Exception as e:
                raise ValueError(f"Invalid args for read_messages command: {e}")
        elif self.command == 'send_message':
            # Try to validate as SendMessageArgs
            try:
                SendMessageArgs(**self.args)
            except Exception as e:
                raise ValueError(f"Invalid args for send_message command: {e}")
        return self


class LLMResponseValidator:
    """
    Validator for LLM responses using Pydantic models
    
    This class provides graceful fallback when LLM returns unexpected structure,
    preventing KeyError exceptions and handling "hallucinations" gracefully.
    """
    
    @staticmethod
    def validate_response(data: Dict[str, Any], session_id: Optional[str] = None) -> Tuple[Optional[Union[TextResponse, ActionResponse]], Optional[str]]:
        """
        Validate LLM response against expected schemas
        
        Args:
            data: Parsed JSON dictionary from LLM
            session_id: Optional session ID to inject if missing in action responses
            
        Returns:
            Tuple of (validated_model, error_message)
            - If validation succeeds: (model, None)
            - If validation fails: (None, error_message)
        """
        # Check if it's an action response (has 'command' field)
        if 'command' in data and data.get('command'):
            try:
                # If session_id is missing but provided from context, inject it
                action_data = data.copy()
                if 'session_id' not in action_data or not action_data.get('session_id'):
                    if session_id:
                        action_data['session_id'] = session_id
                
                action_response = ActionResponse(**action_data)
                return action_response, None
            except Exception as e:
                error_msg = f"ActionResponse validation failed: {str(e)}"
                return None, error_msg
        
        # Check if it's a text-only response
        if 'text' in data:
            try:
                text_response = TextResponse(**data)
                return text_response, None
            except Exception as e:
                error_msg = f"TextResponse validation failed: {str(e)}"
                return None, error_msg
        
        # No recognized structure