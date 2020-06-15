# Module 8
#   Programming Assignment 11
#     Prob-2.py

# Your code below
class Student:
    def __init__(self, name, IDnumber, major, GPA):
       self._name = name
       self._IDnumber = IDnumber
       self._major = major
       self._GPA = GPA

    def set_name(self, name):
        self._name = name
    
    def set_IDnumber(self, IDnumber):
        self._IDnumber = IDnumber

    def set_major(self, major):
        self._major = major

    def set_GPA(self, GPA):
        self._GPA = GPA

    def get_name(self):
        return self._name

    def get_IDnumber(self):
        return self._IDnumber

    def get_major(self):
        return self._major

    def get_GPA(self):
        return self._GPA

def studentTest():
    studentList = []
    studentList.append(Student("Joe Bella", "9933"))
    studentList.append(Student("Tucker Blank", "3399"))
    studentList.append(Student("Gayle Ujifusa", "1011"))
    studentList.append(Student("Edna Anker", "9875"))

    studentList[0].set_major("Web Development")
    studentList[1].set_major("Nursing")
    studentList[2].set_major("Baking")
    studentList[3].set_major("Medical Office")

    studentList[0].set_GPA("3.8")
    studentList[1].set_GPA("3.0")
    studentList[2].set_GPA("2.8")
    studentList[3].set_GPA("3.0")

    for element in studentList:
        print(element.get_name())
        print(element.get_IDnumber())
        print(element.get_major())
        print(element.get_GPA())
        print()

    if __name__ == '__main__':
        studentTest()
    
