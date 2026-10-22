class student:
    def __init__(s, id, name):
        if id is not None & name is not None:
            s.id = id
            s.name = name
            s.gradez = []
            s.isPassed = "NO"
            s.honor = "?"
        elif id is None:
            print("id cannot be empty")
        elif name is None:
            print("Name cannot be empty")
        else:
            print("An error ocurred, could not create student")

    def addGrades(self, g):
        if isinstance(g, int) & g > 0 & g < 100:
            self.gradez.append(g)
        else:
            print("grade must be a valid number between 0 and 100")


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
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calculate_average()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
