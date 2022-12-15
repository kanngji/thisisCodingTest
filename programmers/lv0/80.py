def solution(spell, dic):
    answer = 2
    spellch=[0]*26
    dicch=[0]*26
    # spellch 배열에 한번 씩 넣기
    for i in spell:
        spellch[ord(i)-97]=1
    
    # dic 배열 검사하기
    for j in dic:
        for el in j:
            dicch[ord(el)-97]+=1
        
        if spellch==dicch:
            answer=1
            return answer
        # dic 배열 초기화
        dicch=[0]*26
            
    return answer
    