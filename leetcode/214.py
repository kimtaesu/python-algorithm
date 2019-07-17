class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] != s[i]:
                i += 1
        if i == len(s):
            return s

        remain_rev = s[i:len(s)]
        remain_rev + self.shortestPalindrome(s[0:i] + s[i])
        print(remain_rev)


Solution().shortestPalindrome("aacecaaa")
