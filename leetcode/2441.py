class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negative_arr=[]
        positive_arr=[]

        for i in nums:
            if i < 0:
                negative_arr.append(i)
            else:
                positive_arr.append(i)

        negative_arr = sorted(-1*x for x in negative_arr)

        max_num = -1
        for i in negative_arr:
            if i in positive_arr:
                max_num = max(max_num,i)

        return max_num
    
    