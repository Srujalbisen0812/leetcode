class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = [0] * maxSize
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        i = len(self.stack) - 1
        if i > 0:
            self.inc[i - 1] += self.inc[i]

        val = self.stack.pop() + self.inc[i]
        self.inc[i] = 0
        return val

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            i = min(k, len(self.stack)) - 1
            self.inc[i] += val