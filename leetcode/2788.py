class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []

        for i in words:
            ans.append(i.split(separator))

        res =[]
        for i in ans:
            for j in i:
                if j=="":
                    continue
                else:
                    res.append(j)

        return res