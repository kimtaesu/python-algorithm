from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # The number of jumps needed to reach the starting index is 0
        if n <= 1:
            return 0

        # Return -1 if not possible to jump
        if nums[0] == 0:
            return -1

        # initialization
        # stores all time the maximal reachable index in the array
        maxReach = nums[0]
        # stores the amount of steps we can still take
        step = nums[0]
        # stores the amount of jumps necessary to reach that maximal reachable position
        jump = 1

        # Start traversing array
        for i in range(1, n):
            # Check if we have reached the end of the array
            # 먼저 배열의 끝에 도달했는지 여부를 테스트합니다.이 경우 점프 변수를 반환하면됩니다.
            if i == n - 1:
                return jump

                # updating maxReach
            # 다음으로 maxReach를 업데이트합니다. 이것은 maxReach와 i + arr [i] (현재 위치에서 취할 수있는 단계의 수)의 최대 값과 같습니다.
            maxReach = max(maxReach, i + nums[i])

            # we use a step to get to the current index
            # 현재 색인으로 이동하기 위해 단계를 밟았으므로 단계를 줄여야합니다.
            step -= 1

            # If no further steps left
            if step == 0:
                print("step == 0")
                """
                단계가 더 이상 남아 있지 않으면 (예 : steps = 0이면 점프를 사용해야합니다. 따라서 점프를 증가시켜야합니다.)
    어떻게 든 maxReach에 도달 할 수 있다는 것을 알고 있으므로 maxReach에 도달하는 단계 수로 단계를 다시 초기화합니다.
    위치 i. 그러나 다시 초기화 단계 전에 단계가 0 또는 음수가되는지 여부도 확인합니다.이 경우 더 이상 도달 할 수 없습니다.
                """
                # we must have used a jump
                jump += 1

                # Check if the current index/position or lesser index
                # is the maximum reach point from the previous indexes
                if i >= maxReach:
                    return -1

                # re-initialize the steps to the amount
                # of steps to reach maxReach from position i.
                step = maxReach - i
        return -1


print(Solution().jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
