# 대충 만든 자판
def solution(keymap, targets):
    answer = []
    dict1={}
    for i in keymap:
        for j in i:
            dict1[j]=i.index(j)+1
    for i in targets:
        score=0
        for j in i:
            if j in dict1:
                score+=dict1[j]
            else:
                answer.append(-1)
        if score!=0:
            answer.append(score)
    
    return answer

# 연습 tc는 다 통과 채점은 fail

def solution(keymap, targets):
    keytable = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1)

    result = []
    for target in targets:
        clicked = 0
        for key in target:
            if key not in keytable:
                clicked = -1
                break
            clicked += keytable[key]
        result.append(clicked)

    return result