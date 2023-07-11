from compile_and_exec import compile_and_exec as exec_module
from CONST import Const_Value as CONST

def main():
    args = ['Hello world']
    result = exec_module('./test2.c','exec',CONST.TYPE_ARGS,args_list=args)
    print(result)


if __name__ == '__main__':
    main()