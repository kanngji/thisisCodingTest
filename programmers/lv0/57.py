def solution(cipher, code):
    answer = ''
    left=' '
    cipher=left+cipher
    for i in range(1,len(cipher)):
        
        if i%code==0:
            answer+=cipher[i]
    
    
            
            
            
    return answer