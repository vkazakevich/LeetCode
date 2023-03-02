'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
'''

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums


# Result
s = Solution()
print(s.runningSum([3, 1, 2, 10, 1]))  # [3,4,6,16,17]
