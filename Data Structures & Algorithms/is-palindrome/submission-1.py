class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0


        s = s.replace(" ", "").lower()
        formatted_str = "".join(char for char in s if char.isalnum())

        right = len(formatted_str)-1

        while left < right:
            if formatted_str[left] != formatted_str[right]:
                return False
            
            left+=1
            right-=1
        return True
        

        