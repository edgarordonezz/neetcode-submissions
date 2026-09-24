class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        freq = {}
        for i in range(len(s)):
            length = 0
            # while current is in our map, update left pointer and remove curr
            while s[i] in freq:
                del freq[s[left]]
                left += 1
            # else add it to freq
            freq[s[i]] = freq.get(s[i], 0) + 1
            length = i - left + 1
            longest = max(longest, length)
        return longest