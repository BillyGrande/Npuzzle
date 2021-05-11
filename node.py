from puzzle import Puzzle

class Node:
    """
    Η κλάσση Node μας βοηθάει στο να αποθηκέυσουμε τα αντικείμενα
    Puzzle σε μορφή node. Δηλαδή να έχουν parent. Επίσης αποθηκεύουμε
    ποια κίνηση χρειάστηκε για να φτάσουμε εκεί.
    """
    def __init__(self,puzzle,parent=None,move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move

    @classmethod
    def equality(cls, node1, node2):
       tiles1 = node1.puzzle.tiles
       tiles2 = node2.puzzle.tiles
       return Puzzle.equal_tiles(tiles1,tiles2)
