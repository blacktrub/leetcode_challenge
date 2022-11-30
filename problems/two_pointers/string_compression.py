from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast < len(chars):
            chars[slow] = chars[fast]
            count = 1
            while fast + 1 < len(chars) and chars[fast] == chars[fast + 1]:
                fast += 1
                count += 1

            if count > 1:
                for c in str(count):
                    slow += 1
                    chars[slow] = c

            fast += 1
            slow += 1

        return slow


if __name__ == "__main__":
    assert Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
