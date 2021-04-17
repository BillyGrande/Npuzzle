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

    def _move(self,zindex,index):
        self.tiles[zindex] = self.tiles[index]
        self.tiles[index] = 0

    def move_down(self):
        zindex = self.tiles.index(0)
        index = zindex + self.n
        if index <= self.length-1:
            self._move(zindex,index)

    def move_up(self):
        zindex = self.tiles.index(0)
        index = zindex - self.n
        if index >= 0:
            self._move(zindex,index)


    def move_right(self):
        zindex = self.tiles.index(0)
        index = zindex + 1
        if (index % self.n) != 0:
            self._move(zindex,index)


    def move_left(self):
        zindex = self.tiles.index(0)
        index = zindex - 1
        if zindex !=0:
            if (zindex % self.n) != 0:
                self._move(zindex,index)
