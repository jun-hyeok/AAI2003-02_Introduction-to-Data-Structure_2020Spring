#회문 판별 함수 2
from slstack import Stack
def is_palindrome(string):
    s = Stack()
    for i in string:
        s.push(i)
    reversed_string = ''
    while not s.is_empty():
        reversed_string = reversed_string + s.pop()
    if string == reversed_string:
        return True
    else:
        return False

if __name__ == "__main__":

    print( is_palindrome("pop") )
    print( is_palindrome("push") )
    print( is_palindrome("madam") )
    print( is_palindrome("rotator") )
    print( is_palindrome("tattarrattat") )
    
    
    
    
    