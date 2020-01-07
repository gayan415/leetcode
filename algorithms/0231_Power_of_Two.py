"""
https://leetcode.com/problems/power-of-two/

231. Power of Two

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
"""
import math
class Solution1:
  def isPowerOfTwo(self, n: int) -> bool:
    if n<= 0:
      return False

    if int((str(math.log2(n)).split('.')[1])) == 0:
      return True
    else:
      return False

class Solution2:
  def isPowerOfTwo(self, n: int) -> bool:
    if n == 0:
      return False
    
    return n & (-n) == n
