import random
number=int(input("enter the number : "))
x=random.randint(1,9)
print(x)
if number<x:
    print("too low")
elif number>x:
    print("too high")
else:
    print("exactly right")
