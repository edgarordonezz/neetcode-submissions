class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 2 ^ 4 = 2^2 + 2^2
        res = float(1)
        # when even, split n
        if n == 0:
            return res

        half = self.myPow(x, abs(n) // 2)
        if n % 2 == 0:
            res = half * half
        else:
            res = x * half * half
        if n < 0:
            res = 1 / res
        return res