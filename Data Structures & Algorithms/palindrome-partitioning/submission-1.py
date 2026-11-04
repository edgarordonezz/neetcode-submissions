class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, path):
            if start == len(s): # once start = len(s), we're done
                res.append(path[:])
                return
            for i in range(start, len(s)):
                sub = s[start: i + 1] # create the substring
                backwards = sub[::-1] # create the substring backwards
                if sub == backwards: # check if theyre palindromes
                    path.append(sub) # append it
                    backtrack(i + 1, path) # explore the rest
                    path.pop() # un choose
        backtrack(0, [])
        return res