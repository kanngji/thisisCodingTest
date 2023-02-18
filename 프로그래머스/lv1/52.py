# 둘만의 암호

def solution(s, skip, index):
    answer = ''
    skip_dict=dict()
    # skip 에 있는거 값은 다 true로
    # ord(a)=97
    for skip_case in skip:
        skip_dict[ord(skip_case)]=True
        
    for j in s:
        word=ord(j)
        cnt=0
        while cnt<index:
            word+=1
            if word>ord('z'):
                word=ord('a')
            if skip_dict.get(word):
                continue
            else:
                cnt+=1
        answer+=chr(word)    
        
            
            
    return answer