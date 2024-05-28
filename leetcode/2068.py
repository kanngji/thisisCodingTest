from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        all_chars = set(counter1.keys()).union(set(counter2.keys()))

        for char in all_chars:
            if abs(counter1.get(char,0) - counter2.get(char,0)) > 3:
                return False
        return True