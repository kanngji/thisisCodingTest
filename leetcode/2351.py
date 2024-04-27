class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict1 = dict()

        for i in s:
            # <조심>
            if i in dict1 and dict1[i]==1:
                return i

            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1 