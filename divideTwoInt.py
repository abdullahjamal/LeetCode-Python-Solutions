class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        pos = (dividend < 0 ) is (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp,i = divisor, 1
            while dividend >= temp:
                dividend -=temp
                quotient += i
                i <<= 1
                temp <<= 1
        if not pos:
            quotient = -quotient
        return min(max(-2147483648,quotient),2147483647)
