"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

from heapq import heappush, heappop


class Heap:
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        return str(self.data)

    def push(self, n):
        heappush(self.data, n)

    def pop(self):
        return heappop(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


class MinHeap(Heap):
    pass


class MaxHeap(Heap):
    def push(self, n):
        if n > 0:
            n = -n
        else:
            n = abs(n)
        super().push(n)

    def pop(self):
        n = super().pop()
        if n > 0:
            n = -n
        else:
            n = abs(n)
        return n

    def __getitem__(self, idx):
        n = super().__getitem__(idx)
        if n > 0:
            n = -n
        else:
            n = abs(n)
        return n


class MedianFinder:
    def __init__(self):
        self.max_heap = MinHeap()
        self.min_heap = MaxHeap()

    def addNum(self, num: int) -> None:
        if not self.max_heap and not self.min_heap:
            self.min_heap.push(num)
            return

        m = self.findMedian()
        if num > m:
            if self.max_heap and self.max_heap[0] < num:
                self.min_heap.push(self.max_heap.pop())
            self.max_heap.push(num)
        else:
            if self.min_heap and self.min_heap[0] > num:
                self.max_heap.push(self.min_heap.pop())
            self.min_heap.push(num)

        while self.max_heap and self.max_heap[0] < m:
            self.min_heap.push(self.max_heap.pop())

        while self.min_heap and self.min_heap[0] > m:
            self.max_heap.push(self.min_heap.pop())

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            sm = self.min_heap[0] + self.max_heap[0]
            add = 1 if sm > 0 else -1
            return (abs(sm) / 2) * add
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return self.max_heap[0]


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(2)
    mf.addNum(1)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    mf = MedianFinder()
    mf.addNum(-1)
    mf.addNum(-2)
    mf.addNum(-3)
    mf.addNum(-4)
    mf.addNum(-5)
    assert mf.findMedian() == -3.0

    mf = MedianFinder()
    for x in [12, 10, 13, 11, 5, 15]:
        mf.addNum(x)
    assert mf.findMedian() == 11.5
