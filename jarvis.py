import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import pygame

def hablar(texto):
    """Función para que el asistente hable con la voz de Google"""
    tts = gTTS(texto, lang='es')
    tts.save("voz.mp3")  # Asegúrate que el nombre coincida
    pygame.mixer.init()
    pygame.mixer.music.load("voz.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue  # Esperar hasta que termine de reproducirse

    pygame.mixer.quit()
    try:
        os.remove("voz.mp3")
    except FileNotFoundError:
        pass

def escuchar():
    """Función para escuchar y reconocer la voz"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language="es-ES")
            return comando.lower()
        except sr.UnknownValueError:
            return "No entendí el comando"
def abrir_calculadora():
    """Abre la calculadora en Windows"""
    hablar("Abriendo la calculadora")
    os.system("calc")

# Saludo inicial
hablar("Hola, soy tu asistente con la voz de Google. ¿En qué te puedo ayudar?")

# Loop principal
while True:
    comando = escuchar()
    print(f'Comando: {comando}')


    
    if "hora" in comando:
        hora_actual = datetime.now().strftime("%H:%M")
        hablar(f'La hora actual es {hora_actual}')

    elif "calculadora" in comando:
        abrir_calculadora()

    elif "cómo estás" in comando or "como estas" in comando:
        hablar("Estoy bien, gracias por preguntar. ¿Y tú?")

    elif "salir" in comando or "adiós" in comando:
        hablar("Hasta luego, que tengas un buen día")
     break   
else:
    hablar("Lo siento, aún no tengo esa función, pero puedo aprenderla.")
