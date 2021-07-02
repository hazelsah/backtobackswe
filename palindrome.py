from math import floor


class Solution:

    def get_digit(self, number, n):
        l = []
        for i in range(0, n):
            l.append(number // 10 ** i % 10)
        return l

    def countDigit(self, n):
        count = 0
        while n != 0:
            n //= 10
            count += 1
        return count

    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        if x < 0:
            return False
        s = []

        l = self.get_digit(x, self.countDigit(x))
        if len(l) % 2 != 0: l.pop(int(len(l)/2))
        for i in range(0, int(len(l)/2)):
            s.append(l.pop())

        if l == s: return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))
    print(s.isPalindrome(9232))
    print(s.isPalindrome(1))
    print(s.isPalindrome(-121))