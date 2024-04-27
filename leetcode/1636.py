class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict1=dict()
        ans=[]
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
            
        sorted_dict = sorted(dict1.items(), key=lambda x:(x[1],-x[0]))
        for i in sorted_dict:
            for _ in range(i[1]):
                ans.append(i[0])

        return ans
    
# sorted_dict x[0] 일때 내림차순 하려면 - 붙이기
    # 첫번째로 x[1] 빈도 -> x[0] 값 (내림차순)