class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans=""
        for i in words:
            j=0
            ans+=i[j]
        return ans==s
            
        