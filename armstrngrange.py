lower=int(input())
upper=int(input())
for num in range(lower,upper+1):
    sum=0
    temp=num
    order=len(str(num))
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
    if(num==sum):
        print(num)