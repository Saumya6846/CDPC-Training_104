#Simple Array


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'simpleArraySum' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY ar as parameter.
# #

# def simpleArraySum(ar):
#     # Write your code here
#     sum = 0
#     for i in ar:
#         sum = sum + i
#     return sum
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#Accept 4 numbers and find max numbers

# n1=int(input("Enter value: "))
# n2=int(input("Enter value: "))
# n3=int(input("Enter value: "))
# n4=int(input("Enter value: "))

# max = n1

# if n2 > max:
#     max = n2
# if n3 > max:
#     max = n3
# if n4 > max:
#     max = n4

# print("Maximum number is:", max)

#Result : 
# Enter value: 45
# Enter value: 55
# Enter value: 66
# Enter value: 11
# Maximum number is: 66

# n1=int(input("Enter value: "))
# n2=int(input("Enter value: "))
# n3=int(input("Enter value: "))
# n4=int(input("Enter value: "))

# min = n1

# if n2 < min:
#      min = n2
# if n3 > min:
#      min = n3
# if n4 > min:
#      min = n4

# print("Minimum number is:", min)

#Min & Max in one Program

# arr = [5,3,9,2,8]

# max = arr[0]
# min = arr[0]

# for i in range(1, len(arr)):
#     if max<arr[i]:
#         max=arr[i]
#     if min>arr[i]:
#         min=arr[i]

# print("Maximum:", max)
# print("Minimum:", min)

# Result : 
# Maximum: 9
# Minimum: 2

#Check Leap Year

# year=int(input("Enter year: "))
# if year%100!=0:
#     if year%4==0:
#        print("Non century leap year")
#     else:
#      print("Not leap year")
# else:
#     if year%400==0:
#          print("century leap year")
#     else:
#          print("Not leap year")
#  Result : 
# Enter year: 2006
# Not leap year

#Tech Number

# no=int(input("Enter number: "))
# n1=no%100
# n2=no//100
# sum=n1+n2
# sq=sum**2
# if sq==no:
#    print("Tech no")
# else:
#   print("Not Tech no")

#   Result : 
# Enter number: 2025
# Tech no

