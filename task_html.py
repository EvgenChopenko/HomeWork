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
       #return self.__firstChild
    @property
    def last_child(self):
        raise TagException('Not a container tag!')
      #  return self.__lastChild
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
            super().__setattr__(key, value)
        except :
            self.__attributes[key] = value

    def __delattr__(self, item):
        try:
           super().__delattr__(item)
        except AttributeError:
            del self.__attributes[item]
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,data):
        self.__name=data


    # def __str__(self):
    #     s = ''.join([' ' + k + '="' + v + '"'
    #                  for k, v in self.__attributes.items() if k and v])
    #     return '<{}{}>'.format(self.__name, s)


class ContainerTag(Tag):
    __slots__ = ('__count')
    def __init__(self,name,**kwrgs):
        super().__init__(name,**kwrgs)



    def append_child(self,tag):
       # tag.parent=self
       if (self.__firstChild is None):
           self.firstChild=tag
       if (self.last_child is not None):
           tag.previousSibling = self.last_child
           (self.last_child).nextSibling=tag

       self.last_child=tag
       tag.nextSibling
       tag.parent=self





    def insert_before(tag, next_sibling):
        pass#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111111
    @property
    def firstChild(self):
       return self.__firstChild

    @firstChild.setter
    def firstChild(self,data):
        self.__firstChild =data

    @firstChild.deleter
    def firstChild(self):
        del self.__firstChild
    @property
    def last_child(self):
        return self.__lastChild
    @last_child.setter
    def last_child(self,data):
        self.__lastChild=data

    @last_child.deleter
    def last_child(self,data):
        del self.__lastChild

    @property#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    def children(self):
        raise TagException('Not a container tag!')




if __name__ == '__main__':
    img = Tag('img')
    img.src = '/logo.png'
    # img.parent='asda'
    img.alt = 'Логотип'
    h = Tag('h')
    h.src = '/logo.png'
    # img.parent='asda'
    h.alt = 'Логотип'
    div = ContainerTag('div')
    div.append_child(img)
    div.append_child(h)
    print(img.parent,"img parenst")
    print(img.nextSibling,"img следуюший")
    print(img.previousSibling,"img преведуший")
    print(h.parent,"h.parent")
    print(h.nextSibling,"h cследуюший")
    print(h.previousSibling, "h преведуший")
    print(div.last_child,"div последний")
    print(div.firstChild,"div первый")



