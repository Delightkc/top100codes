def fact(n):
    if(n<0):
        return "no negative for factorial" 
    elif(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n=int(input())
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+fact(digit)
    temp=temp//10
if(n==sum):
    print("strong")
else:
    print("no")
