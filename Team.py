n=int(input())
i=0
for _ in range(n):
    a=list(map(int,input().split()))
    if sum(a)>=2:
        i+=1
print(i)