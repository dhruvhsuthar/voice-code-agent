import subprocess
import os

def code_executor(file_path):
    if not os.path.exists(file_path):
        return {"success": False, "stdout":"","stderr":"file not found"}

    try :
        results = subprocess.run(
            ['python',file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
    except subprocess.TimeoutExpired as e :
        if e.stderr :
            return {"success":False,"stdout":"","stderr":e.stderr}
        else :
            return {"success":True,"stdout":"program ran successfully with GUI","stderr":""}
    if results.returncode == 0 :
        return {"success":True,"stdout":results.stdout,"stderr":""}
    else :
        return {"success":False,"stdout":"","stderr":results.stderr}
