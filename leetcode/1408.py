class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in words:
                if words[i]==j:
                    continue
                else:
                    if words[i] in j:
                        ans.append(words[i])
        return set(ans)