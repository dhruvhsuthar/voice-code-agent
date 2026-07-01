from voice_recorder import record_audio
from voice_transcriber import transcribe_audio
from intent_parsing import understand_intent
from planner import create_plan

def listen():
    audio_file = record_audio(duration = 7)
    text = transcribe_audio(audio_file)
    print(f'Done. You said {text}')

    intent = understand_intent(text)
    print(f'Understood intent : {intent}')

    plan = create_plan(intent)
    print(f'Plan :')
    for i,step in enumerate(plan,1):
        print(f'Step {i}. {step}')

    return intent,plan

if __name__ == "__main__":
    listen()


