a=list(input())
c=1
d=1
for i in range(len(a)-1):
    if a[i]==a[i+1]=="0":
        c+=1
        d=1
    elif a[i]==a[i+1]=="1":
        d+=1
        c=1
    else:
        c=d=1
    if c>=7 or d>=7:
        print("YES")
        break
if c<7 and d<7:
    print("NO")