n=int(input())
a=list(map(int,input().split()))
a=[i%2 for i in a]
if sum(a)==1:
    print(a.index(1)+1)
else:
    print(a.index(0)+1)