class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        mp = {}
        l = 0
        for i in range(len(s)):
            char = s[i]
            # if char is in map, remove key and increment window from left
            while char in mp:
                del mp[s[l]]
                l += 1
            if char not in mp:
                mp[char] = mp.get(char, 0) + 1
                longest = max(longest, len(mp))
            
        return longest