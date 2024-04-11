class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for i in accounts:
            sum = 0
            for j in i:
                sum+=j
            ans.append(sum)
        
        return max(ans)
    
    