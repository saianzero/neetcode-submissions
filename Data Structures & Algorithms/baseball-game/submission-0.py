class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                res = int(record[-1]) + int(record[-2])
                record.append(res)
            elif op == "D":
                res = 2*int(record[-1])
                record.append(res)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)


