import math

class Puzzle:

    def __init__(self,tiles):
        self.tiles = tiles
        self.length = len(tiles)
        self.n = int(math.sqrt(self.length))
        self._solveable = (self._permutations() % 2 == 0)

    def solveable(self):
        return self._solveable

    def _permutations(self):
       i = 0
       perms = 0

       while i<self.length:
           num = self.tiles[i]
           for x in self.tiles[i:]:
               if x > num:
                   perms +=1
           i += 1

       return perms

    def pretty_print(self):
        pass
        i = 0
        row = 0
        column = 0
        while row < n:
            column = 0
            while column < n:
                break
