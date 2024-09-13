a=[list(map(int,input().split())) for _ in range(5)]
for i in range(5):
    if sum(a[i])==1:
        for j in range(5):
            if a[i][j]==1:
                break
        break
print(abs(i-2)+abs(j-2))