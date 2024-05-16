class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = dict()

        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        dict1 = list(sorted(dict1.items(), key=lambda item: (-item[1],item[0])))

        res = ''.join(item[0]*item[1] for item in dict1)
        return res