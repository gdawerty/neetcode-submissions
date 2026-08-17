class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]

        pairs.sort(reverse = True)
        print(pairs)
        stack = []

        for position, speed in pairs:
            time = (target - position) / speed

            if not stack or time > stack[-1]:
                stack.append(time)


        return len(stack)