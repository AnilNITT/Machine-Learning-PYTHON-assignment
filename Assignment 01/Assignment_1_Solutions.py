Question 1.
Write a function that returns the maximum of two numbers
----------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def max(a,b):
    if a>b:
        return a
    else:
        return b
        
a,b=map(int,input("enter a no").split(","))
max(a,b)

========================================================================================================================================

Question 2.
Write a function called fizz_buzz that takes a number. If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”. If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, 
it should return the same number.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def fizz_buzz(n):
    if(n%3==0) and (n%5==0):
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return n
        
n=int(input("enter a no : "))
fizz_buzz(n)

=======================================================================================================================================

Question 3.
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”. Otherwise, for every 5 km above the speed limit (70),
it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, 
the function should print: “License suspended
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def veh(speed):
    if speed<70:
        print("ok")
    else:
        point=(speed-70)//5
        if point>12:
            print("License suspended")
        else:
            print("points:",point)
        
speed=int(input("enter the vehicle speed: "))
veh(speed)

=======================================================================================================================================

Question 4.
Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a 
label to identify the even and odd numbers. For example, if the limit is 3, it should print:
1.ODD
2.EVEN
3.ODD
4.EVEN
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

def showNumbers(n):
    for i in range(n+1):
        if not i%2:
            print(i+1,"EVEN")
        else:
            print(i+1,"ODD")

n=int(input("enter the limit"))
showNumbers(n)


=======================================================================================================================================

Question 5.
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def sum(limit):
  k=0
  for i in range(0,limit+1):
    if i%3==0 or i%5==0:
      k=k+i
  return k

limit=int(input("enter the limit"))
sum(limit)


=======================================================================================================================================

Question 6.
Write a function called show_stars(rows). If rows is 5, it should print the following:
'*'
'**'
'***'
'**'
'*'
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def show_stars(rows):
    a="*"
    for i in range(1,rows+1):
        if i<(rows/2+1):
            print(a*i)
        else:
            print(a*(rows-i+1))
    
rows=int(input("enter the row no"))
show_stars(rows)

=======================================================================================================================================

Question 7.
Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def prime(limit):
    print("1")
    for i in range(1,limit):
        if(i>1):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i)

limit=int(input("input a limit no"))                    
prime(limit)

=======================================================================================================================================

Question 8.
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
Consider use range(begin, end) method.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
************* with function****************************

def show(x,y):
      L=[]
      for i in range(x,y+1):
            if i%7==0 and i%5!=0:
                  L.append(i)
      print(",".join(map(str,L)))
                
# also take input from user           
# x,y=map(int,input("enter the limit").split(","))
x=2000;y=3000
show(x,y)

-------------------------------------------------------------------------

************** without function ************************

l1=[]
for i in range(2000,3001):
      if i%7==0 and i%5!=0:
            l1.append(i)
print(",".join(map(str,l1)))


=======================================================================================================================================

Question 9.
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
******* simple method  ***************
=============================================

n=int(input("enter a no"))
fact=1
if n<0:
    print("enter positive no")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of ",n," is :",fact)

----------------------------------------------------------------------        

********FACTORIAL USING RECURSION**************
===============================================

def fact(n):
        if n==1 or n==0:
            return 1
        else:
            return n*fact(n-1)  # call again to "fact" function
    
n=int(input("enter the number "))
fact(n)
print("Factorial of ",n," is : ",fact(n))


=======================================================================================================================================

Question 10.
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8 Then,
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

n=int(input("enter a no"))
m=dict()
for i in range(1,n+1):
    m[i]=i*i
print(m)

=======================================================================================================================================

Question 11.
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains 
every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, 
it should be assumed to be a console input. tuple() method can convert list to tuple
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

n=input("enter the nos").split(",")
p=list(n)
q=tuple(n)
# q=list(p)
# p=list(q)
print(p,q)

=======================================================================================================================================

Question 12.
Define a class which has at least two methods: getString: to get a string from console input printString: to print the string 
in upper case. Also please include simple test function to test the class methods.
Hints:
Use init method to construct some parameters
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

class st:
    def getstring(self):
        s=input("input a string")
        self.s=s
    def printstring(self):
        print(self.s.upper())
        
obj=st()
obj.getstring()
obj.printstring()


=======================================================================================================================================

Question 13.
Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 C D)/H] 
Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your 
program in a comma-separated sequence. Example Let us assume the following comma separated 
input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value 
(for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question,
it should be assumed to be a console input
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

****************** Using MATH Module *******************

import math
d=map(int,input("enter the nos: ").split(","))
c=50;h=30
l=[]
for i in d:
    q=int(2*c*i/h)
    q=int(math.sqrt(q))          # findout square root of no
    l.append(q)
print(",".join(map(str,l)))

---------------------------------------------------------

***************** simple Method *************************

d=map(int,input("enter the nos: ").split(","))
c=50;h=30
l=[]
for i in d:
    q=int(2*c*i/h)
    q=int(q**(1/2))      # findout square root of no
    l.append(q)
print(",".join(map(str,l)))


=======================================================================================================================================

Question 14.
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example: Suppose the following inputs are given to the program: 3,5 Then, 
the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======




=======================================================================================================================================

Question 15.
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, 
the output should be: bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

s=input("enter the words : ").split(",")
s.sort()                                      # SORT method prefer CAPITAL letter firsrt sort then small letter like [ A...Z, then a..z]
print(",".join(s))                            # a,b,A,B,Z,z  its sort output is [A,B,Z,a,b,z] look like this



=======================================================================================================================================

Question 16.
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program: Hello world Practice makes perfect
Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

s=input("enter string: ")
print(s.upper())                                # convert all small letter into capital letter
# print(s.lower())                              # convert all Capital letter into small letter


=======================================================================================================================================

Question 17.
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words
and sorting them alphanumerically. 
Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
Then, the output should be: again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. We use set container 
to remove duplicated data automatically and then use sorted() to sort the data.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

s=input("enter string : ").split(" ")
l=[]
for i in s:
    if i in l:
        continue                            # if match duplicate contunue loop
    else:
        l.append(i)                         # not match then add into list

p=sorted(l)                                 # sorting the list
# l.sort()
# print(" ".join(l))
print(" ".join(p))


=======================================================================================================================================

Question 18.
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

x= input("enter the no").split(",")
l=[]
for i in x:
    j=int(i,2)
    if not j%5:                             # if not work on when in ur condition u got ZERO (for integer) , EMPTY or False (for string)
#   if j%5==0:  and if not j%5:             # both r same
        l.append(i)
print(" , ".join(l))


=======================================================================================================================================

Question 19.
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even 
number. The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

l=[]
for i in range(1000,3001):
        a=int(i)%2
        b=int(i/10)%2
        c=int(i/100)%2
        d=int(i/1000)%2
        if (a==0) and (b==0) and (c==0) and (d==0):        
                l.append(i)
   
print(",".join(map(str,l)))


=======================================================================================================================================

Question 20.
Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied 
to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

#s=input("enter a string")
s="hello world! 123"
l=[]
letters=digits=0
for i in range(len(s)):
    if s[i]!=" ":
        if(64<ord(s[i])<123):
                letters+=1
                l.append(s[i])
        elif (s[i].isdigit()):
                digits+=1
                l.append(s[i])
            
#print(l)
print("LETTERS: ",letters, " DIGITS :",digits)


=======================================================================================================================================

Question 21.
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

#s=input("enter a string")
s="Hello world!"
l=[]
lower=upper=0
for i in range(len(s)):
    if s[i]!=" ":
        if(s[i].islower()):
                lower+=1
                l.append(s[i])
        elif (s[i].isupper()):
                upper+=1
                l.append(s[i])
            
#print(l)
print("UPPER CASE : ",upper, " LOWER CASE :",lower)


=======================================================================================================================================

Question 22.
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 23.
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

n=input("enter no").split(",")
l=[]
for i in n:
    l.append(int(i))
p=list(filter(lambda i:(i%2!=0),l))
q=list(map(lambda x:x**2,p))
print(",".join(map(str,p)))
print(",".join(map(str,q)))


=======================================================================================================================================

Question 24.
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following: D 100 W 200
D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100
Then, the output should be: 500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

=======================================================================================================================================

Question 25.
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users. Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords 
   and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example : If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
                              
Then, the output of the program should be:
ABd1234@1
                              
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 26.
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers.The tuples are input by console. The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: 
Then sort by score. The priority is that name > age > score. 
If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.                             
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 27.
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Hints:
Consider use yield
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 28.
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer. 
Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, 
the output of the program should be: 2
Hints:														
In case of input data being supplied to the question, it should be assumed to be a console input. 
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 29.
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3?
Read Python 2 or Python 3.
Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1
Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 30.
Write a method which can calculate square value of number
Hints:
Using the ** operator
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

class a:
    def sqr(self,n):
        self.n=n
        return n**2
n=int(input("enter a no"))  
obj=a()
p=obj.sqr(n)
print(p)
                              
                             
=======================================================================================================================================

Question 31.
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
Hints:
The built-in document method is doc
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 32.
Define a class, which have a class parameter and have a same instance parameter.
Hints:
Define a instance parameter, need add it in init method You can init a object with construct parameter or set the value later
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 33.
Define a function which can compute the sum of two numbers.
Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======


def sum(a,b):
    c=a+b
    return c

a,b=map(int,input("enter the no").split(","))
d=sum(a,b)
print(d)                             
                              
                             =======================================================================================================================================

Question 34.
Define a function that can convert a integer into a string and print it in console.
Hints:
Use str() to convert a number to string.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

def conint(s):
    print(int(s,10))

s=input("input a string")
conint(s)                             

                             =======================================================================================================================================

Question 35.
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
Hints:
Use int() to convert a string to integer.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

def sum(a,b):
    return a+b

#a,b=input("enter two no").split(",")
a,b=map(int,input("enter 2 no : ").split(","))
#a=int(a)
#b=int(b)
sum(a,b)                             
                              
                             =======================================================================================================================================

Question 36.
Define a function that can accept two strings as input and concatenate them and then print it in console.
Hints:
Use + to concatenate the strings
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

def sums(a,b):
    print(a+b)
a,b=input("input two string : ").split(",")
sums(a,b)                             
                              
                             =======================================================================================================================================

Question 37.
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.
Hints:
Use len() function to get the length of a string
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

def st(s,t):
    m=len(s)
    n=len(t)
    if m>n:
        print("Max length of string",m)
    elif n>m:
        print("Max length of string",n)
    else:
        print("both have same length \n",s,"\n",t)
s,t=input("input two strings : ").split(",")
st(s,t)                              
                              
                             =======================================================================================================================================

Question 38.
Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number".
Hints:
Use % operator to check if a number is even or odd.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

def ero(n):
    if not n%2:
        print("it is an even number")
    else:
        print("is is an odd number")

n=int(input("input a number"))
ero(n)                                     
                              
                             =======================================================================================================================================

Question 39.
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) 
and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

d=dict()
for i in range(1,4):
    d[i]=i**2
print(d)                              
                             =======================================================================================================================================

Question 40.
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

d=dict()
for i in range(1,21):
    d[i]=i**2
print(d)                             
                             
                             =======================================================================================================================================

Question 41.
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the values only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number.
Use range() for loops. Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.	
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

d=dict()
for i in range(1,21):
    d[i]=i**2
print(d.values())

