class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        ch_to_idx = lambda ch: ord(ch) - ord("a")

        cnt = [0] * 26
        for ch in p:
            cnt[ch_to_idx(ch)] += 1

        cur = [0] * 26
        i, j = 0, len(p)
        for x in range(j):
            cur[ch_to_idx(s[x])] += 1

        found = 0
        for i in range(len(cnt)):
            if cnt[i] == cur[i]:
                found += 1

        res = []
        i = 0
        while j < len(s):
            if found == 26:
                res.append(i)

            ch = s[j]
            idx = ch_to_idx(ch)
            cur[idx] += 1

            if cnt[idx] == cur[idx]:
                found += 1
            elif cnt[idx] + 1 == cur[idx]:
                found -= 1

            iidx = ch_to_idx(s[i])
            cur[iidx] -= 1
            if cnt[iidx] == cur[iidx]:
                found += 1
            elif cnt[iidx] - 1 == cur[iidx]:
                found -= 1

            i += 1
            j += 1

        if found == 26:
            res.append(i)

        return res
