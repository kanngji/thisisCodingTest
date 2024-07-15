class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = []
        neg = []

        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)

        return max(len(pos),len(neg))