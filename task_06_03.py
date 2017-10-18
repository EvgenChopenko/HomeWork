
from collections import namedtuple


def return_namedtuple(*args):

    def decarator(func):
        Nturple = namedtuple('Nturple',[*args])
        def wrapper(*argsdunc,**kwargsfunc):
            s=func(*argsdunc,**kwargsfunc)
            if(isinstance(s,tuple)):
                try:
                    p=Nturple(*s)
                except:
                    return s
                return (p)
            else:
                 return s
        return wrapper
    return decarator










if(__name__=='__main__'):
    @return_namedtuple('one', 'two')
    def func1():
        return 1, 2


    @return_namedtuple('one', 'two', 'three')
    def func2():
        return 1, 2, 3,4

    print(func1())
    print(func2())


    @return_namedtuple('one')
    def func3():
        return 1


    print(func3())

