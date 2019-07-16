class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lens = 0
        for i in range(len(s), 0, -1):
            if s[i - 1] == ' ':
                return lens
            lens += 1
        return lens


print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("a"))
