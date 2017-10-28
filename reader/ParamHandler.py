from abc import ABCMeta, abstractmethod
import os
import pickle,json

class ParamHandlerException(Exception):
 pass


class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value
    def insert_param(self,value):
        self.params=value

    def get_all_params(self):
        return self.params

    def get_source(self):
        return str(self.source)

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):

         # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))

        return klass(source, *args, **kwargs)



# class XmlParamHandler(ParamHandler):
#
#     def read(self):
#
#         """
#         Чтение в формате XML и присвоение значений в self.params
#         """
#         data)
#     def write(self):
#         """
#         Запись в формате XML параметров self.params
#         """
#

class PickleParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
        with open(self.get_source(), 'rb') as f:
            self.insert_param(pickle.load(f))

    def write(self):
        with open(self.get_source(), 'wb') as f:
            pickle.dump(self.get_all_params(), f)

class JsonParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
     with open(self.get_source(), 'rb') as f:
      self.insert_param(json.load(f))
    def write(self):
     with open(self.get_source(), 'w') as f:
         json.dump(self.get_all_params(), f, indent=4)






ParamHandler.add_type('pickle',PickleParamHandler)
ParamHandler.add_type('json', JsonParamHandler)