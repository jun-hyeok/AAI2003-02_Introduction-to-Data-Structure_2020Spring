#소괄호 짝 판별 함수
from slstack import Stack
def is_balanced(string):
    s = Stack()
    balanced = True
    for i in string:
        if i == "(":
            s.push(i)
        elif i == ")":
            if s.is_empty(): 
                balanced = False
            else:
                s.pop()
    if s.is_empty() and balanced:
        return True
    else:
        return False

if __name__ == "__main__":

    print( is_balanced("(1+2)*(3+4)*(5+6)*(7+8)") )
    print( is_balanced("(()(()))") )
    print( is_balanced("(((()))") )

