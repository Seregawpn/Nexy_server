#!/usr/bin/env python3
"""
GUI приложение для запроса разрешений на микрофон.
GUI приложения имеют больше прав для запроса разрешений в macOS.

Запуск: python3 tests/mic_permission_app.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import sys

def test_microphone():
    """Тест микрофона в отдельном потоке."""
    try:
        import pyaudio
        import numpy as np

        result_text.insert(tk.END, "Инициализация PyAudio...\n")
        p = pyaudio.PyAudio()

        # Устройство
        default_input = p.get_default_input_device_info()
        result_text.insert(tk.END, f"Устройство: {default_input['name']}\n")

        # Открываем поток - ЗДЕСЬ macOS должен показать запрос
        result_text.insert(tk.END, "\n🎤 Открываем микрофон...\n")
        result_text.insert(tk.END, "⚠️  macOS может показать запрос на разрешение - РАЗРЕШИТЕ!\n\n")
        window.update()

        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=int(default_input['defaultSampleRate']),
            input=True,
            input_device_index=default_input['index'],
            frames_per_buffer=1024
        )

        result_text.insert(tk.END, "✅ Поток открыт!\n\n")
        result_text.insert(tk.END, "Запись 3 секунды - ГОВОРИТЕ В МИКРОФОН!\n")
        result_text.insert(tk.END, "-" * 60 + "\n")
        window.update()

        # Запись
        frames = []
        for i in range(int(default_input['defaultSampleRate'] / 1024 * 3)):
            data = stream.read(1024, exception_on_overflow=False)
            frames.append(data)

            if i % 20 == 0:
                audio_data = np.frombuffer(data, dtype=np.int16)
                rms = np.sqrt(np.mean(audio_data.astype(np.float32)**2))
                result_text.insert(tk.END, f"[{i * 1024 / default_input['defaultSampleRate']:.1f}s] RMS: {rms:.3f}\n")
                window.update()

        # Анализ
        all_audio = np.frombuffer(b''.join(frames), dtype=np.int16)
        rms = np.sqrt(np.mean(all_audio.astype(np.float32)**2))
        max_val = np.max(np.abs(all_audio))
        nonzero = np.count_nonzero(all_audio)

        result_text.insert(tk.END, "\n" + "=" * 60 + "\n")
        result_text.insert(tk.END, "РЕЗУЛЬТАТЫ:\n")
        result_text.insert(tk.END, f"  RMS: {rms:.6f}\n")
        result_text.insert(tk.END, f"  Max: {max_val}\n")
        result_text.insert(tk.END, f"  Ненулевых: {nonzero}/{len(all_audio)}\n\n")

        if rms > 1:
            result_text.insert(tk.END, "✅ МИКРОФОН РАБОТАЕТ!\n", "success")
            messagebox.showinfo("Успех", "Микрофон работает!\n\nТеперь Homebrew Python тоже должен работать.")
        else:
            result_text.insert(tk.END, "❌ НЕТ СИГНАЛА\n", "error")
            messagebox.showwarning(
                "Нет сигнала",
                "Микрофон не записывает звук.\n\n"
                "Проверьте:\n"
                "1. System Preferences > Security & Privacy > Microphone\n"
                "2. System Preferences > Sound > Input (уровень входа)\n"
                "3. Микрофон не используется другим приложением"
            )

        stream.stop_stream()
        stream.close()
        p.terminate()

    except ImportError as e:
        result_text.insert(tk.END, f"❌ Ошибка импорта: {e}\n", "error")
        result_text.insert(tk.END, "\nУстановите зависимости:\n")
        result_text.insert(tk.END, "  pip3 install pyaudio numpy\n")
    except Exception as e:
        result_text.insert(tk.END, f"❌ Ошибка: {e}\n", "error")
        import traceback
        result_text.insert(tk.END, traceback.format_exc())

    finally:
        test_button.config(state=tk.NORMAL)

def start_test():
    """Запуск теста в отдельном потоке."""
    test_button.config(state=tk.DISABLED)
    result_text.delete(1.0, tk.END)

    # Запускаем в отдельном потоке, чтобы не блокировать GUI
    thread = threading.Thread(target=test_microphone)
    thread.daemon = True
    thread.start()

# Создаем GUI
window = tk.Tk()
window.title("Тест доступа к микрофону macOS")
window.geometry("700x500")

# Заголовок
title_label = ttk.Label(
    window,
    text="Тест разрешений на доступ к микрофону",
    font=("Helvetica", 16, "bold")
)
title_label.pack(pady=10)

# Инструкция
info_text = """
Это приложение поможет получить разрешение на доступ к микрофону.

GUI приложения имеют больше прав для запроса разрешений в macOS.

Когда вы нажмете "Тест микрофона", macOS может показать запрос
на разрешение - ОБЯЗАТЕЛЬНО РАЗРЕШИТЕ!

После успешного теста, обычный Python тоже сможет использовать микрофон.
"""

info_label = ttk.Label(window, text=info_text, justify=tk.LEFT)
info_label.pack(pady=10, padx=20)

# Кнопка теста
test_button = ttk.Button(
    window,
    text="🎤 Тест микрофона",
    command=start_test
)
test_button.pack(pady=10)

# Область результатов
result_frame = ttk.Frame(window)
result_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

result_text = tk.Text(result_frame, height=15, width=70, wrap=tk.WORD)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

# Стили для текста
result_text.tag_config("success", foreground="green", font=("Helvetica", 12, "bold"))
result_text.tag_config("error", foreground="red", font=("Helvetica", 12, "bold"))

# Информация о Python
python_info = f"Python: {sys.executable}"
info_bottom = ttk.Label(window, text=python_info, font=("Courier", 9))
info_bottom.pack(pady=5)

# Запуск
window.mainloop()
