class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # 세 변의 길이를 오름차순으로 정렬
        nums.sort()

        # 삼각형 부등식을 만족하는지 확인
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        # 세 변의 길이에 따라 삼각형의 종류를 판별
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"