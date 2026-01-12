class Student:
    college = "XYZ"
    @classmethod
    def change_college(cls, name):
        cls.college = name

Student.change_college("ABC")
print(Student.college)
