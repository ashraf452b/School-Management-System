from school import *
from person import *
from subject import *
from classroom import *


school=School('Visca EL Barca', 'Barcelona')

#ClassRoom
eight=Classroom('Eight')
nine=Classroom('Nine')
ten=Classroom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#Student 
messi=Student('Messi',eight)
xavi=Student('Xavi',eight)
inesta=Student('Andres inesta',eight)
rakitic=Student('Ivan Rakitic',nine)
moneymar=Student('Neymar',ten)

school.student_admission(messi)
school.student_admission(xavi)
school.student_admission(inesta)
school.student_admission(rakitic)
school.student_admission(moneymar)


#Teacher
guardiola=Teacher('big match experiment')
enrique=Teacher('Luis Thousand Pass')


#subject
tikitaka=Subject('Pass de',guardiola)
bangla=Subject('Bangla',enrique)
english=Subject('English',enrique)
math=Subject('Math',guardiola)

school.add_teacher(tikitaka,guardiola)
school.add_teacher(bangla,guardiola)
school.add_teacher(english,guardiola)
school.add_teacher(math,guardiola)

school.add_teacher(tikitaka,enrique)
school.add_teacher(bangla,enrique)
school.add_teacher(english,enrique)
school.add_teacher(math,enrique)


eight.add_subjects(tikitaka)
eight.add_subjects(math)

nine.add_subjects(english)
nine.add_subjects(math)
nine.add_subjects(bangla)

ten.add_subjects(tikitaka)
ten.add_subjects(bangla)
ten.add_subjects(english)
ten.add_subjects(math)

eight.take_semester_final_exam()

nine.take_semester_final_exam()

ten.take_semester_final_exam()
print(school)