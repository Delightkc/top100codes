def lcmfinder(num1,num2):
    if num1>num2:
        larger=num1
    else:
        larger=num2
    while True:
        if (larger % num1 == 0) and (larger % num2 == 0) :
            lcm=larger
            break
        larger+=1
    print(lcm)

num1, num2 = map(int, input().split())
lcmfinder(num1,num2)
