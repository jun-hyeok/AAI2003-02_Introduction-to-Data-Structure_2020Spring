#후위표기법 수식 계산 함수 
from slstack import Stack

def postfix_evaluation(string):
    s = Stack()
    for i in string:
        if i not in "*/+-":
            s.push(int(i))
        else:
            operand2 = s.pop()
            operand1 = s.pop()
            result = compute(i, operand1, operand2)
            s.push(result)
    result = s.pop()
    return result

def compute(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ == "__main__":
    print(postfix_evaluation('23*45*+'))
    
    
    