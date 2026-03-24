class Solution:
    def sortJumbled(self, mapping, nums):
        def getMapped(num):
            mapped = ''.join(str(mapping[int(d)]) for d in str(num))
            return int(mapped)

        arr = []
        for i, num in enumerate(nums):
            arr.append((getMapped(num), i, num))

        arr.sort()

        return [x[2] for x in arr]