class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def make_cache(self, N):
        self.cache = []
        self.N = N
        for i in range(N + 1):
            c = [-1] * (1 << (N + 1))
            self.cache.append(c)

    def find(self, state, n):
        if n == 0: return 1
        if self.cache[n][state] != -1:
            return self.cache[n][state]
        N = self.N
        res = 0
        for i in range(N):
            if (state >> i) & 0x1:
                value = i + 1
                if value % n == 0 or n % value == 0:
                    new_state = state & (~(1 << i))
                    res += self.find(new_state, n - 1)
        self.cache[n][state] = res
        return res

    def countArrangement(self, N):
        # Write your code here
        self.make_cache(N)
        res = self.find((1 << (N + 1)) -1, N)
        return res
