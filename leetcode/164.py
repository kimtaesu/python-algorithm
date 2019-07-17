from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort() # O(n log n)
        maximum = 0
        for i in range(1, len(nums)):
            maximum = max(nums[i] - (nums[i -1]), maximum)


        return maximum
print(Solution().maximumGap([3,6,9,1, 15]))