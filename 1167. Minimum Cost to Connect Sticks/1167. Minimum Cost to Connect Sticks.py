"""
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int: 
        if len(sticks) == 1:
            return 0
        min_cost,temp_cost = 0,0
        heapq.heapify(sticks)
        x,y = 0,0
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            temp_cost = x + y
            min_cost += temp_cost
            heapq.heappush(sticks,temp_cost)
        return min_cost