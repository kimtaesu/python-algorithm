from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        formats = self.formWords(words)
        maxLen = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if formats[i] & formats[j] == 0:
                    maxLen = max(maxLen, len(words[i]) * len(words[j]))
        return maxLen

    def formWords(self, words):
        ints = []
        for word in words:
            int_word = 0
            for c in word:
                int_word |= 1 << (ord(c) - ord('a'))
            ints.append(int_word)
        return ints

print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))