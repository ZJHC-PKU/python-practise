a=list(map(int,input().split()))
A=[]
s=sum(a)/3
for i in a:
    if i!=s:
        A.append(int(s-i))
print(*A)