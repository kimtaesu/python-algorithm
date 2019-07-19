"""
[1,3,-1,-3,5,3,6,7]


Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for n in range(0, len(nums)):
            if k + n <= len(nums):
                result.append(max(nums[n:k + n]))
        return result


Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
