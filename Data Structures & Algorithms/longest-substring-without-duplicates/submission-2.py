class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_seen = {}
        max_len = 0
        left = 0
        
        # iterate through string
        for right in range(len(s)):
            if s[right] in last_seen: # if letter exists in our map
                left = max(last_seen[s[right]] + 1, left) 

            length = right - left + 1
            last_seen[s[right]] = right
            max_len = max(max_len, length)
        return max_len