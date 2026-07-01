import ollama

def create_plan(intent):
    prompt = f'''
    You are a software planning assistant.Given a coding task, break it down 
    into clear, ordered, numbered steps.
    Rules : 
    - Each step must be specific and actionable 
    - Steps should be in logical order 
    - No code, just plain english steps 
    - Maximum 8 steps would be there 
    - Each step should be on a new line starting with a number 
    
    Task : {intent['task']}
    Language : {intent['language']}
    Features : {','.join(intent['features'])}
    
    Respond only with numbered steps and nothing else.
'''
    response = ollama.chat(
        model = "deepseek-coder:6.7b",
        messages= [{'role':'user','content':prompt}]
    )
    raw_plan = response['message']['content'].strip()
    steps = parse_steps(raw_plan)
    return steps


def parse_steps(raw_plan):
    lines = raw_plan.split('\n')
    steps = []
    for line in lines :
        line = line.strip()
        if line and line[0].isdigit():
            step = line.split('.',1)[-1].strip()
            if step :
                steps.append(step)
    return steps

