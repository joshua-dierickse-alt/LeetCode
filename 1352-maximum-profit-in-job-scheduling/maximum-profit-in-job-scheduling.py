class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        s = []

        for i in range(len(startTime)):
            s.append((startTime[i], endTime[i], profit[i]))

        s.sort(key=lambda x: x[1])

        dp = [[0, 0]]
        ends = [0]

        for start, end, p in s:
            idx = bisect.bisect_right(ends, start) - 1

            last_end, last_p = dp[len(dp) - 1]

            if last_end == end:
                dp[len(dp) - 1][1] = max(dp[len(dp) - 1][1], dp[idx][1] + p)
            else:
                if last_p < dp[idx][1] + p:
                    dp.append([end, dp[idx][1] + p])
                    ends.append(end)

        return dp[len(dp) - 1][1]
            
                



        