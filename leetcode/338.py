class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            num = bin(i)
            num=str(num[2::])
            cnt=0
            for j in num:
                if j=='1':
                    cnt+=1
            ans.append(cnt)

        return ans
        