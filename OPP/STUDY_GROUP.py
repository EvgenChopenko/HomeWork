from collections import OrderedDict


class StudyGroup(object):
    def __init__(self,num_group):
        """
        Учкбная группа состоит из студентов и учителя в каждой группе может быть много студетнтов и один учитиель!
        """
        self.Student = OrderedDict()
        self.Teacher = None
        self.countstudent=0
        self.num_group=num_group

    def add_student(self,student):
        """
        student :type Student

        :return:None
        """
        self.countstudent+=1
        self.Student[self.countstudent]=student

    def add_teacher(self,teacher):
        if self.Teacher is None:
            self.Teacher=teacher
        else:
            print("Error учитель у группы уже есть")

    def new_teacher(self,teacher):
        print("вместо учителя {} в группе новый уучитель {}".format(self.Teacher.show(),teacher.show()))
        self.Teacher=teacher

    def delete_teacher(self):
        print("у группы нет учителя")
        self.Teacher=None

    def delete_student(self,student):
        pass
    def student_replacement(self,student_old,student_new):
        pass


