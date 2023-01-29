'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for item in nums:
            if item in duplicates:
                return True

            duplicates[item] = True

        return False


# Result
s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))  # True
