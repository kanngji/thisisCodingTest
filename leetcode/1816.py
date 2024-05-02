class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split()

        ans = ""
        for i in range(k):
            if i == k-1:
                ans+=arr[i]
            else:
                ans+=arr[i]+" "

        return ans