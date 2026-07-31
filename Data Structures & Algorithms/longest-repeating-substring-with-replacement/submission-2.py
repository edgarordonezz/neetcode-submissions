class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # OPTIMAL SOLUTION
        mp = {} # O(n) space: Might have to scan the whole list
        max_freq = 0
        l = 0
        best = 0
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1 # get how many times we've seen the char
            max_freq = max(max_freq, mp[s[i]]) # whats the biggest count we've seen so far
            window_length = (i - l + 1)
            if window_length - max_freq > k: # if window needs more replacements than allowed, shrink window
                mp[s[l]] -= 1 # decrement the count of the character leaving from the left
                l += 1 # shrink window
            window_length = (i - l + 1) # recalculate window length after we shrunk
            best = max(best, window_length) # get the greatest window length  
        return best