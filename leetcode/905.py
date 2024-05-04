from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in nums:
            if i%2==0:
                even.append(i)
        
        for j in nums:
            if j%2==1:
                odd.append(j)

        return even+odd
        