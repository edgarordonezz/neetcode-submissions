class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n 
        # pop while the top of the stack is cooler than today's temp
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cooler = stack.pop() # get the cooler day indes
                gap = i - cooler # current day index - cooler day index
                ans[cooler] = gap # assign gap difference to cooler day index so ans[0] = 1 for 30,38
            stack.append(i)
        return ans