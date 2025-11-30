import random
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
        self.subject_grade={} #'eng':98
        self.grade=None

    def final_grade(self):
        from school import School
        sum=0
        for i in self.subject_grade.values():
            point=School.grade_to_value(i)
            sum+=point
        if len(self.subject_grade)==0:
            self.grade='N/A'
            return
        
        gpa=sum/len(self.subject_grade)
        self.grade=School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,val):
        self.__id=val

    