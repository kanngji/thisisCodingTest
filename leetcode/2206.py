class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = len(nums)//2

        dict1= dict()

        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        hap = 0
        for k,v in dict1.items():
            if v>=2:
                hap+=v
            if v>=2 and v%2==1:
                return False

        hap//=2

        return hap == res