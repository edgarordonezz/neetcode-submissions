class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s.lower():
                # Map the char to an index from 0 to 25
                index = ord(c) - ord('a')
                count[index] += 1
            key = tuple(count)
            res[key].append(s)
        
        return list(res.values())