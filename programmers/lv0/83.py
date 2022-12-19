def solution(score):
    answer = [1]*len(score)
    rank=[]
    for i in score:
        rank.append(i[0]+i[1])
    
    for i in range(len(rank)):
        for j in range(len(rank)):
            if rank[i]<rank[j]:
                answer[i]+=1
            
            
        
    return answer