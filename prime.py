n=int(input())
p=0
for i in range(2,n//2+1):
    if(n%i==0):
        p=p+1
if(p<=0):
    print("yes")
else:
    print("no")
