t=int(input())
a=[]
for _ in range(t):
    a.append(list(input()))
for i in range(t):
    A=[]
    for j in range(len(a[i])):
        if int(a[i][j])>0:
            A.append(int(a[i][j])*(10**(len(a[i])-j-1)))
    print(len(A))
    print(*A)