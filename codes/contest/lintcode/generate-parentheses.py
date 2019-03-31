class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here

        res = []
        def gen_rec(lbracket, depth, state):
            if lbracket == 0:
                s = state + (')' * depth)
                res.append(s)
                return

            if depth:
                gen_rec(lbracket, depth -1, state + ')')
            gen_rec(lbracket - 1, depth + 1, state + '(')

        gen_rec(n, 0, '')
        return res
