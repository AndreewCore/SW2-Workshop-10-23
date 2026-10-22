class student:
    def __init__(self, student_id, name):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    def addGrades(self, grade):
        """Add a valid grade to the student."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a numeric value.")

        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

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
