# OX 퀴즈

def solution(quiz):
    answer = []
    
    for box in quiz:
        flag= True
        
        plusbox=[]
        minusbox=[]
        
        sep=box.split("=")
        # 공백으로 나누어주지 않으면 14를 14로 인식하는게아니라 1,4로 인식
        for i in list(sep[0].split()):
            if i=='-':
                flag=False
            
            elif i=='+':
                flag=True
            # 숫자가 들어갈때
            else:
                # 음수일때
                if flag==False:
                    minusbox.append(int(i))
                # 양수일때
                else:
                    plusbox.append(int(i))

        left=sum(plusbox)-sum(minusbox)
        # 공백제거
        right=sep[1].strip()
        right=int(right)

        if left==right:
            answer.append("O")
            
        else:
            answer.append("X")
           
    return answer