class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palindrome = ""

        for ch in s:
            if ch.isalnum():
                palindrome += ch.lower()
        
        reverse_palindrome = palindrome[-1::-1]

        print(reverse_palindrome, palindrome)

        return palindrome == reverse_palindrome