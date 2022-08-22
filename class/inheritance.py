#single_inheritance

class Master:
    def __init__(self):
        print("Master")

class Slave(Master):
    def __init__(self):
        super().__init__() 
        print("Slave")
slave = Slave()


#multi_level_inheritance

class Grandfather:
    def __init__(self):
        print("Grandfather")
class Father(Grandfather):
    def __init__(self):
        super().__init__()
        print("Father")
class Child(Father):
    def __init__(self):
        super().__init__()
        print("Child")

child = Child()

#multiple_inheritance

class Husband:
    def __init__(self):
        print("Husband")
class Wife:
    def __init__(self):
        print("Wife")
class Kid(Husband,Wife):    # MRO will count from left
    def __init__(self):
        super().__init__()
        print("Kid")

kid = Kid()
