def isDigit(v):
    [a, b] = v.split(" ", 1)
    return ord('0') <= ord(b[0]) <= ord('9')

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = []
        d = []

        for i in range(len(logs)):
            if isDigit(logs[i]):
                d.append(logs[i])
            else:
                [a, b] = logs[i].split(" ", 1)
                l.append((b, a))

        l = sorted(l, key=lambda x: (x[0], x[1]))

        for i in range(len(l)):
            l[i] = l[i][1] + " " + l[i][0]
        
        return l + d