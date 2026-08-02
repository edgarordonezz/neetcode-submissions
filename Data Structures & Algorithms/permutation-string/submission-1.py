class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Optimal Solution
        n = len(s1) # this will be our window size
        m = len(s2) # length of s2
        mp = {}
        
        for s in s1:
            mp[s] = mp.get(s, 0) + 1

        mp2 = {} # create our substring frequency map
        # get s2 frequency
        substring = s2[0:n]
        for s in substring:
                mp2[s] = mp2.get(s, 0) + 1
        # check if permutation exists from 0-n
        if mp2 == mp:
            return True
        # loop to update our window
        # start at 0 since we checked 0 up above ^^
        for i in range(1, m - n + 1):
            l = s2[i - 1]
            r = s2[i + n - 1]
            mp2[l] = mp2.get(l, 0) - 1 # shrink window from left side
            # if value of key is 0, we remove so that mp = mp2 doesnt get confused
            if mp2[l] == 0:
                del mp2[l]
            mp2[r] = mp2.get(r, 0) + 1 # grow window from right side
            if mp2 == mp:
                return True
        return False