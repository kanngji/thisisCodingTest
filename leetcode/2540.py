class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = list(s1&s2)
        s3.sort()
        if len(s3) == 0:
            return -1
        else:
            return s3[0]

# 아이디어 => set , 교집합을 써서 중복 요소를 찾은 후
# 정렬후 0번 인덱스값 리턴


        

    
