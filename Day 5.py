# CREATING A LIST OF SIZE n
n=int(input("enter the size of the list"))
l=[]
for i in range(n):
    l.append(int(input("enter the list element")))
print(l)

#Q1. Count even numbers and odd numbers
evencount=0
oddcount=0
for i in range(len(l)):
    if l[i]%2==0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print("Count of even numbers is {}\nCount of odd numbers is {}".format(evencount,oddcount))
        
#Q2. Tell max and min of the list ( without using any inbuilt function like max(),min())
max=l[0]
min=l[0]
for i in range(len(l)):
    if max<l[i]:
       max=l[i]
    if min>l[i]:  
        min=l[i]
print("Maximum of the list is {}\nMinimum of the list is {}".format(max,min)) 
  
#Q3. Check whether the whole list is palindrome or not( eg. [1,2,1] gives yes for palindrome while [1,2,2] doesn't
p=l[::-1]
if l==p:
    print("Yes,List is a palindrome")
else:
    print("No,List is not a palindrome") 
    
#Q4. Print the numbers which are palindrome inside the list    
for i in range(len(l)):
    num=l[i]
    rev=0
    while (num > 0):  
        rem = num % 10  
        rev = (rev * 10) + rem
        num = num // 10  
    if(rev==l[i]):    
        print(rev)   
# (or)
'''for i in range(len(l)):
    temp=str(l[i])
    rev=temp[::-1]
    if rev==temp:
        print(rev)'''