class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.probation = is_on_probation

#from 'classes and objects' import Student

student1 = Student("Jim", "Business", "3.5", False)

print(student1.name)
print(student1.gpa)
