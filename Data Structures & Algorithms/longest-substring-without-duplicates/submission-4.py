class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        length = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            length = i - l + 1
            longest = max(longest, length)
        return longest