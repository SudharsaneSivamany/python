def bin_search(ll,num):
    low = 0
    high = len(ll)
    mid = int(high/2)
    if num == ll[mid] or num == ll[low] or num == ll[high-1]:
        print(ll[mid],ll[low],ll[high-1])
        return True
    if len(ll) <= 3:
        return False
    if num < ll[mid]:
        ll = ll[low:mid]
        return bin_search(ll,num)
    else:
        ll = ll[mid::]
        return bin_search(ll,num)
a = []
for i in range(10000):
    a.append(i)
n=98096
if bin_search(a,n):
    print("yes")
else:
    print("no")

