# 최빈값 구하기

def solution(array):
    # 카운터로는 dict 자료형을 많이 이용
    # list 보다 효율적이다 for문 다돌려서 list 확인안해도되니
    times_dict = {}
    for num in array:
        if num not in times_dict:
            times_dict[num] = 0 # key,value 값중 value 값에 0을 넣음
        times_dict[num]+=1 # 있으면 횟수 추가
    mode = float('-inf')
    mode_times = second_times = 0
    
    for key,value in times_dict.items(): # key,value 둘다 순회하려고 itmes() 사용
        if value > mode_times: # 횟수가 0보다크면
            mode = key # 최대값 비교 
            mode_times = value # value값 저장
        elif value == mode_times:
            second_times = value # 최빈값이 여러개이면
            
    
    return mode if mode_times != second_times else -1