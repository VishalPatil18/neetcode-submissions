class Solution:
    def isValid(self, s: str) -> bool:
        """
        Input: string of brackets
        Output: True if valid, False if invalid
        Plan:
            - Have a stack for brackets
            - Start from the first and keep adding the brackets to the stack if they're 
              (, {, [
            - If brackets are }, ], ), check the top of stack and if it is corresponding
              open bracket, remove it from the stack, else add this to the stack
            - After complete iteration
                if stk is empty, return True
                else return False
        """
        stk = []
        for bracket in s:
            if bracket == ')' and len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            elif bracket == '}' and len(stk) != 0 and stk[-1] == '{':
                stk.pop()
            elif bracket == ']' and len(stk) != 0 and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(bracket)

        return True if len(stk) == 0 else False