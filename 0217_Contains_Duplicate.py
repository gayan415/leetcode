"""
https://leetcode.com/problems/contains-duplicate/

217. Contains Duplicate

Eg1:
Input: [1,2,3,1]
Output: true
Eg2:
Input: [1,2,3,4]
Output: false
"""
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
