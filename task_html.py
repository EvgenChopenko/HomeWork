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
        self.__attributes =kwargs
        if isinstance(name,str):
            self.__name = name
        else:
            raise TagException('name not str')
######################################################
    @property
    def parent(self):
        if self.__parent is not None:
            return self.__parent
        else:
            raise TagException('Parents None')
    @parent.setter
    def parent(self,value):
        if isinstance(value,ContainerTag):
            self.__parent=value
        else:
            raise TagException("parents not ContainerTag")
    @parent.deleter
    def parent(self):
        if self.__parent is not None:
            del self.__parent
        else:
            raise TagException("Parents None now")

#______________________________________________________________
#___________________________________________________________
    @property
    def previousSibling(self):
  #      if self.__previousSibling is not None:
            return self.__previousSibling
 #       else:
#            raise TagException("previousSibling None")
    @previousSibling.setter
    def previousSibling(self,value):
        if isinstance(value,Tag) or isinstance(value,ContainerTag):
            self.__previousSibling=value
        else:
            raise TagException("valui is not Tag or Connection Tag")
    @previousSibling.deleter
    def previousSibling(self):
        if self.__previousSibling is not None:
            del self.__previousSibling
        else:
            raise TagException("this __previousSibling None now")
#____________________________________________________________
    @property
    def nextSibling(self):
        if self.__nextSibling is not None:
            return self.__nextSibling
        else:
            raise TagException("__nextSibling is None")
    @nextSibling.setter
    def nextSibling(self,value):
        if isinstance(value, Tag) or isinstance(value, ContainerTag):
            self.__nextSibling = value
        else:
            raise TagException("value is not Tag or ContainerTag")
    @nextSibling.deleter
    def nextSibling(self):
        if self.__nextSibling is not None:
            del self.__nextSibling
        else:
            raise TagException("this __nextSibling is none now")
#____________________________________________________________________
    @property
    def firstChild(self):
        raise TagException ('Not a container tag!')

    @property
    def last_child(self):
        raise TagException('Not a container tag!')

    @property
    def children(self):
        raise TagException('Not a container tag!')

#____________________________________________________________________________

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
#____________________________________________________________________
    @property
    def name(self):
        if self.__name is not None:
            return self.__name
        else:
            raise TagException ("name is None")
    @name.setter
    def name(self,data):
        if isinstance(data,str):
            self.__name=data
        else:
            raise TagException("name is not string")
#____________________________________________________________________________________

    def atr(self):# метод возврошает атрибуты очень важный метод !!!!
        return self.__attributes

    def __iter__(self):
        return self
    ### Безполезные методы нужны что бы избежать ошибок итераци в итерации
    def __next__(self):
        raise StopIteration

    def __str__(self):
        s=""
        if not isinstance(self.__attributes.values(),Tag) :
                s = ''.join([' ' + k + '="' + v + '"' for k, v in self.__attributes.items() if isinstance( v,str)])
                return '<{}{}>'.format(self.__name, s)

        else:
            return ""

    def ToStr(self):# проверочный метод возр строку .
        return str(self)

#########################################################################################3
##########################################################################################
###########################################################################################


class ContainerTag(Tag):
    __slots__ = ('count','__itert',)# count нужен был для проверки _iters хранит сылку последнего элемента в итерации
    def __init__(self,name,**kwargs):
        super().__init__(name,**kwargs)
        self.__itert=None
        self.count=0



############################################################################
    def append_child(self,tag):
       # tag.parent=self
       if (self.__firstChild is None):
           self.firstChild=tag
       if (self.__lastChild is not None):
           tag.previousSibling = self.last_child
           (self.last_child).nextSibling=tag

       self.last_child=tag
       #tag.nextSibling
       tag.parent=self
#########################################################################




    def insert_before(self,tag, next_sibling):
        #tag.parent = self
        if next_sibling is None:
            self.append_child(tag)
            return 0
        if next_sibling.parents == self:
            raise TagException ("Error tag not parents")
        if next_sibling == self.firstChild:
            self.firstChild=tag

            tag.previousSibling = next_sibling.previousSibling
            tag.nextSibling = next_sibling
            next_sibling.previousSibling=tag
            tag.parent = self
            return 0
        if next_sibling != self.firstChild:
           for i in self:
               if i.nextSibling == next_sibling:
                   tag.previousSibling = next_sibling.previousSibling
                   tag.nextSibling = next_sibling
                   next_sibling.previousSibling = tag
                   tag.parent = self
                   return 0
        return 1
    @property
    def firstChild(self):
       return self.__firstChild

    @firstChild.setter
    def firstChild(self,data):
        self.__itert=data
        self.__firstChild =data

    @firstChild.deleter
    def firstChild(self):
        del self.__firstChild
    @property
    def last_child(self):
        return self.__lastChild
    @last_child.setter
    def last_child(self,data):
        # print(self.count)
        self.__lastChild=data

    @last_child.deleter
    def last_child(self,data):
        del self.__lastChild

    def __iter__(self):
        return self
    def __next__(self):
        if self.count == 0 and self.__itert is not None:
            self.count = 1
            return self.__itert
        elif self.__itert !=self.__lastChild and self.__count!=0:
            self.__itert=(self.__itert).nextSibling
            self.count +=1
            return self.__itert
        else:
            raise StopIteration



    @property
    def children(self):
        for i in self:
            yield i

    @children.setter
    def  children(self,data):
        raise TagException('Not setter children!')

    def __str__(self):
        result = ""
        result = '<' + self.name
        result += ''.join([' ' + k + '="' + v + '"' for k, v in self.atr().items()if isinstance(v,str)])
        result += ">\n"
        for i in self.children:
             result+= str(i)+"\n"
        result += '</' + self.name + '>\n'
        return result

############################################################################################
############################################################################################
if __name__ == '__main__':
    img = Tag('img')
    img.src = '/logo.png'
    # img.parent='asda'
    img.alt = 'Логотип'
    # print(img)
    h = Tag('h')
    z = Tag('z')
    h.src = '/logo.png'
    # img.parent='asda'
    h.alt = 'Логотип'
    print(img)
    div = ContainerTag('div')
    div.src="asdfsaf"
    print(div.src)
    # print(img.ToStr())
    div.append_child(img)
    div.append_child(h)
    #div.append_child(z)
    print(div.insert_before(z,img))
    # print(img.parent,"img parenst1")
    # print(img.nextSibling,"img следуюший2")
    # print(img.previousSibling,"img преведуший3")
    # print(h.parent,"h.parent4")
    # print(h.nextSibling,"h cследуюший5")
    # print(h.previousSibling, "h преведуший6")
    # print(div.last_child,"div последний7")
    # print(div.firstChild,"div первый8")
    # i= iter(div)
    # print(next(div))
    # print(next(div))
    # print(next(div))
    # print(next(div))
    #i=iter(div)
    # #print(next(div),"cылки")
    # for i in div.children:
    #     print("!!!!!",i,"9")
    print("da",div,"jhk")
    print(img.parent, "img parenst1")





