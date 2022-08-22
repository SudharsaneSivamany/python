class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.laptop()

    def show(self):
       return self.name, self.rollno, self.laptop.brand, self.laptop.rel

    class laptop:
        def __init__(self):
            self.brand = "hp"
            self.rel   = 1.0

s1 = student("john",1001)
s2 = student("marc",1002)

print(s1.show())
