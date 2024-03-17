a=2
b=5
c=4
d=5
print("before swap a={0} and b={1}".format(a,b))
print("before swap c={0} and d={1}".format(c,d))
temp=a
a=b
b=temp
print("after swap a={0} and b={1}".format(a,b))
c=c+d
d=c-d
c=c-d
print("after swap c={0} and d={1}".format(c,d))