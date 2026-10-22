class student:

    def __init__(s, id, name):
        if not str(id or "").strip():
            raise ValueError("id cannot be empty")
        if not str(name or "").strip():
            raise ValueError("Name cannot be empty")
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = False

    def addGrades(self, g):
        is_number = isinstance(g, (int, float)) and not isinstance(g, bool)
        if is_number and 0 <= g <= 100:
            self.gradez.append(g)
        else:
            print("grade must be a valid number between 0 and 100")

    def calculate_average(self):
        if not self.gradez:
            return 0.0

        return sum(self.gradez) / len(self.gradez)

    def checkHonor(self):
        self.honor = self.calculate_average() >= 90

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    try:
        a = student("x", "")
    except ValueError as error:
        print(f"Error: {error}")
        return
    a.addGrades(100)
    a.addGrades("Fifty")
    a.calculate_average()
    a.checkHonor()
    a.deleteGrade(5)
    a.report()


startrun()
