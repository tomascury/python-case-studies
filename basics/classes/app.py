from Student import Student

student1 = Student("Tom", "Business", 3.1, False)
student2 = Student("Pam", "Art", 4.3, False)

print(student1.name)
print(student1.major)
print(student1.on_honor_roll())

print(student2.gpa)
print(student2.is_on_probation)
print(student2.on_honor_roll())
