import copy

class Favorites:
    def __init__(self):
        self.Foods = []
        self.Colors = []

erics = Favorites()
erics.Foods.append("Pizza")
erics.Colors.append("Blue")
erics.Foods.append("Burgers")

jebs = copy.deepcopy(erics)

jebs.Colors.append("Green")


print("Eric's Colors: ", erics.Colors)
print("Eric's Foods: ", erics.Foods)
print()
print("Jeb's Colors: ", jebs.Colors)
print("Jeb's FoodsL :", jebs.Foods)