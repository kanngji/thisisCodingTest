class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        nums.sort(reverse=True)

        while(k>min(nums)):
            nums.pop()
            cnt+=1
        
        return cnt