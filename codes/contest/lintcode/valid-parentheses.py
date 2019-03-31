class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for c in s:
            if c in '([{':
                exp_c = None
                if c == '(':
                    exp_c = ')'
                elif c == '[':
                    exp_c = ']'
                elif c == '{':
                    exp_c = '}'
                stack.append(exp_c)
            else:
                if not stack or stack[-1] != c:
                    return False
                stack = stack[:-1]
        return not stack
