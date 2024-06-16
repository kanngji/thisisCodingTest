class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            max = -1
            for j in range(i+1,len(arr)):
                if arr[j]>max:
                    max = arr[j]
            ans.append(max)
        return ans
    
# 시간초과,... 흠...
    
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n==0:
            return []
        
        max_from_right = -1

        for i in range(n-1,-1,-1):
            current = arr[i]
            arr[i] = max_from_right

            if current > max_from_right:
                max_from_right = current
        return arr 
    
