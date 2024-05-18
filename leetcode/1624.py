class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dict1 = dict()

        for idx, val in enumerate(s):
            if val not in dict1:
                dict1[val] = [idx]
            else:
                dict1[val].append(idx)

        max_length = -1

        for indices in dict1.values():
            if len(indices) >= 2:
                # 최대 인덱스와 최소 인덱스 간의 거리를 계산
                max_length = max(max_length, indices[-1] - indices[0] - 1)

        return max_length
