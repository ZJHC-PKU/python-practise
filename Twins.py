n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
s=0
for i in range(n):
    s=s+a[i]
    if s>sum(a[i+1:]):
        print(i+1)
        break