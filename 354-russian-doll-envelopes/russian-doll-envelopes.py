from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()

        n = 0
        i = 0

        while i < len(envelopes):
            prev_x = envelopes[i][0]
            j = 0
            last_index = -1
            updates = []

            while i + j < len(envelopes) and prev_x == envelopes[i + j][0]:
                update_index = bisect_left(envelopes, envelopes[i + j][1], 0, n)
                if update_index != last_index:
                    last_index = update_index
                    updates.append((update_index, envelopes[i + j][1]))

                j += 1

            for [update_index, value] in updates:
                if update_index >= n:
                    n += 1
                envelopes[update_index] = value

            i += j
            
        return n
            