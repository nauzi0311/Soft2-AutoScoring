import os,glob
from one_test_case_tester import one_test_case_tester as exec_test
from CONST import Const_Value as CONST

def tester(toml):
    for one_time in toml['configs']:
        source = one_time['source']
        src_file_list = file_fetcher(source,'c')
        
        test_case = one_time['test_case']
        test_file_list = file_fetcher(test_case,'in')
        
        input_type = input_type_checker(one_time['input_type'])
        
        output = one_time['output']
        if not os.path.isdir(output):
            print("Making " + output)
            os.mkdir(output)
        
        exe = one_time['exe']
        if not os.path.isdir(exe):
            print("Making " + exe)
            os.mkdir(exe)
        
        print(src_file_list)
        print("Execution test for " + source)
        for one_student in src_file_list:
            for one_test in test_file_list:
                print("Test " + one_test + " for " + one_student)
                exec_test(one_student,one_test,input_type,exe,output)

def file_fetcher(path:str,extension:str):
    file_list = []
    if not os.path.isdir(path):
        print(path + " is not existed")
        exit(1)
    else:
        print("Fetching file names in " + path)
        path = path + "/*." + extension
        file_list = glob.glob(path)
        file_list.sort()
        return file_list

def input_type_checker(input_type:str):
    ans = 0
    if input_type == 'args':
        ans = CONST.TYPE_ARGS
    elif input_type == 'stdin':
        ans = CONST.TYPE_STDIN
    else:
        print("Error input type:" + input_type)
        exit(1)
    return ans
