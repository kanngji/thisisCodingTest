class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1=dict()
        for i in s:
            if i not in dict1:
                dict1[i]=0
            else:
                dict1[i]+=1
        
        my_list = list(dict1.values())
        for i in range(0,len(my_list)):
            for j in range(i+1,len(my_list)):
                if my_list[j]!=my_list[i]:
                    return False
        
        return True
        
# 단순 비교인데 더 나은 방법을 찾아보자
    
# class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # going to try this one with my understanding of hash maps to see where I get
        character_count = {}
        for c in s:
            if c in character_count:
                character_count[c] += 1 
            else:
                character_count[c] = 1
        #  {a:2, b:1}
        value_set = set(character_count.values())
        if len(value_set) == 1:
            return True
        else:
            return False
# set 은 중복을 허락하지 않아서 굿굿굿
        