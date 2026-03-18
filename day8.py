# Leet Code 

# TWO SUM 

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

#Fizz Buzz

# from typing import List

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         result = []

#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))

#         return result


#  Running Sum of 1d Array

# from typing import List

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] = nums[i] + nums[i - 1]
#         return nums