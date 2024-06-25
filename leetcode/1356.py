class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 1의 개수를 세기 위한 함수
        def countBits(x):
            return bin(x).count('1')

        # 정렬: 1의 개수 우선, 같은 경우 숫자 자체 크기 우선
        arr.sort(key=lambda x: (countBits(x),x))

        return arr