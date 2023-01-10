# 로그인 성공?
def solution(id_pw, db):
    answer = 'fail'
    # 아이디와 비밀번호가 같으면
    if id_pw in db:
        answer='login'
        return answer
    # 아이디는 있는데 비밀번호가 틀려요
    for i in db:
        if id_pw[0]==i[0] and id_pw[1]!=i[1]:
            answer="wrong pw"
        
            
    return answer