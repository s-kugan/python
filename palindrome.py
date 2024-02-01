# This program identifies its a palindrome or not
def isPalindrome(text):
    temp=""
    for x in range(len(text)-1,-1,-1):
        temp += text[x]
        
    if temp==text:
        return True
    return False


print(isPalindrome('MadaM'))
        