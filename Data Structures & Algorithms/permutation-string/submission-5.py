class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2) - n
        # loop from last element we need to check is len(s2) - len(s1)
        freq = {}
        window_freq = {}
        for s in s1:
            freq[s] = freq.get(s, 0) + 1
        for s in s2[0: n]:
            window_freq[s] = window_freq.get(s, 0) + 1

        if window_freq == freq:
            return True
        
        for i in range(1, m + 1):
            leaving = s2[i - 1]
            entering = s2[i + n - 1]
            window_freq[leaving] -= 1
            if window_freq[leaving] == 0:
                del window_freq[leaving]
            window_freq[entering] = window_freq.get(entering, 0) + 1

            if window_freq == freq:
                return True
        return False