class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 가장 짧은 문자열의 길이
        min_length = min(len(s) for s in strs)

        # 각 문자열의 각 위치에서 첫 번째 문자열과 비교
        for i in range(min_length):
            # 현재 위치의 문자를 첫 번째 문자열의 문자와 비교
            current_char = strs[0][i]

            # 다른 문자열들의 현재 위치의 문자와 비교
            for string in strs:
                if string[i] != current_char:

                    return strs[0][:i]
        return strs[0][:min_length]
            
        