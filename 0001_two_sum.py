"""
https://leetcode.com/problems/two-sum/

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
Mothod-1: brute force
Time complexity - O(n^2)
"""
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i, val in enumerate(nums):
        remain = target - val
        for j in range(i+1,len(nums)):
          if remain == nums[j]:
            return [i, j]

"""
Mothod-2
Time complexity - O(n)
"""
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      dict = {}
      for i, val in enumerate(nums):
        if target - val in dict:
          return [dict[target-val], i]
        dict[val] = i
