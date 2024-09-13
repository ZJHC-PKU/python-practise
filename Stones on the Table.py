n=int(input())
s=list(input())
a=0
for i in range(n-1):
    if s[i]==s[i+1]:
        a+=1
print(a)