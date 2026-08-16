class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation, same letters different orders
        mp = {}
        # get the count of letters in s1
        for s in s1:
            mp[s] = mp.get(s, 0) + 1

        window_counts = {} # create window dict
        window = s2[0: len(s1)]
        for w in window:
            window_counts[w] = window_counts.get(w, 0) + 1

        for i in range(1, len(s2) - len(s1) + 1):
            leaving = i - 1
            entering = i + len(s1) - 1
            if window_counts == mp:
                return True
            window_counts[s2[leaving]] -= 1
            if window_counts[s2[leaving]] == 0:
                del window_counts[s2[leaving]]
            window_counts[s2[entering]] = window_counts.get(s2[entering], 0) + 1
        # outside of window
        if window_counts == mp:
            return True
        return False