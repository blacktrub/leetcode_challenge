from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev, start = chars[0], 0
        for i in range(1, len(chars)):
            ch = chars[i]
            if ch != prev:
                start = i
                prev = chars[i]
            else:
                chars[start] += ch
                chars[i] = ""

        i = 0
        while i < len(chars):
            print("ti", chars[i])
            if chars[i] == "":
                i += 1
                continue

            if len(chars[i]) == 1:
                i += 1
                continue

            group = chars[i]
            chars[i] = group[0]
            j = i + 1
            for n in str(len(group)):
                chars[j] = n
                j+=1
            i += 2

        return len([x for x in chars if x != ""])


if __name__ == "__main__":
    assert Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
