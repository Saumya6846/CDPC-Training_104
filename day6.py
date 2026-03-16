#Compare the Triplets HackerRank 

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def compareTriplets(a, b):
#     alice = 0
#     bob = 0

#     for i in range(3):
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1

#     return [alice, bob]

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))
#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

# #A very Big Sum

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'aVeryBigSum' function below.
# #

# def aVeryBigSum(ar):
#     total = 0
#     for i in ar:
#         total = total + i
#     return total

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = aVeryBigSum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#Diagonal Diffrence 

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def diagonalDifference(arr):
#     n = len(arr)
#     sum1 = 0
#     sum2 = 0

#     for i in range(n):
#         sum1 = sum1 + arr[i][i]          # primary diagonal
#         sum2 = sum2 + arr[i][n-i-1]      # secondary diagonal

#     return abs(sum1 - sum2)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#Plus Minus

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def plusMinus(arr):
#     positive = 0
#     negative = 0
#     zero = 0
#     n = len(arr)

#     for i in range(len(arr)):
#         if arr[i] > 0:
#             positive += 1
#         elif arr[i]< 0:
#             negative += 1
#         elif arr[i]==0
#             zero += 1

#     print("{:.6f}".format(positive))
#     print("{:.6f}".format(negative))
#     print("{:.6f}".format(zero))

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)