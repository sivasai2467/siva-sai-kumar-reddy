x,y=map(int,input().strip().split())
for n in range(x,y + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n,end=" ")
