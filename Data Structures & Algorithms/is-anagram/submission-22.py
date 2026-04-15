class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        my_mapS = {}
        my_mapT = {}
        for c in s:
            my_mapS[c] = my_mapS.get(c, 0) + 1
        for c in t:
            my_mapT[c] = my_mapT.get(c, 0) + 1
        return my_mapS == my_mapT

