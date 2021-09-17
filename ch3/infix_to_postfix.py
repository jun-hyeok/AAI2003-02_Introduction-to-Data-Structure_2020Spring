#스택을 이용한 후위표기법 변환 함수 
from slstack import Stack
def infix_to_postfix(string):
    precedence = {} 
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1
    
    s = Stack()
    result = ""
    for i in string: 
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYX" or i in "0123456789": 
            result = result + i 
        elif i == "(":
            s.push(i) 
        elif i == ")":
            top = s.pop() 
            while top != "(":
                result = result + top
                top = s.pop()
        else:
            while (not s.is_empty()) and (precedence[s.peek()]>=precedence[i]):
                result = result + s.pop()
            s.push(i)
    while not s.is_empty(): 
        result = result + s.pop()
    return result

if __name__ == "__main__":
    print(infix_to_postfix('(A+B)/(C-D)'))
    print(infix_to_postfix('A*B+C*D'))
    print(infix_to_postfix('(A+B)*C-(D-E)*(F+G)'))

