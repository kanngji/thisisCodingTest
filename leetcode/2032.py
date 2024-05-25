class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1

        for i in nums2:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1

        for i in nums3:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1

        ans = [k for k,v in dict1.items() if v >= 2]

        return ans 