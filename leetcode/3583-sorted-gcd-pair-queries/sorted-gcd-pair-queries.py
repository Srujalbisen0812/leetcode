from bisect import bisect_left

class Solution:
    def gcdValues(self, nums, queries):
        maxv = max(nums)
        freq = [0] * (maxv + 1)

        for x in nums:
            freq[x] += 1

        cnt = [0] * (maxv + 1)

        for g in range(1, maxv + 1):
            total = 0
            for multiple in range(g, maxv + 1, g):
                total += freq[multiple]
            cnt[g] = total * (total - 1) // 2

        for g in range(maxv, 0, -1):
            for multiple in range(2 * g, maxv + 1, g):
                cnt[g] -= cnt[multiple]

        values = []
        prefix = []

        total = 0
        for g in range(1, maxv + 1):
            if cnt[g] > 0:
                total += cnt[g]
                values.append(g)
                prefix.append(total)

        res = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            res.append(values[idx])

        return res