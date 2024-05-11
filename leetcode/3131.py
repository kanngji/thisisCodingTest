class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        hap_nums1 = sum(nums1)
        hap_nums2 = sum(nums2)

        return (hap_nums2-hap_nums1) // len(nums1)
     
