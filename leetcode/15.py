from typing import List


class Solution:

    def solve(self, result: List[int], nums: List[int], i, l, r):
        if nums[i] == 0: return
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                r -= 1
                l += 1
            elif sum > 0:
                r -= 1
            else:
                l += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for n in range(len(nums)):
            self.solve(result, nums, n, n + 1, len(nums) - 1)

        print(result)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
