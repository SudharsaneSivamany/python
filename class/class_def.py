class skeleton:
    bones = 206
    def __init__(self,name,sex,age):
        self.name = name
        self.sex  = sex
        self.age  = age

    def compare(self,var):
        if self.age == var.age:
            return "yes"
        else:
            return "no"
    @staticmethod
    def avg(value):
        out = 0
        count = 0
        for i in value:
            count+=1
            out = out + i
        return out/count
    @classmethod
    def bone_number(cls):
        return cls.bones

body1 = skeleton("aadhi","male",27)
body2 = skeleton("kani","female",26)

print(body1.compare(body2))

print(skeleton.bones)

print(skeleton.avg([23,54,12,87,34]))

print(skeleton.bone_number())



