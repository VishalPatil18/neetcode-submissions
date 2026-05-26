class MinStack:

    def __init__(self):
        self.stk = []
        minVal = float('-inf')

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        tmp = []
        minEl = self.stk[-1]
        while len(self.stk):
            minEl = min(minEl, self.stk[-1])
            tmp.append(self.stk.pop())

        while len(tmp):
            self.stk.append(tmp.pop())

        return minEl
