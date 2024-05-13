class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dict1 = dict()

        for i in nums:
            if i not in dict1 and i%2==0:
                dict1[i]=1
            elif i in dict1 and i%2==0:
                dict1[i]+=1
        
        if len(dict1) == 0:
            return -1

        else:
            sorted_dict = list(sorted(dict1.items(), key=lambda item :(-item[1], item[0])))
            return sorted_dict[0][0]