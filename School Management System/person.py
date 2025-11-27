import random
from school import *
class Person:
    def __init__(self,name):
        self.name=name
    

class Teacher(Person):
    def __init__(self,name):
        super().__init__(name) 
    def evaluate(self):
        return random.randint(1,100)
    

class Student(Person):
    def __init__(self,name,classroom):
        super().__init__(name)
        self.classroom=classroom
        self.__id=None
        self.marks={}
        self.subject_grade={}
        self.grade=None

    def final_grade(self):
        sum=0
        for i in self.subject_grade.values():
            point=School.grade_to_value(i)
            sum+=point

        gpa=sum/len(self.subject_grade)
        self.grade=School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,val):
        if val>0:
            self.__id=val

    