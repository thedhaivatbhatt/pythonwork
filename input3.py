#write a program to split one number accept number from user only 2 digit
#num1=56
# first =5 , sec =6
num1 = int(input("enter value of num1"))
# num1=56
first = int(num1/10)
second=num1%10
print("the value of ",first,"the value of second is",second)