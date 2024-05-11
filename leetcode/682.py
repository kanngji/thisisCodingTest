class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        pos = 0 # position
        while(pos < len(operations)):
            if operations[pos] != 'C' and operations[pos] != 'D' and operations[pos] != '+':
                stack.append(int(operations[pos]))
            elif operations[pos] == 'C':
                stack.pop()
            elif operations[pos] == 'D':
                stack.append(stack[-1]*2)
            elif operations[pos] == '+':
                stack.append(stack[-1] + stack[-2])
            pos += 1
        return sum(stack)
    
# ops = ["5","-2"]

# print(int(ops[1])) : -2 