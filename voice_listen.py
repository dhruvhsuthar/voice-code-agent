from voice_recorder import record_audio
from voice_transcriber import transcribe_audio
from intent_parsing import understand_intent

def listen():
    audio_file = record_audio(duration = 7)
    text = transcribe_audio(audio_file)
    print(f'Done. You said {text}')

    intent = understand_intent(text)
    print(f'Understood intent : {intent}')
    return intent

if __name__ == "__main__":
    listen()


