class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        dict = {}

        i = 0
        for j in range(n):
            if s[j] in dict.keys():
                i = max(dict[s[j]], i)
            ans = max(ans, j - i + 1)
            dict.update({s[j]: j + 1})
        return ans


print(Solution().lengthOfLongestSubstring("pwwkew"))
