class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for a in asteroids:
            while a < 0 and res and res[-1] > 0:
                diff = res[-1] - abs(a)
                if diff > 0:
                    a = 0
                elif diff == 0:
                    res.pop()
                    a = 0
                else:
                    res.pop()
            if a:
                res.append(a)
        
        return res