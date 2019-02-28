
# coding: utf-8

# In[12]:


# 1. Python program to calculate the average of numbers in given list
n = int(input("enter number of elements to be inserted"))
a=[]
for i in range(0,n):
    elem = int(input("enter element: "))
    a.append(elem)
avg = sum(a)/n
print("average of elements in the list:",round(avg,2))
    
    


# In[14]:


# 2. Python porgram to swap two numbers with out using temp
a = int(input("enter value of first variable: "))
b = int(input("enter value of second variable "))
a = a+b
b = a-b
a = a-b
print(a,b)


# In[1]:


# 3. Program to read a number n and compute n+nn+nnn
n = int(input("enter an integer: "))
temp = str(n)
t1 = temp+temp
t2 = temp+temp+temp
comp = n+int(t1)+int(t2)
print("the value is:",comp)


# In[2]:


#  4. Program to reverse a number
n = int(input("enter a number: "))
rev = 0
while(n>0):
    dig = n%10
    rev = rev*10+dig
    n = n//10
print("reverse of the number is:",rev)


# In[4]:


# 5. Program to check if number is positive or negative
n = int(input("enter an integer: "))
if n>0:
    print("the number is positive integer")
else:
    print("the number is negative intger")


# In[ ]:


# 6. Program to take in the marks of 5 subjects and display the grade
math = int(input("enter the marks:"))
eng = int(input("enter the marks:"))
sci = int(input("enter the marks:"))
soc = int(input("enter the marks:"))
com = int(input("enter the marks"))
a = [math,eng,sci,soc,com]
for i in a:
    if i>=90:
        print("A grade")
    elif i>=80 and i<=89:
        print("B grade")
    elif i>=70 and i<=79:
        print("C grede")
    elif i>=60 and i<=69:
        print("D grade")
    elif i>=50 and i<=59:
        print("E grade")
    else:
        print("F")
    



# In[2]:


# 7. Program to print all numbers in a range divisible by a given numbe
low = int(input("enter lower range: "))
up = int(input("enter upper range:"))
n = int(input("enter a number:"))
for i in range(low,up):
    if i%n == 0:
        print(i)


# In[6]:


# 8. Program to read two numbers and print their quotient and remainder
a = int(input("enter first number:"))
b = int(input("enter second number:"))
q = a/b
r = a%b
print("quptient is equal to:",q)
print("remainder is equal to:",r)


# In[8]:


# 9. Program to accept three digits and print possible combinations to form digit
a = int(input('enter first number'))
b = int(input("enter second number"))
c = int(input("enter third number"))
d = [a,b,c]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j&j!=k&k!=i:
                print(d[i],d[j],d[k])


# In[9]:


# 10. Program to print odd numbers with in a range
n = int(input("enter the range:"))
for i in range(n):
    if i%2 == 1:
        print(i)


# In[11]:


# 11. Program to find sum of digits in a number
n = int(input("enter a number"))
c = 0
while(n>0):
    dig = n%10
    c = c+dig
    n = n//10
print("the total sum of digits is:",c)
    


# In[16]:


# 12.Program to find the smallest divisor of an integer
n = int(input("enter an integer:"))
a=[]
for i in range(2,n+1):
    if n%i == 0:
        a.append(i)
a.sort()
print("smallest divisor is:",a[0])


# In[1]:


# 13. Program to count the number of digits in a number
n = int(input("enter a number:"))
c = 0
while(n>0):
    c += 1
    n = n//10
print("number of digits in a number are:",c)


# In[2]:


# 14. Program to check number is a palindrome
n = int(input("enter number:"))
temp = n
rev = 0
while(n>0):
    dig = n%10
    rev = rev*10+dig
    n = n//10
if temp == rev:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")


# In[28]:


# 15. Program to print all integer that are not divisible by either 2 or 3 and lie between 1 and 50
for i in range(0,51):
    if i%2!= 0 and i%3!= 0:
        print(i)


# In[30]:


# 16. Program to read a number n and add print the series "1+2+...+n="
n = int(input("enter an integer: "))
a = []
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if i<n:
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))


# In[32]:


# 17. Program to print an identity matrix
n = int(input("enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()
        


# In[42]:


# 18. Program to print an inverted star pattern
n = int(input("enter number of rows: "))
for i in range(n,0,-1):
    print(i*'*')


# In[48]:


# 19. Program to check if a date is valid and print the incremented date if it is valid
date = input("enter the date: ")
dd,mm,yy = date.split('/')
dd = int(dd)
mm = int(mm)
yy = int(yy)
if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
    max1=31
elif mm==4 or mm==6 or mm==9 or mm==11:
    max1=30
elif yy%4==0 or yy%100!=0 or yy%400==0:
    max1=29
else:
    max1=28
if mm<1 or mm>12:
    print("the date is invallid")
elif dd<1 or dd>max1:
    print("the date is invalid")
elif dd==max1 and mm!=12:
    dd=1
    mm +=1
    print("incremented date is:",dd,mm,yy)
    
elif dd==31 and mm==12:
    dd=1
    mm=1
    yy +=1
    print("incremented date is:",dd,mm,yy)
else:
    dd += 1
    print("the incremented date is:",dd,mm,yy)




# In[50]:


# 20. Program to compute simple intrest given all the required values
p = float(input('enter the principle amount'))
t = int(input("enter the time:"))
r = float(input("enter the rate"))
i = p*t*r/100
print(i)


# In[51]:


# 21. Program to check whether a given year is leap year
y  = int(input("enter the year:"))
if y%4==0 or y%100!=0 or y%400==0:
    print("the year is a leap year")
else:
    print("the year is not a leap year")


# In[52]:


# 22. Program to read height in cm and convert in feet and inch
cm = float(input("enter the height in cm:"))
inches = 0.394*cm
feet = 0.328*cm
print("height in inches is:",inches)
print('height in feet is:',feet)


# In[55]:


# 23. Program to print the prime factors of an integer
n = int(input("enter an integer:"))
print("factors are:")
i=1
while i<=0:
    k=0
    if n%i==0:
        j=1
        while j<=i:
            if i%j==0:
                k=k+1
            j += j
        if k==2:
            print(i)
    i = i+1


# In[ ]:


# 24.Program to generate all the divisor of an integer
n = int(input("enter an integer: "))
for i in range(1,n+1):
    if n%i==0:
         print(i)


# In[ ]:


# 25.Program to print table of a given number
n = int(input("enter an integer: "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)


# In[1]:


# 26.Program to print sum of negative , positive even number and positive odd number in a list
n = int(input('enter the number of elements in the list: '))
b=[]
for i in range(0,n):
    a = int(input("enter the element:"))
    b.append(a)
sum1 = 0
sum2 = 0
sum3 = 0
for j in b:
    if j>0:
        if j%2 == 0:
            sum1 += j
        else:
            sum2 += j
    else:
        sum3 += j
print('sum of positive even numbers is:',sum1)
print('sum of positive odd numbers is:',sum2)
print('sum of negative numbers is:',sum3)
            


# In[11]:


# 27.Program to print larges even and largest odd in list
n = int(input('enter enumber of elements in a list:'))
b=[]
for i in range(0,n):
    a = int(input('enter element:'))
    b.append(a)
c=[]
d=[]
for j in b:
    if j%2==0:
        c.append(j)
    else:
        d.append(j)
print('the largest of even numbers is:',max(c))
print('the largest of odd number is:',max(d))


# In[16]:


# 28.Program to find the number multiple of 5 and divisible by 7 in the given range
n = int(input('enter the range'))
for i in range(1,n):
    if i%7 ==0 and i%5 ==0:
        print(i)


# In[22]:


# 29.Program to find if the number is armstrog
n = int(input("enter the number"))
a = list(map(int,str(n)))
b = list(map(lambda x:x**3,a))
if sum(b)==n:
    print("the number is an armstrong")
else:
    print("the number is not an armstrong")


# In[24]:


# 30.Program to find LCM of teo numbers
a = int(input('enter the first number'))
b = int(input('enter second number'))
if a>b:
    min1=b
else:
    min1=a
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1 +=1


# In[28]:


# 31.Program to find the GCD of two numbers
import math
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print("the GCD of two numbersa is:",math.gcd(a,b))


# In[37]:


# 32.Program to find the area of the triangle given all three sides
a = float(input('enter first side:'))
b = float(input('enter the second side:'))
c = float(input('enter the thord side:'))
s = a+b+c/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area of the triangle is:',round(area,2))


# In[39]:


# 33.Program to find gravitationl force between two objects
a = int(input('enter number:'))
k=0
for i in range(2,n//2+1):
    if a%i ==0:
        k+=1
if k<=0:
    print('number is prime:')
else:
    print('number is not prime')
     


# In[1]:


# 34.Program to print all prime numbers in a given range
n = int(input('enter upper limit:'))
for a in range(2,n+1):
    k =0
    for i in range(2,a//2+1):
        if a%i == 0:
            k+=1
    if k<=0:
        print(a)


# In[10]:


# 35.Program to check if a number is a perfect number
n = int(input("enter a number"))
s = 0
for i in range(1,n):
    if n % i == 0:
        s +=i
if s==n:
    print("number is perfect ")
else:
    print("number is not perfect")
    


# In[12]:


# 36.Program to print numbers in range without using loops
n = int(input("enter the range"))
b= list(range(1,n))
print(b)


# In[15]:


# 37.Program to find the sum of first n natural numbers
n = int(input('enter a number:'))
s = 0
while n>0:
    s += n
    n -= 1
print("sum of first n natural numberes is:",s)


# In[19]:


# 38.Progrgam to find the sum of series 1+1/2+1/3....+1/n
n = int(input('enter the number of terms'))
s = 0
for i in range(1,n+1):
    s += 1/i
print('sum of series is :',round(s,2))


# In[20]:


# 39.Program to check how many times a number occurs in list
li = [4,5,6,4,5,3,2,3,4]
li.count(4)


# In[21]:


# 40.Progrm to find largest number in list
l = [2,3,4,5,5,6,7,9,10]
max(l)


# In[24]:


# 41.Program to find second largest number in a list
l = [3,6,2,5,9,4,10]
l.sort()
print(l)
print("second largest number is:",l[-2])


# In[26]:


# 42.Program to put even and odd elements in a list into two different lists
l = [2,3,4,6,7,10,13,66,87]
a=[]
b=[]
for i in l:
    if i%2 == 0:
        a.append(i)
    else:
        b.append(i)
print("even list is:",a)
print("odd list is:",b)
        


# In[28]:


# 43.Program to merge two lists and sort it
a = [2,5,7,9,10]
b = [8,1,11,13,18]
c = a+b
c.sort()
print("sorted list is:",c)


# In[33]:


# 44.Program to sort the list according to the second element in sublist
l = ['dog','monkey','lion','tiger']
l.sort(key=len)
print(l)



# In[37]:


# 45.Program to find union of two lists
a = [2,4,6,7,8]
b = [3,4,7,8,9]
c = a+b
print("union of lists is:",list(set(c)))


# In[44]:


# 46.Program to find the intersection of two lists
a = [2,6,4,3,7]
b = [6,4,1,9,3]
c = a+b
d=[]
for i in c:
    if c.count(i)>1:
        d.append(i)
print("intersection of two lists is",list(set(d)))
       


# In[47]:


# 47.Program to creat a list of tuples with the first element as the number and second element as square of the number
l = int(input("enter the lower limit:"))
u = int(input("enter the upper limit:"))
a = [(x,x**2) for x in range(l,u+1)]
print("list of tuples is:",a)
    


# In[56]:


# 48.Program to find all numbers in a range which are perfect squares and sum of all digits in number is less than 10
l = int(input("enter the lower limit:"))
u = int(input("enter the upper limit:"))
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)


# In[61]:


# 49.Program to find the cumilative sum of a list where the ith element is the sum of the first i+1 element from original list
a = [1,2,3,4,5]
b =  [sum(a[0:x+1]) for x in range(0,len(a))]
print("the new list is:",b)


# In[3]:


# 50.Program to generate random numbers from 1 to 20 and appen them to a list
import random
a=[]
n = int(input("enter number of elemnts:"))
for j in range(n):
    a.append(random.randint(1,20))
print(a)


# In[20]:


#  51.Program to swap the first and last values of a list
l = [3,5,6,9,2]
a = l[0]
l[0]=l[-1]
l[-1]=a
print(l)


# In[22]:


# 52.Program to remove duplicate items from the list
l = [4,5,6,4,3,8,4,5,6,8,7,9,10]
list(set(l))


# In[15]:


# 53.Program to remove the ith occurence of the given word in a list where words can repeat
l = ['A','B','A','c','A']
l.pop(2)
print("updated list is:",l)
list(set(l))


# In[10]:


# 54.Program to replace all occurences of 'a' with '$' in a string
n = str(input("enter a string:"))
n = n.replace('a','$')
n = n.replace('A','$')
print("modified string is: ",n)


# In[32]:


# 55.Program to find the nth index charecter from a non empty string
def remove(st,n):
    first = st[:n]
    second= st[n+1:]
    return first+second
st = str(input("enter the string"))
n = int(input("enter the index to be removed: "))
print("modified string is:",remove(st,n))

    


# In[15]:


# 56.Program to detect if two strings are anagrams
s1 = str(input("enter the string 1:"))
s2 = str(input("enter the string2:"))
if sorted(s1)==sorted(s2):
    print("two strings are anagrams")
else:
    print("two strings are anagrams")
    


# In[29]:


# 57.Program to count the number of vowels in a string
s = str(input("enter string:"))
vowels = 0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
         vowels+=1
print("number of vowels is:",vowels)


# In[35]:


# 58.Program to take a string and replace the space with hyphen
s = str(input("enter a string: "))
s = s.replace(' ','-')
print(s)



# In[38]:


# 59.Program to calculate the length of a string without using a library function
s = str(input("enter the string: "))
l = 0
for i in s:
    l+=1
print("length of the string is:",l)


# In[ ]:


# 60.Program to remove charecter of odd index value in a string
s = str(input("enter the string: "))
final =''
for i in s:
    if s.index(i)%2==0:
        final+=i
print(final)


# In[3]:


# 61.Program to calculate the number of words and number of charecters present in a string
s = str(input("enter the string: "))
w = 1
for i in s:
    if i==' ':
        w+=1
print("number of words is: ",w)
print("number of charecters is: ",len(s))
    


# In[5]:


# 62.Program to take two strings and display the larger one without using built in functions
s = str(input("enter the first string: "))
m = str(input("enter the second string: "))
j =0
for i in s:
    j+=1
b = 0
for i in m:
    b+=1
if j>b:
    print("first string is larger")
else:
    print("second string is larger")


# In[6]:


# 63.Program to count number of lower case characters in a string
s = str(input("enter string: "))
c = 0
for i in s:
    if(i.islower()):
        c+=1
print("nuber of lower case charecters is: ",c)


# In[ ]:


# 64.Program to check if a string is a palindrome 
s = str(input("enter string: "))
if s == s[::-1]:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")


# In[1]:


# 65.Program to accept a hyphen separated sequence of words as input and print the words in a hyphen separateed sequence after sorting
 
s = str(input('enter string'))
l = [n for n in s.split('-')]
l.sort()
print('-'.join(l))


# In[7]:


# 66.Program to find the number of letters and digits in a string
s = str(input("enter the string: "))
d = 0
l = 0
for i in s:
    if i.isdigit():
        d+=1
    else:
        l+=1
print("number of digits is: ",d)
print("number of letters is: ",l)
        


# In[8]:


# 67.Program to form a new string made of first 2 and last 2 charecters of given string
s = str(input("enter the string: "))
a = s[:2]+s[-2:]
print("the modified string is: ",a)


# In[11]:


# 68.Program to count the occurences of each of each word in a given string sentence 
s = str(input("enter the string: "))
w = str(input("enter word: "))
a = []
c = 0
a = s.split(" ")
for i in range(0,len(a)):
    if w==a[i]:
        c+=1
print("count of the word is: ",c)


# In[12]:


# 69.Program to check if a sub string is present in a given string
s = str(input("enter the string: "))
sub_s = str(input("enter the word: "))
if s.find(sub_s)==-1:
    print("substring is not present")
else:
    print("substring is present")


# In[ ]:


#70.Program to add a key value pair to the dictionary
key = str(input("enter the key(int) to be added: "))
value = int(input("enter the value to be added: "))
d = {}
d.update({key:value})
print("updated dictionary is :",d)


# In[6]:


# 71.Program to concatenate two dictionaries
d1 = {'hello':23}
d2 = {'hi':45}
d1.update(d2)
print("modified dictionary is: ",d1)


# In[9]:


# 72.Program to check if given key exists in dictonary or not
d = {'a':2,'b':3,'c':4}
k = input("enter the key to check: ")
if k in d.keys():
    print("key is present and value of the key is :",d[k])
else:
    print("key is not present!")



# In[12]:


# 73.Program to generate a dictionary that contains numbers in a range n in the form (x,x*x)
n = int(input("enter a number: "))
d = {x:x*x for x in range(0,n+1)}
print(d)


# In[17]:


# 74.Program to sum all items in dictionary
d = {'a':4,'b':4,'c':4}
print("total sum of values dictionary is: ")
print(sum(d.values()))


# In[18]:


# 75.Program to multiply all values in a dictionary
d = {'a':4,'b':5,'c':6}
c =1
for i in d.values():
    c = c*i
print("the product of all values in a dictionary is: ",c)


# In[20]:


# 76.Program to remove the given key from the dictionary
d = {'a':2,'b':7,'c':6}
n = input('enter the key to be removed: ')
if n in d:
    del d[n]
else:
    print("key not found!")

print("updates dictionary is: ",d)


# In[22]:


# 77.Program to form a dictionary from an object of a class
class di(object):
    def __init__(self):
        self.a=1
        self.b=2
obj = di()
print(obj.__dict__)
    


# In[ ]:


# 78.Program to map two lists into a dictionary
keys = [1,2,3,8]
values = [4,5,6]
d = dict(zip(keys,values))
print("the dictionary is: ",d)


# In[ ]:


# 79.Program to count the frequency of words appearing in a string using a dictionary
s = str(input("enter string"))
l=[]
l = s.split()
wordfreq = [l.count(i) for i in l]
print(dict(zip(l,wordfreq)))


# In[ ]:


# 80.Program to count the number of vowels in a string using set
s = str(input("enter the string: "))
c = 0
vowels = set("aeiou")
for i in s:
    if i in vowels:
    c +=1
    
print("number of vowels in a srting is:",c)


# In[1]:


# 81.Program to check common letters in two input strings
s1 = str(input("enter first string: "))
s2 = str(input("enter second string: "))
l = s1+s2
set(l)


# In[4]:


# 82.Program to display letters which are in first string but not in second string
s1 = str(input("enter first string: "))
s2 = str(input("enter second string: "))
l = set(s1)-set(s2)
print(l)


# In[11]:


# 83.Program to display the letters which are present in both the srings
s1 = str(input("enter first string: "))
s2 = str(input("enter second string: "))
l = set(s1) or set(s2)
print(l)


# In[14]:


# 84.Program to display which letters are in the two strings but not in both
s1 = str(input("enter first string: "))
s2 = str(input("enter second string: "))
l = set(s1)^set(s2)
print(l)


# In[10]:


# 85.Program to read the content of a file
f = open('bhanu.txt')
r=f.readline()
print(r)


# In[9]:


# 86.Program to count the number of words in a text file
f = open('bhanu.txt')
r=f.readline()
print(r)
c = r.split()
print(c)
len(c)


# In[22]:


# 87.Progrgam to count number of lines in a text file
fname= input("enter file name: ")
n = 0
with open(fname,'r') as f:
    for line in f:
        n+=1
print("number of lines: ",n)


# In[27]:


# 88.Porogram to read a string from the user and append it into a file
fname = input("enter file name: ")
f= open(fname,'a')
c = input("enter string to append : \n")
f.write("\n")
f.write(c)
f.close()
print("contents of appended file: ")
f2=open(fname,'r')
line1=f2.readline()
while(line1!=""):
    print(line1)
    line1=f2.readline()
f2.close()


# In[ ]:


# 89.Program to append the contents of file to another file
n1 = input("enter file name to be read from: ")
n2 = input("enter file name to be appended to: ")
fin  = open(n1,"r")
data2 = fin.read()
fin.close()
fout = open(n2, "a")
fout.write(data2)
fout.close()
print()


# In[3]:


# 90.Program to read a file and captalize the first letter of every word in the file
fname = input("enter file name: ")
with open(fname,'r') as f:
    for line in f:
        l = line.title()
        print(l)


# In[4]:


# 91.Program to find the area of a rectangle using class
class rectangle(object):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
a = int(input("enter the length of rectangle: "))
b = int(input("enter the breadth of rectangle: "))
obj = rectangle(a,b)
print("area of the rectangle is: ",obj.area())
print()



# In[3]:


# 92.Program to append , delete and display elements of a list using classs
class check(object):
    def __init__(self,a,b):
        self.n=[]
    def add():
        return self.n.append(a)
    def remove():
        self.n.remove(b)
    def dis(self):
        return (self.n)
a = int(input("enter first number"))
b = int(input("enter second number"))
obj = check(a,b)
choice = 1
while choice !=0:
    print("0.exist")
    print("1.add")
    print("2.delete")
    print("3.display")
    choice = int(input("enter the choise: "))
    if choice == 1:
        n = int(input("enter the number to add"))
        obj.add(n)
        print("list: ",obj.dis())
    elif choice==2:
        n = int(input("enter the nuber to delete: "))
        obj.remove(n)
        print("list: ",obj.dis())

    elif choice==3:
        print("list: ",obj.dis())
    elif choice==0:
        print("exiting!")
    else:
        print("invalid choice!")


# In[8]:


# 93.Program to find the area and perimeter of the circle
import math
class circle(object):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
a = int(input("enter the radius of circle: "))
obj = circle(a)
print("area of circle is: ",round(obj.area(),2))
print("perimeter of circle is: ",round(obj.perimeter(),2))


# In[5]:


# 94.Program to create a class in which perform basic calculator operations
class calculator(object):
    def __ini__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def divide(self):
        return self.a//self.b
a = int(input("enter first number:"))
b = int(input("enter second number:"))
obj = calculator()
choice=1
while choice!=0:
        print("0.exit")
        print("1.addition")
        print("2.subtract")
        print("3.multiplication")
        print("4.division")
        choice =int(input("enter choice:"))
        if choice == 1:
               print("result is:",obj.add())
        elif choice==2:
               print("result is:",obj.sub())
        elif choice==3:
               print("result is:",obj.mult())
        elif choice==4:
               print("result is:",obj.divide())
        elif choice==0:
               print("exiting!")
        else:
               print("invalid input")


# In[ ]:


# 95.Program to print only image files under a file
from PIL import Image
image = Image.open('emoji.jpg')
image.show()


# In[8]:


# 96.Program to concatinate two dictionaries
a = {'a':2,'b':3}
b = {'c':4}
a.update(b)
print(a)


# In[ ]:




