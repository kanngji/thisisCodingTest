class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = []
        for i in letters:
            if ord(i)> ord(target):
                ans.append(i)

        if len(ans) == 0:
            return letters[0]
        else:
            return min(ans)