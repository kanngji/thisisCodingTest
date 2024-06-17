class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = [i%24 for i in hours]

        res = 0
        for i in range(len(ans)-1):
            for j in range(i+1,len(ans)):
                if (ans[i]+ans[j])%24==0:
                    res+=1
        return res