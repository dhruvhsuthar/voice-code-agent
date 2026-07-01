import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="temp_audio.wav",duration = 5, samplerate = 16000):
    print("recording now.....speak now")
    audio = sd.rec(int(duration * samplerate),samplerate = samplerate, channels=1, dtype = 'int16')
    sd.wait()
    write(filename,samplerate, audio)
    print("recording finished")
    return filename


