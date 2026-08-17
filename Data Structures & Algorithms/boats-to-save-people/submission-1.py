class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        at_limit = 0
        people = sorted(people)
        l = 0
        r = len(people) - 1
        first = True
        total = 0

        while l < r:
            if people[l] + people[r] > limit:
                r-=1
            else:
                if first:
                    at_limit = r
                    first = False
                total+=1
                r-=1
                l+=1

        total += len(people) - 1 - at_limit
        if (at_limit + 1) % 2 == 1:
            return total + 1
        else:
            return total
