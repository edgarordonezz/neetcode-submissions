class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # time formula = (target - positioin) / speed 
        paired = list(zip(position, speed))
        sort = sorted(paired, reverse=True)
        stack = []
        for pos, spd in sort:
            time = (target - pos) / spd
            # if stack is empty or current time > previous time
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
            