from enum import Enum

class State(Enum):
    FLAT = 1
    INCREASING = 2
    DECREASING = 3

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur = 1
        res = 1

        prev_state = State.FLAT

        def current_state(i):
            if nums[i - 1] == nums[i]:
                return State.FLAT
            elif nums[i - 1] < nums[i]:
                return State.INCREASING
            else:
                return State.DECREASING

        for i in range(1, len(nums)):
            cur_state = current_state(i)

            if cur_state == State.FLAT:
                res = max(res, cur)
                cur = 1
            elif cur_state == prev_state:
                cur += 1
                res = max(res, cur)
            else:
                res = max(res, cur)
                cur = 2

            prev_state = cur_state
        
        res = max(res, cur)
        
        return res