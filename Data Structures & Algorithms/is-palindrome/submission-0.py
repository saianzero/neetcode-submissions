class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0


        s = s.replace(" ", "").lower()
        formatted_str = "".join(char for char in s if char.isalnum())
        if len(s) == 1:
            return True
        right = len(formatted_str)-1
        if left == right:
            return True
        while left < right:
            if formatted_str[left] != formatted_str[right]:
                return False

            if formatted_str[left] == formatted_str[right]:
                left+=1
                right-=1
        return True
        

        