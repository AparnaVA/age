from datetime import date
name=input("enter your name :")
age=int(input("enter your age : "))
old=100-age
today=date.today()
year=today.year+old
print("hello" ,name, "you will became 100 years old in ",year)
