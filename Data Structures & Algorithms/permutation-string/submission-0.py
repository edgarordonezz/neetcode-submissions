class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force solution
        sorted1 = "".join(sorted(s1))
        # Get the correct range
        # len(s2) = m, len(s1) = n
        # window = len(s1)
        n = len(s1)
        m = len(s2)
        for i in range(m - n + 1):
            substring = s2[i: i + n]
            sorted_sub = "".join(sorted(substring))
            if sorted_sub == sorted1:
                return True
        return False