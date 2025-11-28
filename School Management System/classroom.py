class Classroom:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.subjects=[]
    
    def add_student(self,student):
        roll=f"{self.name}-{len(self.students)+1}"
        student.id=roll
        self.students.append(student)

    def add_subjects(self,subject):
        self.subjects.append(subject)

    def take_semester_final_exam(self):
        for i in self.subjects:
            i.exam(self.students)
        for i in self.students:
            i.final_grade
        
        