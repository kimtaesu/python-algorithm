from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)
        curr = []
        nums.sort()
        self.dfs(result, visited, curr, nums)

        return result

    def dfs(self, result, visited, curr, nums):
        if len(curr) == len(nums):
            result.append(curr[:])
            return

        for i in range(len(nums)):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            curr.append(nums[i])
            self.dfs(result, visited, curr, nums)
            visited[i] = False
            curr.pop()


print(Solution().permuteUnique([1, 1, 2]))
