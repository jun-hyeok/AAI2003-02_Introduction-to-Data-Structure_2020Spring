#일반화시킨 괄호 짝 판별 함수  
from slstack import Stack

def is_balanced(string):
    s = Stack()
    balanced = True
    for i in string:
        if i in "({[":
            s.push(i)
        elif i in")}]":
            if s.is_empty(): 
                balanced = False
            else:
                temp = s.pop()
                if not is_matched(temp, i):
                    balanced = False
    if s.is_empty() and balanced:
        return True
    else:
        return False

def is_matched(open, close):
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)
    
if __name__ == "__main__":

    print( is_balanced("1+2*[{(3+4)+(5+6)}*(7+8)]") )
    print( is_balanced("{(({())}") )
    print( is_balanced("(((()))") )
    
    
    