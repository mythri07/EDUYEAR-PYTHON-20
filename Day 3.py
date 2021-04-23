#AGE CALCULATOR
year_of_birth=int(input())
print("Age is {}".format(2020-year_of_birth))

#SIMPLE CALCULATOR
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
print("Addition is {}".format(num1+num2))
print("Subtraction is {}".format(num1-num2))
print("Multiplication is {}".format(num1*num2))
print("Division is {}".format(num1/num2))
print("Floor Division is {}".format(num1//num2))
print("Remainder is {}".format(num1%num2))
print("Power is {}".format(num1**num2))

#COUNT OCCURRENCES OF CHARACTER 'Y'
name=input("Enter a String")
county=name.count('y')
print("The Count of 'Y' is {}".format(county))

#EVEN INDEXED CHARACTERS
a=input("Enter a String")
print(a[1::2])