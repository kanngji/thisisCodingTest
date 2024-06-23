class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        paragraph = paragraph.lower()

        for i in symbols:
            paragraph = paragraph.split(i)
            paragraph = " ".join(paragraph)

        p = paragraph.split()

        dict1 = dict()

        for i in p:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        
        for i in banned:
            if i in dict1:
                del dict1[i]
        
        max_val = max(dict1.values())
        max_key = [k for k,v in dict1.items() if v==max_val]

        return ''.join(max_key)