class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0 
        for i in words:
            ans = ""
            for j in s:
                ans+=j
                if ans==i:
                    cnt+=1
        return cnt