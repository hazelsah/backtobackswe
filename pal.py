from math import floor
from math import log10


class Solution:

    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        if x < 0:
            return False

        stck = []
        lst = []
        #number of digits
        n_digits = int(floor(log10(x))) + 1
        #split digits
        for i in range(0, n_digits):
            lst.append(x // 10 ** i % 10)
        #remove middle element
        if n_digits % 2 != 0: lst.pop(int(len(lst) / 2))
        #check lists are equal or not
        for i in range(0, int(len(lst) / 2)):
            stck.append(lst.pop())
        if lst == stck:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(89233298)
