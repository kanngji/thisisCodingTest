def solution(before, after):
 
    beforelist=[0]*26
    afterlist=[0]*26
    for i in range(len(before)):
        beforelist[ord(before[i])-97]+=1
    for j in range(len(after)):
        afterlist[ord(after[j])-97]+=1
    
    if beforelist==afterlist:
        answer = 1
    else:
        answer =0
        
    return answer