class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        signal = False

        for i in range(len(word)):
            if word[i]==ch and signal==False:
                ans+=word[i]
                ans=ans[::-1]
                signal=True
            else:
                ans+=word[i]

    
        return ans