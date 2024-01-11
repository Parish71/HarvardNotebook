import random

class Hat:
    houses =  ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)

Hat.sort("Harry")
