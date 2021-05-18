n=int(input())
sum=0
temp=n
for i in range(1,n):
    if(n%i==0):
        sum=sum + i    
        print(i)
if(sum>n):
    print("Abundant")
else:
    print("no")


