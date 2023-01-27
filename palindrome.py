# program 1
def isPalindrome(x):
    for i in range(0, int(len(x)/2)):
        if x[i] != x[len(x)-i-1]:
            return False
    return True

input1 = input('Enter string : ')
result = isPalindrome(input1)
if(result):
    print(input1, 'is a Palindrome.')
else:
    print(input1, 'is not a Palindrome.')

# Program 2
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False