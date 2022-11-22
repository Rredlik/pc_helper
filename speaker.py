import pyttsx3

# from sound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 250)

volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)


def speak(audio):
    # current_volume = Sound.current_volume
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speak('Привет! Как твои дела, броо')
