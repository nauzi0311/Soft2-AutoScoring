import subprocess

def exec_with_args(executable_path:str,args:list):
    command = [executable_path] + args
    try:
        result = subprocess.run(
            command,capture_output=True,text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return -1
    return result.stdout

def debug_exec_with_args(executable_path:str,args:list):
    command = [executable_path] + args
    print('debug_exec_with_args')
    print(command)
    try:
        result = subprocess.run(
            command,capture_output=True,text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return -1
    print(result.stdout)
    print(result.stderr)
    return 0