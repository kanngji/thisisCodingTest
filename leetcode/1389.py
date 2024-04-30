class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        q = []

        for i , j in zip(nums,index):
            q.insert(j,i)

        return q 
    
#insert : 리스트.insert(입력할index, 값)