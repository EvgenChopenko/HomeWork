import os


def strict_argument_types(func):
    from inspect import signature
    sig = signature(func)
    def wrapper(*args,**kwargs)->sig.return_annotation:
        #sig = signature(func)
        #print(sig.return_annotation)
        s1=([(i) for i in args])
        s1=s1+[i for i in kwargs.values()] # kwargs видет как строки ((# любой kwargs  это ошибка
        s2=([sig.parameters[i].annotation for i in sig.parameters])
        #print(s1,len(s1),len(s2),s2)
        if len(s1) == len(s2):
            for i in range(len(s1)):
                if not isinstance(s1[i], s2[i]):
                    raise TypeError ('The argument "{}" must be "{}", passed "{}"'.format(s1[i],s2[i],type(s1[i])))
        else:
            raise ValueError ("the count argumen more ")
        return func(*args,**kwargs)
    return wrapper

def strict_return_type(func):
    from inspect import signature
    from collections import Iterable
    sig = signature(func)
    def wrapper (*args,**kwargs)->sig.return_annotation:
        print(sig.return_annotation)
        s2=sig.return_annotation
        s1=func(*args,**kwargs)
        if isinstance(s2,Iterable) and isinstance(s1,Iterable):
            s2 = [i for i in sig.return_annotation]
            s1 = tuple(func(*args,**kwargs))
            print(s2,s1)
            if len(s1) == len(s2):
                for i in range(len(s1)):
                    if not isinstance(s1[i], s2[i]):
                        raise TypeError ('The return value must be "{}", not "{}"'.format(s2[i],type(s1[i])))
            else:
                raise ValueError ("the count argumen more ")
        elif not isinstance(s2,Iterable) and not isinstance(s1,Iterable):
            if not isinstance(s1,s2):
                raise TypeError('The return value must be "{}", not "{}"'.format(sig.return_annotation, type(func(*args))))
        return func(*args,**kwargs)

    return wrapper

@strict_return_type
@strict_argument_types
def summa(a:int, b:int) -> int:
    return a + b

print(summa(10,b=10))

@strict_return_type
@strict_argument_types
def splitext(path:str) -> (str, str):
    filename, ext = os.path.splitext(path)
    return filename, ext.strip('.').lower()

print(splitext("https:/www.google.ru"))