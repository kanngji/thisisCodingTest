class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1  # j의 초기값을 수정합니다.

        if len(s) == 1:
            return True

        while i < j:
            if not s[i].isalnum():  # isalpha()를 isalnum()으로 수정합니다.
                i += 1
                continue
            if not s[j].isalnum():  # isalpha()를 isalnum()으로 수정합니다.
                j -= 1
                continue
            if s[i].lower() != s[j].lower():  # 대소문자를 무시하기 위해 lower()를 사용합니다.
                return False

            i += 1
            j -= 1

        return True