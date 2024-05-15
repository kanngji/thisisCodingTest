class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict1 = dict()

        for i in sentence:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        
        if len(dict1)==26:
            return True
        
        return False