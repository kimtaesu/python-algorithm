from typing import List


class Solution():
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged


if __name__ == '__main__':
    Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
