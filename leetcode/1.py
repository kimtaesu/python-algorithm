from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict.keys():
                return [dict[complement], i]
            dict[nums[i]] = i


print(Solution().twoSum([3, 2, 4], 6))
