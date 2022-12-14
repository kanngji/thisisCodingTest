# 신규 아이디 추천
def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다
    new_id=new_id.lower()
    
    # 2단계 new_id 에서 알파벳 소문자, 숫자 , 빼기 ,밑줄, 마침표를 제외한 모든 문자를 제거
    # 정규식 공부해보기
    for c in new_id:
        if c.isalnum() or c in '-_.':
            answer+=c
    # 3단계 new_id 에서 .가 2번이상 연속된 부분을 하나의 마침표로 치환
    while '..' in answer:
        answer = answer.replace('..','.')
    
    # 4단계 new_id 에서 .가 처음이나 끝에 위치한다면 제거
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] =='.' else answer
    
    # 5단계 new_id 가 빈 문자열이라면 new_id에 'a'를 대입
    if answer =='':
        answer='a'
    
    # 6 단계 new_id의 길이가 16자 이상이라면 new_id의 첫 15개의 문자를 제외한 나머지
    # 문자들을 모두 제거합니다.
    if len(answer) >= 16:
        answer=answer[:15]
        # 만약 제거 후 . 가 new_id의 끝에 위치한다면 끝에 위치한 .문제를 제거합니다
        if answer[-1]=='.':
            answer=answer[:-1]
    
    # new_id의 길이가 2자 이하라면 new_id의 마지막 문자를 new_id의 길이가 3이 될때까지
    # 반복해서 붙입니다.
    
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    
    
    return answer

# 정규식 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
