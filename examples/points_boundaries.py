def check(p,b):
    count=0
    out = []
    for i in range(int(len(b)-1)):
        for j in range(len(p)):
            if p[j] >= b[i] and p[j] < b[i+1]:
                count +=1
        out.append(count)
        count = 0
    print(out)
points = [2,55,7,88,1]
boundaries = [0,5,50,100]

check(points,boundaries)
