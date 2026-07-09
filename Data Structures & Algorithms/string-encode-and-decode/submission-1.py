class Solution:
    hmap = {}

    def encode(self, strs: List[str]) -> str:

        s = "".join(strs)
        self.hmap[s] = strs
        return s
    
    def decode(self, s: str) -> List[str]:
        for k, v in self.hmap.items():
            if k == s:
                return v
        
