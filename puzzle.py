import math
import functools
import copy

class Puzzle:

    def __init__(self,tiles):
        self._tiles = tiles
        self.tiles = copy.deepcopy(self._tiles)
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
                if num > x:
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
        while row < self.n:
            column = 0
            text = ""
            dtext = ""
            while column < self.n:
                text = text + str(self.tiles[column+i]) + "|"
                dtext = dtext + "-+"
                column +=1
            print(text[:-1])
            print(dtext)
            row += 1
            i += self.n
