n=int(input())
a=list(map(int,input().split()))
c=0
p=0
for i in range(n):
    if a[i]==-1 and p==0:
        c=c+1
    elif a[i]>0:
        p=p+a[i]
    else:
        p=p-1
print(c)