input = "abcba"
input1 = "abcdda"
def is_palindrome(string):
    n = len(string)
    for i in range(n): #i:0 ~ n-1
        if string[i] != string[n - 1 - i]:
            return False
    return True

print(is_palindrome(input))

#재귀함수 사용 시
def is_palindrome_recursive(string):
    if string[0] != string[-1]:
        return False
    if len(string) <=1:
        return True
    return is_palindrome_recursive(string[1:-1])

print(is_palindrome_recursive(input1))