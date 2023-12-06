str=input("enter the string : ")
p=len(str)
flag=0
j=-1
for i in str:
    if i !=str[j]:
        flag=1
        break
    j=j-1
if(flag==0):
    print("palindrome")
else:
    print("not palindrome")
