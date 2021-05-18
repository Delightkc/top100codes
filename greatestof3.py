first=int(input())
second=int(input())
third=int(input())
if first>second and first>third:
    print(first," is greater")
elif second>first and second>third:
    print(second," is greater")
else:
    print(third," is greater")