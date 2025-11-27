class School:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.teachers={}
        self.classrooms={}

    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
    
    def student_admission(self,student):
        pass

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70 and marks<80:
            return 'A'
        elif marks>=60 and marks<70:
            return 'A-'
        elif marks>=50 and marks <60:
            return 'B'
        elif marks>=40 and marks<50:
            return 'C'
        elif marks>=33 and marks<40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map={
            'A+'    : 4.00,
            'A'     : 3.50,
            'A-'    :3.00,
            'B'     :2.50,
            'C'     :2.00,
            'D'     :1.00,
            'F'     :0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value>=4.5 and value<=5.00:
            return 'A+'
        elif value>=4.00 and value<4.50:
            return 'A'
        elif value>=3.50 and value<4.00:
            return 'A-'
        elif value>=3.00 and value<3.50:
            return 'B'
        elif value>=2.50 and value<3.00:
            return 'C'
        elif value>=1.00 and value<2.50:
            return 'D'
        else:
            return 'F' 
        
    def __repr__(self):
        #all classroom
        #all students
        #all subjects
        #all teachers
        #All Students results
        pass