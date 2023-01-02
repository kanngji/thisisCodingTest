# 폰켓몬

def solution(nums):
    answer = 0
    target=len(nums)//2
    nums=list(set(nums))
    
    if target>= len(nums):
        answer = len(nums)
    else:
        answer = target
    return answer

# n/2 >= 중복제가 허가 nums의 길이이면 중복제거 nums의 길이가 답
# 아니면 n/2 가 답
