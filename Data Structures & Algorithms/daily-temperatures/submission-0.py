class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):

            # stack[-1] is temperatures[0] on second pass
            # stack[-1] is temperatures[1] on third pass
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # First pass: Fails immedialty on first pass, nothing happens
                # Second pass: 30 > 0
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
            # stack = # [,0,0,0,0,0]
        return res
