n = int(input("Enter the number:"))
for i in range(0,int(n/2)):
    print(" "*i+str(int(n-i))+str(int((n-2)-(i*2))*" ")+str(int(i+1))+" "*i)
if n%2 != 0:
    print(str(" "*int((n-1)/2))+str(int(n/2)+1)+str(" "*int((n-1)/2)))
for i in range(int(n/2),0,-1):
    i=i-1
    print(" "*i+str(int(n-i))+str(int((n-2)-(i*2))*" ")+str(int(i+1))+" "*i)
