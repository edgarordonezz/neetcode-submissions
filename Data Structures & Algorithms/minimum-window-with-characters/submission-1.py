class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = {} 
        # get the frequency of the letters in t
        for char in t: 
            mp[char] = mp.get(char, 0) + 1 

        window = {}
        have = 0 # make sure we have the same letters
        need_count = len(mp)
        left = 0 
        best = ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1 
            # if char is one we actually need, and we now have exacly enough of it in our window, then increment have  
            
            if char in mp and window[char] == mp[char]: 
                have += 1
            while have == need_count:
                window_len = (right - left + 1)
                if best == "" or window_len < len(best):
                    best = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in mp and window[left_char] < mp[left_char]:
                    have -= 1
                left += 1 
        return best