class student:
    def __init__(self, student_id, name):
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    def addGrades(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.gradez:
            return 0.0

        return sum(self.gradez) / len(self.gradez)

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("001", "Mario")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calculate_average()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
