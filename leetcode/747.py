class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        for i in nums:
            if i == max_num:
                continue
            else:
                if i*2>max_num:
                    return -1
        
        return nums.index(max_num)

# 배열 index 구하기
# 배열.index(max_num)