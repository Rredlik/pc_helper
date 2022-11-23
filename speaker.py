import time

import pyttsx3
import torch
import sounddevice as sd

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000  # 8000, 24000, 48000
speaker = 'baya'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # or gpu
# from sound


model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)


# print(text)
# audio = model.apply_tts(text=text,
#                         speaker=speaker,
#                         sample_rate=sample_rate,
#                         put_accent=put_accent,
#                         put_yo=put_yo)
# sd.play(audio, sample_rate)
# time.sleep(len(audio) / sample_rate*1.01)
# print(sample_rate)
# sd.stop()

def speak(text):
    _audio = model.apply_tts(text=text,
                             speaker=speaker,
                             sample_rate=sample_rate,
                             put_accent=put_accent,
                             put_yo=put_yo)
    sd.play(_audio, sample_rate)
    time.sleep(len(_audio) / sample_rate)
    sd.stop()


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# # print(voices)
# engine.setProperty('voices', voices[0].id)
# engine.setProperty('rate', 250)
#
# volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)

# def speak(audio):
#     # current_volume = Sound.current_volume
#     engine.say(audio)
#     engine.runAndWait()

# if __name__ == '__main__':
#     # speak('Привет! Как твои дела, броо')
#     robo_speak("Абоба")
