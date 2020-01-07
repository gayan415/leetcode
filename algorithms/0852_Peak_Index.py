"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

852. Peak Index in a Mountain Array

Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1
"""

class Solution2:
  def peakIndexInMountainArray(self, A: List[int]) -> int:
    if 2 > len(A):
      return 0
    else:
      for i in range(len(A)-1):
        if A[i] > A[i+1]:
          return i

# This solution is too slow
class Solution2:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
