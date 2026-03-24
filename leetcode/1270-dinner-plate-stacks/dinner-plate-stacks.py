import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.available = []
        self.right = -1

    def push(self, val: int) -> None:
        while self.available and self.available[0] < len(self.stacks) and len(self.stacks[self.available[0]]) == self.cap:
            heapq.heappop(self.available)

        if not self.available:
            self.stacks.append([])
            heapq.heappush(self.available, len(self.stacks) - 1)

        idx = self.available[0]
        self.stacks[idx].append(val)

        if len(self.stacks[idx]) == self.cap:
            heapq.heappop(self.available)

        self.right = max(self.right, idx)

    def pop(self) -> int:
        while self.right >= 0 and (self.right >= len(self.stacks) or not self.stacks[self.right]):
            self.right -= 1

        if self.right < 0:
            return -1

        val = self.stacks[self.right].pop()
        heapq.heappush(self.available, self.right)
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()
        heapq.heappush(self.available, index)
        return val