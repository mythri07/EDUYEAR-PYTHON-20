
#NUMBERS WHICH ARE DIVISIBLE BY BOTH 5 AND 7
n=int(input("enter number"))
m=int(input("enter number"))
for i in range(n,m+1):
    if i%5==0 and i%7==0:
        print(i)
        
#SUM OF THE SERIES(2+22+222+....)      
no_of_terms=int(input("enter no of terms"))
a='2'
count=0
for i in range(1,no_of_terms+1):
     count=count+int(a*i)
print(count)    

#SUM OF GIVEN NUMBERS USING WHILE LOOP
sum=0
while 1:
    a=input("enter number")
    if a=='q':
        break
    else:
       b=int(a)
       sum=sum+b
print(sum)

#FACTORIAL OF A NUMBER
number=int(input("enter number"))
count=1
for i in range(1,number+1):
    count=count*i
print("Factorial of {} is {}".format(number,count))