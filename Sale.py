n,m=map(int,input().split())
a=list(map(int,input().split()))
earn=0
for i in range(m):
    if min(a)>0:
        break
    else:
        earn=earn-min(a)
        a.remove(min(a))
print(earn)
