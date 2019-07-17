from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(result, nums, 0)
        return result

    def dfs(self, result, nums, j):
        if j == len(nums):
            result.append(nums[:])
            return

        for i in range(j, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(result, nums, j + 1)
            nums[i], nums[j] = nums[j], nums[i]


print(Solution().permute([1, 2, 3]))
