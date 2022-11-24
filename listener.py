import json

import sounddevice
import vosk
import sys
import sounddevice as sd
import queue

model = vosk.Model('model_small')
samplerate = 16000
device = 1

q = queue.Queue()


def q_callback(indata, frames, time, status):
    """

    :param indata:
    :param frames:
    :param time:
    :param status:
    """
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def listen(callback):
    """

    :param callback:
    """
    with sd.RawInputStream(samplerate=samplerate,
                           blocksize=8000,
                           device=device,
                           dtype='int16',
                           channels=1,
                           callback=q_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
                callback(json.loads(rec.Result())["text"])
            # else:
            #     print(rec.PartialResult())


def listen_test(callback):

    with sd.RawInputStream(samplerate=samplerate,
                           blocksize=8000,
                           device=device,
                           dtype='int16',
                           channels=1,
                           callback=q_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
            # else:
            #     print(rec.PartialResult())


if __name__ == "__main__":
    print(sd.get_portaudio_version())
    listen_test()
