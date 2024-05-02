class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            res = []
            if len(str(i))==1:
                ans.append(i)
            elif len(str(i))!=1:
                for j in str(i):
                    res.append(int(j))

                maxnum = max(res)
                maxnum = str(maxnum)
                ans.append(maxnum*len(str(i)))
        ans = [int(i) for i in ans]
        return sum(ans)