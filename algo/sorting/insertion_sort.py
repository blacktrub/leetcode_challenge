"""
Time complexity
Worst case: O(n**2)
Average case: O(n**2)

Notes: 
    - Works in-place
    - Constant memory usage, O(1)
    - Effecient for small data sets
"""


def insertion_sort(arr: list[int]) -> None:
    for j in range(1, len(arr)):
        key = arr[j]

        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


if __name__ == "__main__":
    arr = [3, 2, 1]
    insertion_sort(arr)
    assert arr == [1, 2, 3], arr
