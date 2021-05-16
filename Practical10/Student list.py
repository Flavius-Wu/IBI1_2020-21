class Student:
    def __init__(self, firstname, lastname, programme):
        self.f = firstname
        self.l = lastname
        self.p = programme
    def __str__(self):
        return "%s %s %s" % (self.f, self.l, self.p)



information1 = Student("Yuefeng", "Wu", "BMI")

print(information1)


