class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = [] 
        for i in range(m):
            tar = []
            for j in range(n):
                tar.append(original[i*n+j])
            ans.append(tar)

        return ans