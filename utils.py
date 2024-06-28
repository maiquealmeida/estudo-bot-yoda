import datetime
import os
import time
import pygame
from elevenlabs import Voice, VoiceSettings, play, save
from elevenlabs.client import ElevenLabs
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY=os.environ['ELEVENLABS_API_KEY']
ELEVENLABS_VOICE_ID=os.environ['ELEVENLABS_VOICE_ID']

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY
)

def inner_thoughts_remove(frase: str, inicio: str, fim: str) -> str:
    while inicio in frase and fim in frase:
        start_index = frase.find(inicio)
        end_index = frase.find(fim, start_index) + len(fim)
        if start_index == -1 or end_index == -1:
            break
        frase = frase[:start_index] + frase[end_index:]
    return frase

def inner_thoughts_extractor(frase: str, inicio: str, fim: str) -> list[str]:
    resultados = []
    while inicio in frase and fim in frase:
        start_index = frase.find(inicio) + len(inicio)
        end_index = frase.find(fim, start_index)
        if start_index == -1 or end_index == -1:
            break
        resultados.append(frase[start_index:end_index])
        frase = frase[end_index + len(fim):]
    
    return ' '.join(resultados)


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def say(message, filename=None):
    yoda_voice=Voice(
        voice_id=ELEVENLABS_VOICE_ID,
        settings=VoiceSettings(
            stability=0.52,
            similarity_boost=1,
            use_speaker_boost=True
        )
    )

    audio=client.generate(
        text=message,
        voice=yoda_voice,
        model='eleven_multilingual_v2'
    )

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"output_{timestamp}.mp3"
    save(audio, filename)
    play_audio(filename)