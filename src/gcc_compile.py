import subprocess

def gcc_compile(Cfile_PATH:str,executable_folder_name:str):
    Outfile_PATH = executable_folder_name + '/' + Cfile_PATH[Cfile_PATH.rfind('/')+1:-2]
    command = ['gcc','-Wall','-O2',Cfile_PATH,'-o',Outfile_PATH]
    try:
        result = subprocess.run(
            command,capture_output=True,text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return -1
    return Outfile_PATH
        
def debug_gcc_compile(Cfile_PATH:str,executable_folder_name:str):
    print('debug_gcc_compile')
    print(Cfile_PATH)
    print(Cfile_PATH.rfind('/'))
    Outfile_PATH = './' + executable_folder_name + '/' + Cfile_PATH[Cfile_PATH.rfind('/')+1:-2]
    print(Outfile_PATH)
    command = ['gcc','-Wall','-O2',Cfile_PATH,'-o',Outfile_PATH]
    try:
        result = subprocess.run(
            command,capture_output=True,text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return -1
    # result.stdout : 標準出力
    # result.stderr : エラー出力
    return 0