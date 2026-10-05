from collections import defaultdict

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = defaultdict(lambda: 0)

        depth = 0

        for c in s:
            if c == "(":
                depth += 1
            else:
                if stack[depth] > 0:
                    stack[depth - 1] += 2 * stack[depth]
                    stack[depth] = 0
                else:
                    stack[depth - 1] += 1
                depth -= 1

        return stack[0]
        