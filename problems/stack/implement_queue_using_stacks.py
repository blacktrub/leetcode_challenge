class MyQueue:
    def __init__(self):
        self.q = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.peek()
        return self.q2.pop()

    def peek(self) -> int:
        if not self.q2:
            while self.q:
                self.q2.append(self.q.pop())
        return self.q2[-1]

    def empty(self) -> bool:
        return len(self.q) == 0 and len(self.q2) == 0
