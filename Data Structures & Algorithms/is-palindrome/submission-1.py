class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        left = 0
        right = len(string) - 1
        while left < right:
            while left < right and not string[left].isalnum():
                left += 1
            while left < right and not string[right].isalnum():
                right -= 1
            if string[left] != string[right]:
                return False
            left  += 1
            right -= 1
        return  True
            

            