class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        m = {}

        for i in range(len(nums)):
            m[nums[i]] = m.get(nums[i], 0) + 1

        sorted_keys = sorted(m.keys())

        dp = [None] * (k + 1)
        dp[0] = (0, 0)

        dp_len = len(dp)
        sorted_keys_len = len(sorted_keys)

        for i in range(sorted_keys_len):
            key = sorted_keys[i]
            for j in range(key, dp_len):
                prev = dp[j - key]
                if prev is not None and dp[j] is None:
                    if prev[0] == key:
                        if prev[1] < m[key]:
                            dp[j] = (key, prev[1] + 1)
                    else:
                        dp[j] = (key, 1)
        
        f = []

        num_x = 0
        p = sorted_keys_len - 1

        for x in range(len(nums), 0, -1):
            found = False
            for i in range(num_x + 1):
                if 0 > dp_len - (i * x) - 1:
                    break
                if dp[dp_len - (i * x) - 1] is not None and dp[dp_len - (i * x) - 1][0] <= x:
                    found = True
                    break
            f.append(found)

            if p >= 0 and x == sorted_keys[p]:
                num_x += m[sorted_keys[p]]
                p -= 1

        f.reverse()
        return f
