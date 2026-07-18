class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, _ = stack.pop()
                res[j] = i-j
            stack.append((i, temp))
        
        return res