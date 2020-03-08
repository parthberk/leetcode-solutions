"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = [0 for _ in range(len(nums))]
        final = 1
        for i in range(len(nums)):
            temp_max = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    temp_max = max(temp_max,result[j])
            result[i] = temp_max + 1
            final = max(final,result[i])
        return final