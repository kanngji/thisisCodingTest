class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict1 = dict()

        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1

        fre_val = sorted(dict1.values())
        fre_key = sorted(dict1.keys())

        if len(fre_key) ==1:
            return fre_val[-1]
        else:
            max_arr = max(fre_val)
            cnt = fre_val.count(max_arr)
            return cnt*max_arr