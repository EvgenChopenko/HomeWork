import time

def pause(second):
    def decorator(func):
        def wraper(*args, **kwargs):
            time.sleep(second)
            return func(*args, **kwargs)
        return wraper
    return decorator


if(__name__=='__main__'):
    @pause(7)#6999 ms
    def func():
        print("функция с содержкой ")
    func()