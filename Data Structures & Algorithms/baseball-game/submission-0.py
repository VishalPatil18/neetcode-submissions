class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Input: List of Str with nums and Operations
        Output: Number (sum of all the records)
        Plan:
            - Iterate over the operations list and add the element to the records stack
            - Maintain a records stack
            - If + is encountered -> take sum of previous two el of stack and add the result to records
            - If D is encountered -> take double of prevous score and add to record
            - If C is encountered -> remove the previous record
        """
        record_stk = []
        for el in operations:
            if el == '+':
                num1 = int(record_stk[-1])
                num2 = int(record_stk[-2])
                record_stk.append(num1 + num2)
            elif el == 'D':
                record_stk.append(int(record_stk[-1]) * 2)
            elif el == 'C':
                record_stk.pop()
            else:
                record_stk.append(int(el))
            
        return sum(record_stk)