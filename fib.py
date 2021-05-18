n=int(input())
n1,n2=0,1
print("fib numbers are:",n1,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
#print()