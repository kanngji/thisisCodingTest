class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maxWords=0
        for i in sentences:
            space=0

            for j in i:
                if j ==" ":
                    space+=1
            if space>=maxWords:
                maxWords=space
        return maxWords+1
            
        