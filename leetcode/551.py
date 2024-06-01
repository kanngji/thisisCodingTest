class Solution:
    def checkRecord(self, s: str) -> bool:
        ab_cnt = 0
        for i in s:
            if i == 'A':
                ab_cnt+=1
        
        if ab_cnt >=2:
            return False
        la_cnt = 0
        total_lates = 0
        for i in range(len(s)):
            # if total_lates > 3:
            #     return False
            if s[i]=='L':
                la_cnt+=1
                if la_cnt == 3:
                    return False
                total_lates+=1
            else:
                la_cnt=0

        return True