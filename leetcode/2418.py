class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict1={}
        for i in range(len(names)):
            dict1[names[i]]=heights[i]
        
        
        sorted_dict = sorted(dict1.items(), key=lambda item:item[1], reverse=True)
        return [item[0]for item in sorted_dict]
        

# 해쉬, 맵
# case1 은 통과 case2 동명이인은 실패.
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        dict_hn = {h:n for h,n in zip(heights,names)}

        dict_hn = sorted(dict_hn.items(),reverse=True,key=lambda x:x[0])

        ans = [value for key, value in dict_hn]

        return ans

# lambda 정렬 연습        
                

    