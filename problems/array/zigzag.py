# Input: v1 = [1, 2] and v2 = [3, 4, 5, 6]
# Output: [1, 3, 2, 4, 5, 6]
# Explanation:
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.first = v1
        self.second = v2
        self.cur_first = len(v1) > 0
        self.first_cur = 0
        self.second_cur = 0

    def _next(self):
        if self.cur_first:
            val = self.first[self.first_cur]
            self.first_cur += 1
        else:
            val = self.second[self.second_cur]
            self.second_cur += 1

        if self.cur_first and self.second_cur < len(self.second):
            self.cur_first = False
        elif not self.cur_first and self.first_cur < len(self.first):
            self.cur_first = True

        return val

    def hasNext(self):
        return self.first_cur < len(self.first) or self.second_cur < len(self.second)


if __name__ == "__main__":
    i = ZigzagIterator([1], [4])
    out = []
    while i.hasNext():
        out.append(i._next())

    assert out == [1, 4]

    i = ZigzagIterator([1], [])
    out = []
    while i.hasNext():
        out.append(i._next())

    assert out == [1]

    i = ZigzagIterator([], [1])
    out = []
    while i.hasNext():
        out.append(i._next())

    assert out == [1]

    i = ZigzagIterator([1, 2, 3], [1])
    out = []
    while i.hasNext():
        out.append(i._next())

    assert out == [1, 1, 2, 3]

    i = ZigzagIterator([1], [1, 2, 3])
    out = []
    while i.hasNext():
        out.append(i._next())

    assert out == [1, 1, 2, 3]
