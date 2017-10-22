from collections import OrderedDict,namedtuple


class Courses(object):
    def __init__(self):

        self.namedtuple=namedtuple('namedtuple',['name','studygroup'])
        self.curs=OrderedDict()
        self.count=0

    def add_group(self,name,studygroup):
        self.count+=1
        self.curs[self.count]=self.namedtuple(name=name,studygroup=studygroup)
    def delet_group(self,id):
        pass
    """
    ......
    course<=StudyGroup<=Techer,Studetnt
    """
