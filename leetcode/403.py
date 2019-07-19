class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        target, stones, memo = stones[-1], set(stones), set()
        return self.backtrack(stones, 1, 1, target, memo)

    def backtrack(self, stones, pos, jump, target, memo):
        if (pos, jump) in memo:
            return False
        if pos == target:
            return True
        if jump <= 0 or pos not in stones:
            return False
        print(jump, pos, memo)
        for j in (jump - 1, jump, jump + 1):
            if self.backtrack(stones, pos + j, j, target, memo):
                return True
        memo.add((pos, jump))  # record bad position and jump
        return False

print(Solution().canCross([0,1,3,5,6,8,12,17]))
# print(Solution().canCross([0,1,2,3,4,8,9,11]))