from typing import List


class Solution:
    def count(self, n):
        return int((n * (n + 1)) / 2)

    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)

        candies = 0
        up = 0
        down = 0
        old_slope = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            else:
                if ratings[i] < ratings[i - 1]:
                    new_slope = -1
                else:
                    new_slope = 0

            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 and new_slope >= 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = 0
                down = 0
            if new_slope > 0:
                up += 1
            if new_slope < 0:
                down += 1
            if new_slope == 0:
                candies += 1
            old_slope = new_slope
        candies += self.count(up) + self.count(down) + max(up, down) + 1
        return candies


print(Solution().candy([1,0,2]))

# public class Solution {
#     public int count(int n) {
#         return (n * (n + 1)) / 2;
#     }
#     public int candy(int[] ratings) {
#         if (ratings.length <= 1) {
#             return ratings.length;
#         }
#         int candies = 0;
#         int up = 0;
#         int down = 0;
#         int old_slope = 0;
#         for (int i = 1; i < ratings.length; i++) {
#             int new_slope = (ratings[i] > ratings[i - 1]) ? 1 : (ratings[i] < ratings[i - 1] ? -1 : 0);
#             if ((old_slope > 0 && new_slope == 0) || (old_slope < 0 && new_slope >= 0)) {
#                 candies += count(up) + count(down) + Math.max(up, down);
#                 up = 0;
#                 down = 0;
#             }
#             if (new_slope > 0)
#                 up++;
#             if (new_slope < 0)
#                 down++;
#             if (new_slope == 0)
#                 candies++;
#
#             old_slope = new_slope;
#         }
#         candies += count(up) + count(down) + Math.max(up, down) + 1;
#         return candies;
#     }
# }
