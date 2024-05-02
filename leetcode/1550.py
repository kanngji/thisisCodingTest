class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        ans=[]
        for i in arr:
            if i%2==1:
                ans.append(i)

                cnt+=1
                if cnt==3:
                    return True
            else:
                cnt=0
        
        return False