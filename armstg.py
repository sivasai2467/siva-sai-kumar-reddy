n=int(input())
o=list(map(int,str(n)))
p=list(map(lambda x:x**3,o))
if(sum(p)==n):
    print("yes")
else:
    print("no")
