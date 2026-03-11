# n=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end="\t")
#         n=n+1
#     print()

#Print ASKY VALUE using For loop

# n=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end="")
#         n=n+1
#     print()

#     #small Letters

#     n=97
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end="")
#         n=n+1
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#          print(i,end="")
#     print()

#Print (*)

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#          print("*",end="")
#     print()

# ls=[]
# print(type(ls))
# print(ls)

# 0 1 2 3 4
# ls=[12,3,36,45,645]
# print(ls)

# #Using For Loop (ls)

# for i in range(len(ls)):
#     print(ls[i])

#     #Using For Loop 

# for i in ls:
#     print(i)


#(ls) append 

# ls=[12,3,36,45,645]
# print(ls)
# ls.append(66)
# ls.append(69)
# ls.pop(3)
# print(ls)

# #Negative no.

# ls=[12,3,36,45,645]
# print(ls)
# print(ls[-1])

#List printing 

# ls=[12,3,36,45,64,77,88,99]
# print(ls[1:5])

#Print Same
# s='saumya'
# print(s)

#Reverse of Name
# s='saumya'
# print(s[::-1])

#TASK

#Check whether a number is Even or Odd

no=int(input("Enter number: "))

if no%2==0:
    print("Even Number")
else:
    print("Odd Number")

#Find Largest of Three Numbers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b and a>c:
    print("Largest =",a)
elif b>c:
    print("Largest =",b)
else:
    print("Largest =",c)

#Check Positive, Negative or Zero

no=int(input("Enter number: "))

if no>0:
    print("Positive")
elif no<0:
    print("Negative")
else:
    print("Zero")

#Check Number Divisible by 3 and 5

no=int(input("Enter number: "))

if no%3==0 and no%5==0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible")

#Print Numbers from 1 to N

n=int(input("Enter value: "))

for i in range(1,n+1):
    print(i)

#Print All Even Numbers from 1 to N

n=int(input("Enter value: "))

for i in range(1,n+1):
    if i%2==0:
        print(i)

#Sum of First N Natural Numbers

n=int(input("Enter value: "))
sum=0

for i in range(1,n+1):
    sum=sum+i

print("Sum =",sum)

#Factorial of a Number

no=int(input("Enter number: "))
fact=1

for i in range(1,no+1):
    fact=fact*i

print("Factorial =",fact)

#Multiplication Table

no=int(input("Enter number: "))

for i in range(1,11):
    print(no,"*",i,"=",no*i)

#Count Number of Digits

no=int(input("Enter number: "))
count=0

while no>0:
    no=no//10
    count=count+1

print("Digits =",count)

#Reverse a Number

no=int(input("Enter number: "))
rev=0

while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10

print("Reverse =",rev)

#Check Palindrome

no=int(input("Enter number: "))
temp=no
rev=0

while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10

if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Sum of Digits

no=int(input("Enter number: "))
sum=0

while no>0:
    rem=no%10
    sum=sum+rem
    no=no//10

print("Sum =",sum)

#Armstrong Number

no=int(input("Enter number: "))
temp=no
sum=0
count=0

while no>0:
    no=no//10
    count=count+1

no=temp

while no>0:
    rem=no%10
    sum=sum+rem**count
    no=no//10

if temp==sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")

#Numbers Divisible by 7 between 1 and N

n=int(input("Enter value: "))

for i in range(1,n+1):
    if i%7==0:
        print(i)


