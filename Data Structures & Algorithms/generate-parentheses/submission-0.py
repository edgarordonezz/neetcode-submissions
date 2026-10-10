class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack(countOpen, countClose):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            if countOpen < n:
                path.append("(")
                backtrack(countOpen + 1, countClose)
                path.pop()

            if countClose < countOpen:
                path.append(")")
                backtrack(countOpen, countClose + 1)
                path.pop()
    
        backtrack(0, 0)
        return res