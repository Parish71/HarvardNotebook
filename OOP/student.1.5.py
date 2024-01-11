# Way to make a code with rules for the developer The reason that I'm going through the trouble of defining
# this getter or setter is because I want to make sure that programmers cannot do
#$ things like this.

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    student.house = "Number, FouR"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()
