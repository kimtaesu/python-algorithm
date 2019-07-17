class Solution:
    def shortestPalindrome(self, s: str) -> str:

        result = []
        front = 0
        for i in range(len(s) - 1, 0, -1):
            if s[front] == s[i]:
                result.ad
                continue
            else:
                s[front]
                front += 1
            front += 1


Solution().shortestPalindrome("aacecaaa")
