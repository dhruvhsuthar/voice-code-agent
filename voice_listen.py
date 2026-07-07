from voice_recorder import record_audio
from voice_transcriber import transcribe_audio

def listen():
    audio_file = record_audio(duration = 7)
    text = transcribe_audio(audio_file)
    print(f'Done. You said : {text}')
    return text

if __name__ == "__main__":
    listen()


