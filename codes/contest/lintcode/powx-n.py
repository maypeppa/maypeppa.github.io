class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        def pow_pos(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            m = n // 2
            v = pow_pos(x, m)
            res = v * v
            if n % 2 == 1:
                res *= x
            return res

        if x == 0:
            return 0

        if n < 0:
            res = pow_pos(x, -n)
            res = 1.0 / res
        else:
            res = pow_pos(x, n)
        return res
