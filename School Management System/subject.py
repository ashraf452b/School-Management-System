from person import  *
from school import *
class Subject:
    def __init__(self, name, teacher):
        self.name=name
        self.teacher=teacher
        self.max_marks=100
        self.pass_marks=33


    def exam(self,students):
        for i in students:
            mark=self.teacher.evaluate()
            i.marks[self.name]=mark
            i.subject_grade[self.name]=School.calculate_grade(mark)
