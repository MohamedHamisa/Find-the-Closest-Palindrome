class Solution:
    def nearestPalindromic(self, n):
        k = len(n)
        candidates = set((str(10 ** k + 1), str(10 ** (k - 1) - 1)))
        prefix = int(n[:(k + 1) // 2])
        for num in map(str, (prefix - 1, prefix, prefix + 1)):
            suffix = num if k % 2 == 0 else num[:-1]
            candidates.add(num + suffix[::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
