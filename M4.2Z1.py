# 4.2 Argumenty funkcji
'''
def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")
'''
def count_them_all(*,a,b):
    a=0
    b=0
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")

count_them_all(1, 2, 3, "A", a=1, b=2)