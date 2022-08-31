def bin_search(ll,num):
    low = 0
    high = len(ll)
    mid = int(high/2)
    if num == ll[mid] or num == ll[low] or num == ll[high-1]:
        print(ll[mid],ll[low],ll[high-1])
        return True
    elif num < ll[mid]:
        ll = ll[low:mid]
        return bin_search(ll,num)
    else:
        ll = ll[mid::]
        return bin_search(ll,num)
    return False
a = []
for i in range(10000):
    a.append(i)
n=9806
if bin_search(a,n):
    print("yes")
else:
    print("no")

