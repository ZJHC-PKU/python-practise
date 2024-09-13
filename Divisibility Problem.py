t=int(input())
a=[list(map(int,input().split())) for _ in range(t)]
for i in range(t):
    if a[i][0]%a[i][1]!=0:
        c=a[i][1]-a[i][0]%a[i][1]
    else:
        c=0
    print(c)