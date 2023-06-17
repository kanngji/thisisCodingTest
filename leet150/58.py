class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        answer=0
        if not word:
            return 0
        
        return len(word[-1])