class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        mp2 = {}

        for c in s:
            mp[c] = mp.get(c, 0) + 1
        
        for c in t:
            mp2[c] = mp2.get(c, 0) + 1

        return mp == mp2