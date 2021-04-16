import math
import functools

class Puzzle:

    def __init__(self,tiles):
        self.tiles = tiles
        self.length = len(tiles)
        self.n = int(math.sqrt(self.length))
        self._solveable = (self._permutations() % 2 == 0)
        self.fs_tiles = list(range(1,self.length))
        self.fs_tiles.append(0)
        self.fs = self.final_state()


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
        if perms == 0: perms = 1

        return perms

    def final_state(self):
        if functools.reduce(lambda x, y: x and y, map(lambda n1,n2: n1 == n2,self.tiles,self.fs_tiles),True):
            self._solveable = True
            return True
        else:
            return False

    def pretty_print(self):
        pass
        i = 0
        row = 0
        column = 0
        while row < n:
            column = 0
