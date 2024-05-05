class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word :
            return True
        
        if word.upper() == word:
            return True

        signal = False
        for i in range(len(word)):
            if i==0:
                if 65<=ord(word[i])<=90:
                    signal = True
            else:
                if 65<=ord(word[i])<=90:
                    signal = False
        return signal
            