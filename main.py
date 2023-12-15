from gtts import gTTS
import playsound
import os

def text_prompt():
    while True:
        try:
            text = input("Digite o que deve ser dito: ").lower().strip()
            return text
        except:
            exit(" não entendi a fala")

def speak_text(text):
    tts = gTTS(text=text, lang = 'pt-BR')
    tts.save("fala.mp3")
    playsound.playsound("fala.mp3")
    os.remove("fala.mp3") 

while True:
    spoke_text = text_prompt()
    if spoke_text:
        print("Texto reconhecido:", spoke_text)
        speak_text(spoke_text)
    else:
        print("Não foi possível reconhecer a fala.")
        exit()