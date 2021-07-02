class Solution:
    def isValid(self, s):
        '''
        :type s: str
        :rtype: bool
        '''
        lst = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                lst.append(char)
            elif char == ')':
                if len(lst) == 0: return False
                c = lst.pop()
                if c != '(':
                    return False
            elif char == '}':
                if len(lst) == 0: return False
                c = lst.pop()
                if c != '{':
                    return False
            elif char == ']':
                if len(lst) == 0: return False
                c = lst.pop()
                if c != '[':
                    return False
        if len(lst) == 0: return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('((([[)))'))
