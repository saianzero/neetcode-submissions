class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        close_to_open = {")":"(","}":"{","]":"["}
        
        for char in s:
            if char in "{[(":
                st.append(char)
            else:

                if not st or st[-1]!= close_to_open[char]:
                    return False
                st.pop()
        return len(st)==0
                
