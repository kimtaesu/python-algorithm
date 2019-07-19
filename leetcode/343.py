class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1

        if n == 4: return 4

        tmp = n
        sum = 1
        while tmp > 4:
            tmp -= 3
            sum *= 3

        return sum * tmp

print(Solution().integerBreak(10))
