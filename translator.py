from tkinter import *
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os

# 🧠 Initialize Pygame for audio
pygame.mixer.init()

# 🎨 Main GUI Setup
window = Tk()
window.title("🌍 Linguista - Visual Language Translator")
window.geometry("650x500")
window.config(bg="#fff9f2")

# 🖌️ Title
Label(window, text="🌍 Linguista", font=("Helvetica", 28, "bold"), bg="#fff9f2", fg="#6a0572").pack(pady=10)
Label(window, text="Type your thoughts and choose your language", font=("Helvetica", 12), bg="#fff9f2", fg="#444").pack()

# ✍️ Input Box
input_text = Text(window, height=5, width=60, font=("Helvetica", 12), wrap=WORD, bd=2, relief=GROOVE)
input_text.pack(pady=10)

# 🌐 Language Dropdown
Label(window, text="Translate to:", font=("Helvetica", 12), bg="#fff9f2").pack()
languages = ["english", "spanish", "french", "german", "turkish", "arabic", "urdu", "hindi", "japanese", "korean", "chinese"]
lang_var = StringVar(window)
lang_var.set("spanish")
OptionMenu(window, lang_var, *languages).pack(pady=5)

# 🖼️ Output
output_label = Label(window, text="", font=("Helvetica", 14), bg="#fff9f2", fg="#333", wraplength=500, justify="center")
output_label.pack(pady=20)

# 🔊 Speak Function
def speak_output(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("voice.mp3")
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print("Audio error:", e)

# 🧠 Translate Button Function
def translate_text():
    src = input_text.get("1.0", END).strip()
    if not src:
        output_label.config(text="Please enter some text first!")
        return

    target_lang = lang_var.get()

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(src)
        output_label.config(text=f"🔁 Translation:\n{translated}")
        speak_output(translated, target_lang[:2])  # only first 2 letters of lang
    except Exception as e:
        output_label.config(text=f"Translation Error: {str(e)}")

# 🔘 Translate Button
Button(window, text="✨ Translate", command=translate_text, font=("Helvetica", 12), bg="#6a0572", fg="white", padx=10, pady=5).pack()

# 👣 Footer
Label(window, text="Made with 💜 by your digital bestie", font=("Helvetica", 10), bg="#fff9f2").pack(side="bottom", pady=10)

# 🚀 Run it!
window.mainloop()
