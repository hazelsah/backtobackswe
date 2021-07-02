class Solution:
    def findAndReplacePattern(self, words, pattern):
        '''
        :type words: list of str
        :type pattern: str
        :rtype: list of str
        '''
        lst = []
        words.append(pattern)
        for word in words:
            dict = {}
            str = ""
            i = 0
            for char in word:
                if char in dict:
                    str = str + dict[char].__str__()
                else:
                    dict[char] = i
                    str = str + dict[char].__str__()
                    i = i + 1
            lst.append(str)

        matched = []
        ptrn = lst[-1]
        for iteration, item in enumerate(lst[0:len(lst) - 1]):
            if ptrn == item:
                matched.append(words[iteration])
        return matched


if __name__ == '__main__':
    s = Solution()
    print(s.findAndReplacePattern(["aba", "dde", "efe", "yzy"], "iji"))
