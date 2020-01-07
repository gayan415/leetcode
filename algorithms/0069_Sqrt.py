"""
https://leetcode.com/problems/sqrtx/

69. Sqrt(x)

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
            the decimal part is truncated, 2 is returned.
"""
import math
class Solution1:
  def mySqrt(self, x: int) -> int:
    return int(math.sqrt(x))

# Pocket Calculator Algorithm
from math import e, log
class Solution2:
  def mySqrt(self, x: int) -> int:
    if 2 > x:
      return x
    
    left = int(e**(0.5 * log(x)))
    right = left + 1
    
    if right * right > x:
      return left
    else:
      return right

class Solution3:
  def mySqrt(self, x: int) -> int:
    return int(x ** (1/2))
