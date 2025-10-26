class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []

        m = 0

        heights.append(0)

        for i in range(len(heights)):
            if not s:
                s.append((heights[i], i))
            else:
                start = i

                while s and s[len(s) - 1][0] >= heights[i]:
                    h, j = s.pop()
                    m = max(m, h * (i - j))
                    start = j

                s.append((heights[i], start))

        return m