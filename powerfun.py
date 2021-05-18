def pow(b,e):
    if(e==0):
        return 1
    else:
        return b*pow(b,e-1)
b=int(input())
e=int(input())
print(pow(b,e))