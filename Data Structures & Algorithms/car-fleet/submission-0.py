class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            curr = (target-p)/s
            if not stack or curr > stack[-1]:
                stack.append(curr)
        
        return len(stack)