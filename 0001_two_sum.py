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
