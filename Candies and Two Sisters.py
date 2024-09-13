t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
for i in range(t):
    if a[i]%2==0:
        print(int(a[i]/2-1))
    else:
        print(int(a[i]//2))