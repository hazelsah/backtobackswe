class Solution:
    def canVisitAllRooms(self, rooms):
        '''
        :type rooms: list of list of int
        :rtype: bool
        '''

        seen = []
        queue = []
        sol = []

        seen.append(0)
        queue.append(0)

        while len(queue) > 0:
            idx = queue.pop(0)
            sol.append(idx)
            for key in rooms[idx]:
                if key not in seen:
                    queue.append(key)
                    seen.append(key)

        if len(sol) != len(rooms):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    rooms = [[1], [2], [3], []]
    print(s.canVisitAllRooms(rooms))
