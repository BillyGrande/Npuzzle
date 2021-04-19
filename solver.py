from puzzle import Puzzle
from node import Node
import copy

class Solver:

    #moves = ["up","down","left","right"]

    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.visited = []
        self.parent = Node(puzzle)
        self.queue = [self.parent]

    def bfs(self):
        if self.parent.puzzle.solveable():
            while input() == "y":
                print(self.queue)
                node= self.queue[0]
                node.puzzle.pretty_print()
                if not node.puzzle.final_state():
                    for vnode in self.visited:
                        if Node.equality(vnode,node):
                            self.queue.pop(0)
                            continue
                    self._expand(node)
                    self.visited.append(node)
                    self.queue.pop(0)
                else:
                    self.visited.append(node)
                    self.queue.pop(0)
                    break

            print("Puzzle solved {0}".format(self.visited[-1].puzzle.puzzle.tiles))


    def dfs(self):
        pass

    def _next_moves(self,prev_move):
        try:
            return  ["up","down","left","right"].remove(prev_move)
        except ValueError:
            return ["up","down","left","right"]

    def _expand(self,node):
        next_moves = self._next_moves(node.move)
        ogtiles = copy.deepcopy(node.puzzle.tiles)
        states = []
        print(next_moves)
        for move in next_moves:
            getattr( node.puzzle, "move_"+ move)()
            node2 = Node(Puzzle(node.puzzle.tiles),node,move)
            self.queue.append(node2)
            node.puzzle.tiles = ogtiles
