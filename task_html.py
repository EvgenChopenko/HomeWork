class TagException(Exception):
    pass

class Tag(object):
    __slots__ = ('__name', '__attributes', '__parent',
                 '__previousSibling', '__nextSibling','__firstChild','__lastChild','__children')
    def __init__(self,name,**kwargs):
        self.__parent = None
        self.__previousSibling = None
        self.__nextSibling=None
        self.__firstChild=None
        self.__lastChild=None
        self.__children=None
        self.__attributes = kwargs
        if isinstance(name,str):
            self.__name = name
        else:
            raise TagException('name not str')

    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self,value):
        self.__parent=value
    @parent.deleter
    def parent(self):
        del self.__parent

    @property
    def previousSibling(self):
        return self.__previousSibling
    @previousSibling.setter
    def previousSibling(self,value):
        self.__previousSibling=value
    @previousSibling.deleter
    def previousSibling(self):
        del self.__previousSibling

    @property
    def nextSibling(self):
        return self.__nextSibling

    @nextSibling.setter
    def nextSibling(self,value):
        self.__nextSibling = value

    @nextSibling.deleter
    def nextSibling(self):
        del self.__nextSibling

    @property
    def firstChild(self):
        raise TagException ('Not a container tag!')


    @property
    def last_child(self):
        raise TagException('Not a container tag!')

    @property
    def children(self):
        raise TagException('Not a container tag!')



    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
                return self.__attributes.get(attr)

    def __setattr__(self, key, value):
        try:
            return super().__setattr__(key, value)
        except :
            self.__attributes[key] = value

    def __delattr__(self, item):
        try:
            return super().__delattr__(item)
        except AttributeError:
            del self.__attributes[item]

    def __str__(self):
        s = ''.join([' ' + k + '="' + v + '"'
                     for k, v in self.__attributes.items() if k and v])
        return '<{}{}>'.format(self.__name, s)

if __name__ == '__main__':
    img = Tag('img')
    img.src = '/logo.png'
    img.parent='asda'
    img.alt = 'Логотип'
    print(img)

