class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mp = {}
        maxf = 0
        res = 0
        for r in range(len(s)):
            char = s[r]
            mp[char] = mp.get(char, 0) + 1
            # get the most frequent element
            # for XYY, maxf = 2 YY
            maxf = max(maxf, mp[char])
            # 2 - 0 + 1 = 3 - 2 = 2 replacements available <= 2 yes
            if (r - l + 1) - maxf > k:
                mp[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
        return res