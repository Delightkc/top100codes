start=int(input())
end=int(input())
flag=0
print("prime numbers are:")
for i in range(start,end):
    for j in range(2,i//2):
        if(i%j==0):
            break
    else:        
        print(i)



