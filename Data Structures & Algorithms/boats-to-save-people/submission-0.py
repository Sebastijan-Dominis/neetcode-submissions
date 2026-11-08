class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        l, r = 0, len(people) - 1

        while l <= r:
            boats += 1
            remain = limit - people[r]
            r -= 1
            if l <= r and people[l] <= remain:
                l += 1

        return boats