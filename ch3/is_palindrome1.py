#회문 판별 함수 1
from slstack import Stack
def is_palindrome(string):
    s = Stack()
    palindrome = True
    if len(string) % 2 == 0:
        for i in string[:len(string)//2]:
            s.push(i)
        for j in string[len(string)//2:]:
            temp = s.pop()
            if temp != j:
                palindrome = False
                break
    else:
        for i in string[:len(string)//2]:
            s.push(i)
        for j in string[len(string)//2+1:]:
            temp = s.pop()
            if temp != j:
                palindrome = False
                break
    return palindrome

if __name__ == "__main__":

    print( is_palindrome("pop") )
    print( is_palindrome("push") )
    print( is_palindrome("rotator") )
    print( is_palindrome("tattarrattat") )
    
