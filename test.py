class student:
    def __init__(self, id, name):
        self.id = id.strip()
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

    def deleteGrade_by_index(self, index):
        if not isinstance(index, int) or isinstance(index, bool):
            print("Error: Index must be an integer.")
            return

        try:
            removed_grade = self.grades.pop(index)
            print(f"Grade {removed_grade} removed successfully.")
        except IndexError:
            print(f"Error: Index {index} is out of bounds.")

    def deleteGrade_by_value(self, grade):
        try:
            self.grades.remove(grade)
            print(f"Grade {grade} removed successfully.")
        except ValueError:
            print(f"Error: Grade {grade} was not found.")

    def report(self):  # broken format
        print("Student ID: " + self.id)
        print("Student Name: " + self.name)
        print("Number of Grades: " + len(self.grades))
        print("Avergae Grade: " + self.calculate_average)
        print("Letter Grade: " + self.letter)
        print("Pass/Fail status: "+self.checkHonor)
        print("Honor Roll status: "+self.checkHonor)

    def calculate_avarage_grade(self):
        if not self.gradez:
            return 0.0
        return sum(self.gradez) / len(self.gradez)

    def Letter_grades(self):
        avg = self.calculate_avarage_grade()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def passed(self):
        avg = self.calculate_avarage_grade()
        if avg >= 60:
            self.isPassed = "Passed"
        else:
            self.isPassed = "Failed"


def startrun():
    a = student("001", "Mario")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calculate_average()
    a.checkHonor()
    a.deleteGrade_by_index(5)
    a.deleteGrade_by_value(4)
    a.report()


startrun()
