n=int(input())
flag=0
a=0
a=n//2
if n==1 or n==0:
    print("neither prime nor composite")
else:
    for i in range(2,a+1):
        if n%i==0:
            print("Not a prime")
            flag=1
            break
    if(flag==0):
        print("prime")
    