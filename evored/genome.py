"""
Contains all the classes and functions that comprise the conceptual model for
this project.
"""
from evored.fitness import Fitnessable
from evored.tree import Tree, _copy_tree


class Chromosome(Fitnessable):
    """
    Represents a single Redcode instruction in a probabilistic syntax tree.
    """

    def __init__(self, ins, fitness=0):
        super().__init__(fitness)
        self.ins = ins

    def __copy__(self):
        return Chromosome(self.ins, self.fitness)

    def __eq__(self, other):
        if isinstance(other, Chromosome):
            return self.fitness == other.fitness and self.ins == other.ins
        return NotImplemented

    def __hash__(self):
        return hash((self.fitness, self.ins))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "(%s,%i)" % (self.ins, self.fitness)


class Warrior(Fitnessable):
    """
    Represents a single, stochastic realization of a genome tree.

    This warrior object itself represents a collection of Redcode assembly
    instructions that have been created by a probabilistic depth-first
    traversal of a binary tree of chromosomes to a leaf.  Each warrior has a
    fitness score that is determined by its performance against other
    warriors using a Core Wars simulator, in this case the PMARS program.
    """

    def __init__(self, ins_list, fitness=0):
        super().__init__(fitness)
        self.ins_list = ins_list

    def __copy__(self):
        return Warrior(self.ins_list, self.fitness)

    def __eq__(self, other):
        if isinstance(other, Warrior):
            return self.fitness == other.fitness and \
                   self.ins_list == other.ins_list
        return NotImplemented

    def __hash__(self):
        return hash((self.fitness, self.ins_list))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "\n".join(map(str, self.ins_list))


class Genome(Fitnessable, Tree):
    """
    Represents a probabilistic syntax tree whose nodes are comprised of
    singular Redcode instructions.
    """

    def __init__(self, chromosomes=None, fitness=0):
        Fitnessable.__init__(self, fitness)
        Tree.__init__(self, chromosomes)

    def __copy__(self):
        return _copy_tree(self, Genome(fitness=self.fitness))

    def __eq__(self, other):
        if isinstance(other, Genome):
            return Fitnessable.__eq__(self, other) and Tree.__eq__(self, other)
        return NotImplemented

    def hash(self):
        return hash((Fitnessable.__hash__(self), Tree.__hash__(self)))

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return repr((Fitnessable.__repr__(self), Tree.__repr__(self)))

    def __str__(self):
        return "(" + Fitnessable.__str__(self) + ", " + \
               Tree.__str__(self) + ")"
