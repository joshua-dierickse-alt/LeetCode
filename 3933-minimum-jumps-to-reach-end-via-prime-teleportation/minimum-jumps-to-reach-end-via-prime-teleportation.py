from collections import deque, defaultdict

spf = [i for i in range(10 ** 6 + 1)]

for i in range(2, int(len(spf) ** 0.5) + 3):
    if spf[i] == i:
        for j in range(i + i, len(spf), i):
            if spf[j] == j:
                spf[j] = i
    
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        def add_element(i):
            if i == len(nums) - 1:
                raise ValueError()
            if 0 <= i and v[i] == False:
                q.append(i)
                v[i] = True

        def factorize(i):
            f = set()
            while i > 1:
                f.add(spf[i])
                i //= spf[i]
            return f

        if len(nums) <= 1:
            return 0

        factor_to_nums = defaultdict(list)
        num_to_indexs = defaultdict(list)

        for i in range(len(nums)):
            num_to_indexs[nums[i]].append(i)
            for factor in factorize(nums[i]):
                factor_to_nums[factor].append(nums[i])
            

        q = deque([0])
        v = [False] * len(nums)
        v[0] = True

        c = 1

        try:
            while q:
                for _ in range(len(q)):
                    f = q.popleft()
                    cp = nums[f]

                    add_element(f - 1)
                    add_element(f + 1)

                    if spf[cp] == cp and cp in factor_to_nums:
                        for num in factor_to_nums[cp]:
                            if num in num_to_indexs:
                                for index in num_to_indexs[num]:
                                    add_element(index)
                                del num_to_indexs[num] 
                        del factor_to_nums[cp]

                c += 1
        except:
            return c