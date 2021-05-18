num1, num2 = map(int, input().split())
if(num1>num2):
    smaller=num2
else:
    smaller=num1
for i in range(1,smaller+1):
    if num1 % i == 0 and num2 % i == 0 :
        hcf=i
print(hcf)
