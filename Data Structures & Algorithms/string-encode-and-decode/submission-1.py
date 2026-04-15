class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_str = s[i:j]
            length = int(length_str)
            word_str = s[j+1:j+1+length] # for 5#hello j+1 is at 2 and length is at 5 so 2 + 7 
                                         # word_str starts at index 2, and ends at index 7
            result.append(word_str)
            i = j+1+length
        return result
