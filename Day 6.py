'''Q1. Give all the index values of vowels.
Eg. "abed" 
>> 0 2'''
string=input("Enter the String")
for i in range(len(string)):
    if(string[i]=='a'or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
        print(i,end=" ")

'''Q2.Reverse the words of a string
Eg.Input... hello world happy birthday
Output... birthday happy world hello'''
a=input("\nenter the string")
b=a.split()
b=b[::-1]
reverse_string=' '.join(b)
print(reverse_string)
   
'''Q3. Remove duplicate elemnts without using set()
Ex. 
[1,2,3,3,2,4]
>> [1,2,3,4]   '''
a = list(map(int,input("\nEnter the numbers : ").split()))
new=[]
for i in range(len(a)):
    if a[i] not in new:
        new.append(a[i])
print(new)              
    
    

  