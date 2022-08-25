a = [1,2,3,4,5]
i = iter(a)
for j in range(0,1):
    print(i.__next__())

print("_______________________________")

class iterator:
    def __init__(self): 
        self.num = [1,2,3,4,5]
    def __iter__(self):
        return self
    def __next__(self):
        tmp = self.num[0]
        self.num.pop(0)
        self.num.append(tmp)
        print(tmp)
o = iterator()
for i in range(0,8):
    o.__next__()


