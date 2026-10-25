class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)  # diff = val - val = 0
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:
                self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return

        diff = self.stack.pop()
        if diff < 0:
            # Recover previous min_val
            self.min_val = self.min_val - diff

        if not self.stack:
            self.min_val = None  # reset if stack is empty

    def top(self) -> int:
        if not self.stack:
            return None

        diff = self.stack[-1]
        if diff >= 0:
            return self.min_val + diff
        else:
            return self.min_val

    def getMin(self) -> int:
        return self.min_val

