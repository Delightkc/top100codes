num=int(input())
sum=0
temp=num
order=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+digit**order
    temp=temp//10
if(num==sum):
    print("Armstrong")
else:
    print("no")