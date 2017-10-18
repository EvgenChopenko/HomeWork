import sys

def run_on_linux(func):
    def wrapper(*args, **kwargs):
        if(sys.platform =='linux'):
            return func()
        else:
            return None
    return wrapper


def run_on_macos(func):
    def wrapper(*args, **kwargs):
        if (sys.platform == 'darwin'):
            return func()
        else:
            return None
    return wrapper

def run_on_windows(func):
    def wrapper(*args, **kwargs):
        if (sys.platform =='win32'):
            return func()
        else:
            return None
    return wrapper

if (__name__=='__main__'):
    @run_on_linux
    def func1():
        print('Функция выполняется только на Linux!')


    @run_on_macos
    def func2():
        print('Функция выполняется только на MACOS!')


    @run_on_windows
    def func3():
        print('Функция выполняется только на WINDOWS!')


    func1()
    func2()
    func3()
