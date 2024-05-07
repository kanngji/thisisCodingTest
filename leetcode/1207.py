class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = dict()
        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        val_list = list(dict1.values())
        set_val_list = set(val_list)
        if len(val_list) == len(set_val_list):
            return True
        return False