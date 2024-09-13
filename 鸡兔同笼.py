a=input()
a=int(a)
if a%2==1:
    print(0,0,sep=" ")
else:
    x=a/2
    SumMax=int(a/4+x/2)
    if a%4==0:
        print(int(a/4),SumMax,sep=" ")
    else:
        print(int(a/4+0.5),SumMax,sep=" ")


