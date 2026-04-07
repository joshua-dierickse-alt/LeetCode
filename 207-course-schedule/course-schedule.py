class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}

        for c1, c2 in prerequisites:
            if c1 == c2:
                return False
            g.setdefault(c2, set()).add(c1)

        v = [False] * numCourses
        s = [None] * numCourses
        e = [None] * numCourses

        t = [0]

        def dfs(c):
            v[c] = True

            s[c] = t[0]
            t[0] += 1

            if c in g:
                for nc in g[c]:
                    if v[nc] == False:
                        dfs(nc)

            e[c] = t[0]
            t[0] += 1

        for k in g:
            if not v[k]:
                dfs(k)

        for c1, c2 in prerequisites:
            if s[c1] < s[c2] and e[c2] < e[c1]:
                return False

        return True


        