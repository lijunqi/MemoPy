
class Student():
    def __init__(self, number):
        self.num = number

    def __repr__(self):
        return f"Student_{self.num}"

s1 = Student(1)
s2 = Student(2)
s3 = Student(3)
s4 = Student(4)
s5 = Student(5)
s6 = Student(6)

all_students = [s2, s3, s1, s5, s6, s4]
print("Before sort: ", all_students)

all_students.sort(key=lambda x: x.num, reverse=True)
print("After sort: ")
for stu in all_students:
    print(stu)
