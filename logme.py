import sys
from functools import reduce
from datetime import datetime


class entry(object):
    
    def __init__(self, log_str):
        pass

    def __repr__(self):
        pass

def start(args):
    "写入'me.log'."
    
    # 需要处理参数的简单方法
    try:
        assert len(args) in range(1, 3)
    except AssertionError:
        print('usage: melog start <subject> [<comment>]')
    
    subject = args[0]
    comment = '--'
    if len(args) == 2:
        comment = args[1]

    time = datetime.now().isoformat()
    entry = time + ' ' + subject + ' ' + comment + '\n'

    # 写入记录
    with open('me.log', 'a') as f:
        f.write(entry)


def today(args):
    with open('me.log', 'a') as f:
        info = f.read()
        print(info)
    

def helpme(args):
    ""
    print('usage: logme start/today')


functions = [start, today, helpme]

def main():
    args = sys.argv[1:]

    # 没有参数，视为查看 today（TODO：改成 now）
    if len(args) == 0:
        args.append(today)

    # 匹配第一个参数跳转到不同的命令
    function_name = args.pop(0)
    function = next((f for f in functions if f.__name__ == function_name), helpme)
    # for f in functions:
    #     print(f.__name__)
    # print(function, function_name)
    function(args)

     




# print(desc)


if __name__ == '__main__':
    main()

