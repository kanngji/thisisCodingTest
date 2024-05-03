class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        text = s.split()
        arr = []
        for i in text:
            if i.isdigit():
                arr.append(int(i))

        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                return False

        return True