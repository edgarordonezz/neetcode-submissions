class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # create a map to group things
        for s in strs: # for every word in the list
            sortedS = ''.join(sorted(s)) # sort the words and join them together
            groups[sortedS].append(s) # place words into their appropiate lists
        return list(groups.values()) # return groups in lists