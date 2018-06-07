class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        r, n = 0, x

        while n > 0:
            reminder = n % 10
            r = (r * 10) + reminder
            n = n // 10

        print(x)
        print(r)
        print(n)

        return x == r
