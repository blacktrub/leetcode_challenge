class Counter:
    def __init__(self) -> None:
        self.q = [(0, 0)] * (60 * 5)

    def hit(self, tm):
        idx = tm % 300
        time, hit = self.q[idx]
        if time != tm:
            self.q[idx] = tm, 1
        else:
            self.q[idx] = time, hit + 1

    def getHits(self, tm):
        res = 0
        for time, hit in self.q:
            if tm - time < 300:
                res += hit
        print(self.q)
        print("res", tm, res)
        return res


if __name__ == "__main__":
    counter = Counter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    assert counter.getHits(4) == 3
    counter.hit(300)
    assert counter.getHits(300) == 4
    assert counter.getHits(301) == 3
