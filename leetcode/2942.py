class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(0,len(words)):
            for j in words[i]:
                if j==x:
                    ans.append(i)
                    break
                    

        return ans
    
# for문 break로 탈출
