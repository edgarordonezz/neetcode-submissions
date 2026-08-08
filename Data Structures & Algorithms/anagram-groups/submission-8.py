class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # same characters but order can be different
        # will use hashmap's for counting the values
        res = defaultdict(list)
        for s in strs:
            mp = {}
            for c in s:
                mp[c] = mp.get(c, 0) + 1 # get the frequency of each letter
            key = tuple(sorted(mp.items())) # create a key so we can append
            res[key].append(s)
        return list(res.values())