def generator(actual):
    name = ["friend","lover","affection","marriage","enemy","sister"]
    for i in range(0,5):
        for j in range(0,actual):
                tmp = name[0]
                name.pop(0)
                name.append(tmp)
        name.remove(tmp)
    yield name[0]
name1 = input("Enter the name1:")
name2 = input("Enter the name2:")
name1 = name1.lower()
name2 = name2.lower()
name1 = name1.replace(" ","")
name2 = name2.replace(" ","")
init_count  = 0
for i in range(0,len(name1)):
    for j in range(0,len(name2)):
        if name1[i] == name2[j]:
            name2 = name2.replace(name2[j],"",1)
            init_count +=1
            break
actual = len(name1)-init_count+len(name2)
flames = generator(actual)
print("Relationship:",flames.__next__())
