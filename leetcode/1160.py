from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= chars_count[c] for c in word_count):
                total_length += len(word)
        
        return total_length

#all은 파이썬 내장 함수로, 주어진 iterable(반복 가능한 객체)의 모든 요소가 True인지 확인합니다. 
    #만약 모든 요소가 True이면 all 함수는 True를 반환하고, 하나라도 False가 있으면 False를 반환합니다.
    