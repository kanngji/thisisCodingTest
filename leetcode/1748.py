class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique={}
        for i in nums:
            if i not in unique:
                unique[i]=0
            else:
                unique[i]+=1
        
        
        return sum([item[0] for item in unique.items() if item[1]==0])

# 리스트 컴프리헨션 if 어디다가 쓰는지.