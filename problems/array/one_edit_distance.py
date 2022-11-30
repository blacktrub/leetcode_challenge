class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """

    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False

        if abs(len(s) - len(t)) > 1:
            return False

        i = j = d = 0
        while i < len(s) and j < len(t):
            if d > 1:
                return False

            if s[i] != t[j]:
                if len(s) > len(t):
                    i += 1
                elif len(s) < len(t):
                    j += 1
                else:
                    i += 1
                    j += 1
                d += 1
                continue
            i += 1
            j += 1

        while i < len(s):
            i += 1
            d += 1

        while j < len(t):
            j += 1
            d += 1

        return d == 1
