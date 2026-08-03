class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute force solution
        mp = {} 

        for c in t:
            mp[c] = mp.get(c, 0) + 1

        best = ""
        for i in range(len(s)):
            window = {}
            for j in range(i, len(s)):
                window_len = (j - i + 1)
                # once we find a valid substring, we shorten it as long as its valid
                window[s[j]] = window.get(s[j], 0) + 1

                valid = True
                for char in mp:
                    if window.get(char, 0) < mp[char]:
                        valid = False 
                        break
                if valid:
                    if best == "" or window_len < len(best):
                        best = s[i:j+1]
        return best