#Duck type polymorphism

class A:
    def out(self):
        print("out - A")

class C:
    def out(self):
        print("out - C")

class B:
    def print(self,val):
        val.out()

a = C()
b = B()
b.print(a)

#operator overloading polymorphism

class operation:
    def __init__(self,a,b):
        self.val1 = a
        self.val2 = b
        print("val1:%d  val2:%d"%(self.val1,self.val2))

    def __add__(self,val):
        s1 = self.val1 + self.val2
        s2 = val.val1 + val.val2
        return s1 + s2
    def __gt__(self,val):
        s1 = self.val1 + self.val2
        s2 = val.val1 + val.val2
        if s1 > s2:
            return s1
        else:
            return s2

add1 = operation(30,3)
add2 = operation(30,4)

sum = add1 + add2

print(sum)

print(operation.__gt__(add1,add2))


#method overloading polymorphism

class overload:
    def add(self,a=None,b=None,c=None):
        if c!=None:
            s = a+b+c
        elif b!=None:
            s = a+b
        else:
            s = a
        print("Method Overloadiong")
        print(s)

over = overload()
over.add()


#method overriding

class base:
    def out(self):
        print("base")
class env(base):
    def out(self):
        print("env")

env.out(1)
