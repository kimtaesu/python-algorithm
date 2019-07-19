"""
[1,3,-1,-3,5,3,6,7]


Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if i >= k - 1:
                out += nums[d[0]],
        return out


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))


# public int[] maxSlidingWindow(int[] a, int k) {
# 		if (a == null || k <= 0) {
# 			return new int[0];
# 		}
# 		int n = a.length;
# 		int[] r = new int[n-k+1];
# 		int ri = 0;
# 		// store index
# 		Deque<Integer> q = new ArrayDeque<>();
# 		for (int i = 0; i < a.length; i++) {
# 			// remove numbers out of range k
# 			while (!q.isEmpty() && q.peek() < i - k + 1) {
# 				q.poll();
# 			}
# 			// remove smaller numbers in k range as they are useless
# 			while (!q.isEmpty() && a[q.peekLast()] < a[i]) {
# 				q.pollLast();
# 			}
# 			// q contains index... r contains content
# 			q.offer(i);
# 			if (i >= k - 1) {
# 				r[ri++] = a[q.peek()];
# 			}
# 		}
# 		return r;
# 	}
