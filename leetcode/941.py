class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # 배열의 처음 부터 증가 하는 부분
        while i + 1 < n and arr[i] < arr[i+1]:
            i+=1

        # 최고점이 배열의 시작이나 끝이라면 false
        if i == 0 or i == n -1:
            return False

        # 최고점에서 배열이 감소하는지 확인
        while i + 1 < n and arr[i] > arr[i+1]:
            i+=1

        return i == n - 1