class Solution:
    def secondHighest(self, s: str) -> int:
        ans = set()
        for i in s:
            if i.isdigit():
                ans.add(int(i))
        
        ans=list(ans)
        ans.sort()

        if len(ans)<2:
            return -1
        else:
            return ans[-2]