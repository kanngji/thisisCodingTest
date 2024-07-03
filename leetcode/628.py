class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        combinations = list(itertools.combinations(nums,3))

        max_value = float('-inf')

        for comb in combinations:
            f = 1
            for i in comb:
                f = f*i
            if f>max_value:
                max_value = f
        return max_value
# Memory Limit Exceeded
    
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l1 = nums[-1]*nums[-2]*nums[-3]
        l2 = nums[0]*nums[1]*nums[-1]
        return max(l1,l2)
# l1은 양수 3개 가정 하고 l2는 음수2개 양수 1개 가정한건가?