class Solution:
    def interpret(self, command: str) -> str:
        command=command.replace('()','o')
        command=command.replace('(al)','al')

        return command
        
# 문자열 치환 replace
# command=command.replace()
    
    