class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            cur=0
            for j in range(0,len(nums)):
                if i==j:
                    continue
                if nums[i]>nums[j]:
                    cur+=1
            ans.append(cur)
        return ans

# continue 로 i==j 일때는 넘어가기
#문제 nums인덱스의 값보다 작은 값들의 개수가 몇개 있는지 확인하는 문제   
