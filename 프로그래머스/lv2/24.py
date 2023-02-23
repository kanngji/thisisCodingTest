# 전화번호 목록
# 나의 풀이 2번째 예 통과 x
def solution(phone_book):
    dict1={}
    
    
    for i in phone_book:
        dict1[i]=i
    
    for key,value in dict1.items():
        for j in phone_book:
            if j.count(dict1[key])>0:
                return False
            else:
                answer=True
    
    return answer

# 키값이랑 밸류 값을 그대로 준다음에 다시 phone_book에 for문으로 돌려서 문자열이니까 count함수쓰면
# 있으면 1 이상 나오니까 그떄는 false 주고 아니면 true줄라했는데 2번 사례에서 없는데대로 false를 준다...
# 여기서 막혓다

# 다른 사람풀이

def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map={}
    for phone_number in phone_book:
        hash_map[phone_number]=1
    
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo =""
        for number in phone_number:
            jubdoo+=number
            # 3. 접두어를 찾아야한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo !=phone_number:
                return False
    
    return True