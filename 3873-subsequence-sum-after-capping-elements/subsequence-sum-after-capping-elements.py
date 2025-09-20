class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        m = {}

        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        sorted_keys = []

        for key in m.keys():
            sorted_keys.append(key)

        sorted_keys.sort()

        dp = [None] * (k + 1)

        dp[0] = (0, 0)

        for i in range(len(sorted_keys)):
            for j in range(sorted_keys[i], len(dp)):
                if dp[j - sorted_keys[i]] != None and dp[j] == None:
                    if dp[j - sorted_keys[i]][0] == sorted_keys[i]:
                        if dp[j - sorted_keys[i]][1] < m[sorted_keys[i]]:
                            dp[j] = (sorted_keys[i], dp[j - sorted_keys[i]][1] + 1)
                    else:
                        dp[j] = (sorted_keys[i], 1)
        
        f = []

        num_x = 0
        p = len(sorted_keys) - 1


        for x in range(len(nums), 0, -1):
            found = False
            for i in range(num_x + 1):
                if 0 > len(dp) - (i * x) - 1:
                    break
                if dp[len(dp) - (i * x) - 1] != None and dp[len(dp) - (i * x) - 1][0] <= x:
                    found = True
                    break
            f.append(found)

            if p >= 0 and x == sorted_keys[p]:
                num_x += m[sorted_keys[p]]
                p -= 1

        f.reverse()
        return f