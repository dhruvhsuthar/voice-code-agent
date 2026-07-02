import ollama
import re
import os

def code_generator(intent,steps,output_path):
    formatted_steps = "\n".join([f'{i+1}.{steps}' for i,steps in enumerate(steps)])

    prompt = f'''
    You are a professional software engineer with more than 2 decades of experience.
    expert in writing clean python code 
    
    Given the following plan, provide a complete,working code file.
    
    Task : {intent['task']}
    Language : {intent['language']}
    Features : {','.join(intent['features'])}
    
    Steps to be followed : 
    {formatted_steps}
    
    Rules : 
    - Return ONLY raw Python code
    - The very first character of your response must be either 'import', 'from', 'def', or '#'
    - No explanations, no descriptions, no markdown fences
    - No sentences in English anywhere in the output
    - If you write anything other than Python code, you have failed
    - return only complete code file, nothing else 
    - no markdown fencies, no explanation and no commentary 
    - the code must be complete and runnable in a single file 
    - follow the plan steps in order 
'''

    response = ollama.chat(
        model = "deepseek-coder:6.7b",
        messages = [{'role':'user','content':prompt}]
    )

    code = response['message']['content'].strip()

    code = re.sub(r'```python|```','',code).strip()

    os.makedirs(os.path.dirname(output_path),exist_ok=True)

    with open(output_path,'w') as f :
        f.write(code)

    print(f'code saved to {output_path}')
    return output_path

