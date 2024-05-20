class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        dict1 = dict()

        for i in arr1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] +=1

        for j in arr2:
            if j in dict1:
                for _ in range(dict1[j]):
                    ans.append(j)
        arr1 = sorted(arr1)

        for i in arr1:
            if i not in ans:
                for _ in range(dict1[i]):
                    ans.append(i)
        return ans