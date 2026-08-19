class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for detail in details:
            if int(detail[-4:-2]) > 60:
                    count+=1
        return count

