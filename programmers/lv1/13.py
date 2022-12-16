def solution(s):
    answer = ''
    mid = len(s)
    if mid%2==1:
        answer=s[mid//2]
    else:
        answer+=s[mid//2-1]
        answer+=s[mid//2]
    return answer