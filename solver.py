from puzzle import Puzzle
from node import Node
import copy
import  time

class Solver:

    moves = ["up","down","left","right"]

    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.visited = []
        self.parent = Node(puzzle)
        self.queue = [self.parent]

    def bfs(self):
        start = time.process_time()
        if self.parent.puzzle.solveable():

            node = self.queue[0]

            while not node.puzzle.final_state():
                #node.puzzle.pretty_print()
                #print(10*"-")

                for vnode in self.visited:
                    if Node.equality(vnode,node):
                        self.queue.pop(0)
                        node = self.queue[0]
                        continue

                self._expand(node)
                self.visited.append(node)
                self.queue.pop(0)

                node= self.queue[0]

            self.visited.append(node)
            self.queue.pop(0)

            print("Puzzle solved {0}".format(self.visited[-1].puzzle.tiles))
            print(len(self.visited))


            i = -1
            node = self.visited[i]
            solution = []
            while node.parent != None:
                solution.insert(0,node)
                node = node.parent

            self.puzzle.pretty_print()
            for node in solution:
                print(node.move)
                node.puzzle.pretty_print()

            print(time.process_time()-start)


    def dfs(self):
        start = time.process_time()
        if self.parent.puzzle.solveable():

            node = self.queue[0]

            while not node.puzzle.final_state():

                for vnode in self.visited:
                    if Node.equality(vnode,node):
                        self.queue.pop(0)
                        node = self.queue[0]
                        continue

                self.visited.append(node)
                self.queue.pop(0)
                self._expand_dfs(node)

                node = self.queue[0]

            self.visited.append(node)
            self.queue.pop(0)

            print("Puzzle solved {0}".format(self.visited[-1].puzzle.tiles))
            print(len(self.visited))


            i = -1
            node = self.visited[i]
            solution = []
            while node.parent != None:
                solution.insert(0,node)
                node = node.parent

            self.puzzle.pretty_print()
            for node in solution:
                print(node.move)
                node.puzzle.pretty_print()

            print(time.process_time()-start)


    def _next_moves(self,prev_move):
        try:
            return  copy.deepcopy(Solver.moves).remove(prev_move)
        except ValueError:
            return copy.deepcopy(Solver.moves)

    def _expand(self,node):
        #next_moves = self._next_moves(node.move)
        next_moves = ["up","down","left","right"]
        ogtiles = copy.deepcopy(node.puzzle.tiles)
        states = []
        for move in next_moves:
            #print(move)
            getattr( node.puzzle, "move_"+ move)()
            node2 = Node(Puzzle(node.puzzle.tiles),node,move)
            self.queue.append(node2)
            node.puzzle.tiles = copy.deepcopy(ogtiles)

    def _expand_dfs(self,node):
        next_moves = ["up","down","left","right"]
        ogtiles = copy.deepcopy(node.puzzle.tiles)
        states = []
        for move in next_moves:
            #print(move)
            getattr( node.puzzle, "move_"+ move)()
            node2 = Node(Puzzle(node.puzzle.tiles),node,move)
            self.queue.insert(0,node2)
            node.puzzle.tiles = copy.deepcopy(ogtiles)
