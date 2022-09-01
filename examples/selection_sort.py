def sort(ll):
    for i in range(len(ll)-2):
        ind = i
        for j in range(i,len(ll)):
            if ll[j] < ll[ind]:
                ind = j
        tmp = ll[i]
        ll[i]= ll[ind]
        ll[ind] =tmp
    print(ll)


a = [3,2,5,4,6,9,8,1]
sort(a)

