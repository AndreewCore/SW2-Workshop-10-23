class student:

    def __init__(s, id, name):
        if not str(id or "").strip():
            raise ValueError("id cannot be empty")
        if not str(name or "").strip():
            raise ValueError("Name cannot be empty")
        s.id = id
        s.name = name
        s.grades = []
        s.isPassed = "NO"
        s.honor = False

    def addGrades(self, g):
        is_number = isinstance(g, (int, float)) and not isinstance(g, bool)
        if is_number and 0 <= g <= 100:
            self.grades.append(g)
        else:
            print("grade must be a valid number between 0 and 100")

    def calculate_average(self):
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def checkHonor(self):
        self.honor = self.calculate_average() >= 90

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
    try:
        a = student("001", "Mario")
    except ValueError as error:
        print(f"Error: {error}")
        return
    a.addGrades(100)
    a.addGrades("Fifty")
    a.calculate_average()
    a.checkHonor()
    a.deleteGrade_by_index(5)
    a.deleteGrade_by_value(4)
    a.report()


startrun()
