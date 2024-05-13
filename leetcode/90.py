class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        dubbled = set() # 이미 들어간 조합을 기록

        for i in range(len(nums)+1):
            combs = list(combinations(nums,i))

            for comb in combs:
                sorted_comb = tuple(sorted(comb)) # 조합의 순서가 달라도 같은 조합
                if sorted_comb not in dubbled:
                    ans.append(list(sorted_comb))
                    dubbled.add(sorted_comb)
        return ans