class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        max_len = 0
        for r in range(len(s)):
            # keep removing the duplicates until the invariant condition is met
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            #once the duplicates are gone, add s[r]
            charset.add(s[r])
        
            if max_len < r-l+1:
                max_len = r-l+1
        return max_len
        



        