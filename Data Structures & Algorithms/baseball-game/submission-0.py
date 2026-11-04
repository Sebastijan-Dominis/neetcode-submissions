class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for o in operations:
            if o == "C":
                scores.pop()
            elif o == "D":
                scores.append(scores[-1]*2)
            elif o == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(o))
        
        res = 0
        for s in scores:
            res += s
        return res