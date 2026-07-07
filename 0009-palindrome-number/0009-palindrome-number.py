class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        # Numbers ending in 0 cannot be palindrome
        # except 0 itself
        if x != 0 and x % 10 == 0:
            return False
        reverse = 0
        while x > reverse:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return x == reverse or x == reverse // 10