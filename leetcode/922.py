from collections import deque
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        odd = sorted(odd)
        even = sorted(even)

        ans = []
        odd=deque(odd)
        even=deque(even)

        while odd and even:
            ans.append(even.popleft())
            ans.append(odd.popleft())

        if odd:
            ans.append(odd)
        
        if even:
            ans.append(even)

        return ans