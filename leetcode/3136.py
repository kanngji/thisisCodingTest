class Solution:
    def isValid(self, word: str) -> bool:
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        const = {'b','B','c','C','d','D','f','F','g','G','h','j','J','k','K','l','L',
        'm','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z'}
        possible = {}

        if len(word) < 3:
            return False

        if word.isalnum() == False:
            return False
        mo = 0
        for i in word:
            if i in vowel:
                mo+=1
        if mo == 0:
            return False
        con = 0
        for i in word:
            if i in const:
                con +=1
        if con == 0:
            return False
        return True