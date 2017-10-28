from abc import ABCMeta, abstractmethod
import re

from datetime import datetime


class ValidExseps(Exception):
    pass

class Validator(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def validate(self,value):
        pass
    """
    validate(value) => true or false
    
    """

    type_val={}
    @classmethod
    def add_validat(cls,name,klass):
        if issubclass(klass,Validator):
            cls.type_val[name]=klass
        else:
            raise ValidExseps ('Class {} is not Validator!'.format(klass))

    @classmethod
    def get_instance(cls,name,*args,**kwargs):
        s=cls.type_val.get(name)
        if s is not None:
            return s(*args,**kwargs)
        else:
            raise ValidExseps ( 'Validator with name "{}" not found'.format(name))



class EMailValidator(Validator):
    def __init__(self):
        super().__init__()

    def validate(self, value):
        a = str.maketrans('', '',
                          'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁйцукенгшщзхъфывапролджэячсмитьбюё~=)(^%$#!:;\\\/\+\*\?\^')

        if value!=value.translate(a):
            return False


        try:
            parse=re.search("\w+@\w+.\w+", value)
            parse.group()
        # except AttributeError :
        #     return False
            return True
        except AttributeError:
            return False
        except:
            return False


class DateTimeValidator(Validator):
    def __init__(self):
        super().__init__()

    def validate(self,value):
        data = None
        try: data = datetime.strptime(value, "%Y-%m-%d")
        except:pass
        try:data = datetime.strptime(value, "%Y-%m-%d %H:%M")
        except:pass
        try:data = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except:pass
        try:data = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except:pass
        try:data = datetime.strptime(value, "%d.%m.%Y")
        except:pass
        try:data = datetime.strptime(value, "%d.%m.%Y %H:%M")
        except:pass
        try:data = datetime.strptime(value, "%d.%m.%Y %H:%M:%S")
        except:pass
        try:data = datetime.strptime(value, "%d/%m/%Y")
        except:pass
        try: data = datetime.strptime(value, "%d/%m/%Y %H:%M")
        except:pass
        try: data = datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
        except:pass



        if data:
            return True

        return False



Validator.add_validat('email',EMailValidator)
Validator.add_validat('datetime',DateTimeValidator)
