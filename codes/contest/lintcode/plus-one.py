class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        n = len(digits)
        carry = 1
        for i in reversed(range(n)):
            carry += digits[i]
            digits[i] = carry % 10
            carry //= 10
        if carry:
            digits.insert(0, carry)
        return digits
