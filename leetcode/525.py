class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict1 = dict()

        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] +=1
        
        if dict1[1] and dict1[0]:
            num1 = dict1[1]
            num0 = dict1[0]

            min_num = min(num1,num0)

            return min_num*2

        else:
            return 0
# 문제이해가 안되는데...
        