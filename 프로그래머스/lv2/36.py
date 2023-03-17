# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list=list(skill)
        for s in skills:
            if s in skill:
                if s!=skill_list.pop(0):
                    break
        else:
            answer+=1
    return answer

# https://eda-ai-lab.tistory.com/460 다시 한번 풀기
