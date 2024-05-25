class Solution:
    def isFascinating(self, n: int) -> bool:
        step1 = n*2
        step2 = n*3

        res=str(n)+str(step1)+str(step2)

        if '0' in res or len(res) != 9:
            return False
        dict1 = dict()
        for i in res:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        for i in range(1,10):
            if str(i) not in dict1 or dict1[str(i)] != 1:
                return False
        return True
#dict1 딕셔너리의 키가 문자열이기 때문에 dict1[i]는 dict1[str(i)]로 접근          