def topten():
    n=1
    while n <= 10:
        yield n
        n +=1

val = topten()
for i in val:
    print(i)
