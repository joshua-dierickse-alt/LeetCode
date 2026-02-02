def prettyPrint(l):
    return ["".join(e) for e in l]

def recursive_generation(c, start, end):
    c = c.copy()

    if start >= end:
        return [c]

    c[start] = "("

    filled_lists = []

    for i in range(int((end - start) / 2)):
        c[start + 1 + i * 2] = ")"

        bracket_lists = recursive_generation(c, start + 1, start + 1 + i * 2)

        for bracket_list in bracket_lists:
            filled_lists += recursive_generation(bracket_list, start + 2 + i * 2, end)

        c[start + 1 + i * 2] = "."

    return filled_lists



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # [(, 0, 0, 0, 0, 0]

        # [(, ), 0, 0, 0, 0]
        # [(, 0, 0, ), 0, 0]
        # [(, 0, 0, 0, 0, )]


        return prettyPrint(recursive_generation(["."] * n * 2, 0, n * 2))