class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 =dict()
        dict2 =dict()
        dict3 = dict()

        for i in words1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in words2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        
        for i in dict1:
            if dict1[i] == 1 and i not in dict3:
                dict3[i] = 1
        
        for i in dict2:
            if dict2[i] ==1 and i in dict3:
                dict3[i] += 1
        
        ans = 0

        for k in dict3.keys():
            if dict3[k] == 2:
                ans+=1

        return ans
    
# ... 머쓱...
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0

        for i in words1:
            if words1.count(i)==1 and words2.count(i)==1:
                count=count+1

        return count