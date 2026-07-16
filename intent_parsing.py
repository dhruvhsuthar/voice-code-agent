import ollama
import json
import re

MODEL = "deepseek-coder:6.7b"

def extract_json(raw_output):

    raw_output = re.sub(r'```json|```', '', raw_output).strip()
    match = re.search(r'\{.*\}', raw_output, re.DOTALL)
    if match:
        return match.group()
    return raw_output

def understand_intent(text):
    prompt= f'''
    You are an intent parser for a coding assistant. Given a user's 
    spoken request, extract structured information.
    Respond ONLY with valid JSON in this exact format, no markdown, no code fences, nothing else: 
    {{
    "task" : "short description of what to build",
    "language" : "programming language",
    "features" : ["feature1","feature2"]
    }}
    User request : "{text}"
    '''
    response = ollama.chat(
        model = MODEL,
        messages = [{'role':'user','content':prompt}]
    )

    raw_output = response['message']['content'].strip()

    try :
        raw_output = extract_json(raw_output)
        intent = json.loads(raw_output)
        return intent
    except json.JSONDecodeError:
        print('could not parse json, raw output was : ')
        print(raw_output)
        return None

