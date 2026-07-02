from voice_recorder import record_audio
from voice_transcriber import transcribe_audio
from intent_parsing import understand_intent
from planner import create_plan
from codegen import code_generator
from code_executor import code_executor

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

    output_path = '/Users/dhruvsuthar/Documents/voice_assistant /firstproject.py'
    code_generator(intent,plan,output_path)

    result = code_executor(output_path)

    if result["success"]:
        print(f'Code ran successfully')
        if result["stdout"]:
            print(f'Output : {result["stdout"]}')
    else :
        print(f'Error detected')
        print(result['stderr'])
    return intent,plan


if __name__ == "__main__":
    listen()


