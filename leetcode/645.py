# 이거 sorted 해야 할거같음
# https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-04-02

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        dict1 = dict()

        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        
        arr = [0,0]

        for i in range(1,l+1):
            if i in dict1:
                if dict1[i]==2:
                    arr[0] = i
            else:
                arr[1] = i

        return arr
            
            