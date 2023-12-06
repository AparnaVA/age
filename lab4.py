number=int(input("enter the number :"))
a=[]
for i in range(1,number+1):
    if (number%i==0):
        a.append(i)
print(a)