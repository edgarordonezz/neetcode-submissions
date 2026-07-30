class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force Solution
        max_len = 0
        for i in range(len(s)): # try every starting index
            seen = set()
            for j in range(i, len(s)): # extend forward from i
                if s[j] in seen: # if letter in set, means it's duplicate, max_len is seen
                    break # break
                else:
                    seen.add(s[j]) # else letter not in set, add to set
            max_len = max(max_len, len(seen))
        return max_len