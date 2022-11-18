class Student:
    print('hi')
    def __init__(self, height=160):
        self.height = height

sasha = Student()
print(sasha.height)

dina = Student(height=167)
print(dina.height)