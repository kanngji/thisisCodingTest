class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_Arr = []
        negative_Arr = []
        ans = []
        for i in nums:
            if i>0:
                positive_Arr.append(i)
            else:
                negative_Arr.append(i)

        for i , j in zip(positive_Arr,negative_Arr):
            ans.append(i)
            ans.append(j)

        return ans