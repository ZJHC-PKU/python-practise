t=int(input())
A=[]
for _ in range(t):
    a=list(map(int,input().split()))
    if a[0]+a[1]==a[2]:
        A.append("YES")
    elif a[1]+a[2]==a[0]:
        A.append("YES")
    elif a[2]+a[0]==a[1]:
        A.append("YES")
    else:
        A.append("NO")
for i in A:
    print(i)
