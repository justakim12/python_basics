## practicing class
from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Computer Science", 3.8, False)

print(student1.gpa)
print(student2.name)
print(student1.on_honor_roll())
print(student2.on_honor_roll())