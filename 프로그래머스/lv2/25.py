

import re
def solution(s):
    # s가 문자열이니까 리스트로 변환하기
    s = re.sub('[{}]', '', s).split(',')
    s = list(map(int, s))

    dic = {n:0 for n in set(s)}
    # # 각 문자가 나온 횟수 카운트하기
    for n in s:
        dic[n] += 1
    
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return [k for k, v in dic]
#re의 sub를 이용해서 s 문자열에서 '{'와 '}'를 한 번에 없앤다. 그러면 숫자와 ','만 남을 텐데 ','를 기준으로 나누고 값을 int형으로 변환한다.

# https://velog.io/@minji0801/%EC%98%A4%EB%8B%B5%EB%85%B8%ED%8A%B8%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8A%9C%ED%94%8C
# 다음에 한번 더 보기