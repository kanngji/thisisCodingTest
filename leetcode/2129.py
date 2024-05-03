class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()

        ans = []
        title =title.split()

        for i in title:
            res =""
            for j in range(len(i)):
                if j ==0 and len(i)>2:
                    res+=i[j].upper()
                else:
                    res+=i[j]

            ans.append(res)
        
        ans = ' '.join(ans)
        return ans