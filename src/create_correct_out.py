from CONST import Const_Value as CONST
import gcc_compile as gc
from exec_with_args import exec_with_args as exe_arg
from exec_with_stdin import exec_with_stdin as exe_std
import os

def create_correct_out(
        CORRECT_Cfile_PATH:str,
        CORRECT_EXE_PATH:str,
        out_folder_path:str,
        type:CONST,
        args_list:list = None,
        stdin_text : str = None
    ):
    if not os.path.exists(CORRECT_EXE_PATH):
        os.mkdir(CORRECT_EXE_PATH)
    Out_PATH = gc.gcc_compile(CORRECT_Cfile_PATH,CORRECT_EXE_PATH)
    result = None
    if type == CONST.TYPE_ARGS:
        result = exe_arg(Out_PATH,args_list)
    elif type == CONST.TYPE_STDIN:
        result = exe_std(Out_PATH,stdin_text)
    else:
        print("No type input")
        return -1
    with open(out_folder_path,'w') as f:
        f.write(result)
    return 0