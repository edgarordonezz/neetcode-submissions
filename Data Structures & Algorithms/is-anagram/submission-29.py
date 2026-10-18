class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = {}
        setT = {}
        if len(s) != len(t):
            return False
        for c in s:
            setS[c] = setS.get(c, 0) + 1
        for c in t:
            setT[c] = setT.get(c, 0) + 1
        
        return setS == setT