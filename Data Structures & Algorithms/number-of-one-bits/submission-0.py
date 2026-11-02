class Solution:
    def hammingWeight(self, n: int) -> int:
        # 23 / 2 = 11 R 1
        # 11 / 2 = 5 R 1
        # 5 / 2 = 2 R 1
        # 2 / 2 = 1 R 0
        # 1 / 2 = 0 R 1
        # 10111
        count = 0
        while n > 0:
            count += n % 2
            n //=2
        return count