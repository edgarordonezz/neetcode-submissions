class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # check if we've seen char
        length = 0
        longest = 0
        l = 0 # the way we shrink our window
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            length = i - l + 1
            seen.add(s[i])
            longest = max(longest, length)
        return longest