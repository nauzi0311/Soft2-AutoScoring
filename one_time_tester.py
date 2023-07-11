
from compile_and_exec import compile_and_exec as tester
from CONST import Const_Value as CONST

def one_user_tester(Cfile_path,type:CONST,exec_folder_name:str,output_dir:str,args=None,input_txt=None):
    result = tester(Cfile_path,exec_folder_name,type,args,input_txt)
    
    