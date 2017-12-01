"""
Contains all classes and functions necessary to describe the Redcode language
per the 1994 standard.
"""
from enum import unique, Enum


@unique
class AddressMode(Enum):
    """
    Represents the available addressing modes in Redcode.
    """

    A = "*"
    """
    Indirect addressing mode using the A-field (pointer of pointer address).
    """

    APredecrement = "{"
    """
    Addressing mode that decrements the A-field indirect address before 
    retrieving the value stored at that location.
    """

    APostincrement = "}"
    """
    Addressing mode that increments the A-field indirect address after 
    retrieving the value stored at that location.
    """

    B = "@"
    """
    Indirect addressing mode using the B-field (pointer of pointer address).
    """

    BPredecrement = "<"
    """
    Addressing mode that decrements the B-field indirect address before 
    retrieving the value stored at that location.
    """

    BPostincrement = ">"
    """
    Addressing mode that increments the B-field indirect address after 
    retrieving the value stored at that location.
    """

    Direct = "$"
    """
    Addressing mode that uses the value of the A- or B-fields as the address 
    (direct pointer address).
    
    This mode is the default in the absence of any others.
    """

    Immediate = "#"
    """
    Addressing mode that uses the current instruction as the address.
    """


@unique
class Modifier(Enum):
    """
    Represents a collection of modifiers that may adorn an argument value in
    Redcode.
    """

    A = "A",
    """
    A modifier that uses the A-field value directly.
    """

    AB = "AB",
    """
    A modifier that uses the A-field value from the A-field address and the 
    B-field value from the B-field address.
    """

    B = "B",
    """
    A modifier that uses the B-field value directly.
    """

    BA = "BA",
    """
     A modifier that uses the B-field value from the A-field address and the 
     A-field value from the B-field address.
    """

    F = "F",
    """
    A modifier that copies both A- and B-field addresses from a source to a 
    destination, preserving their current order (A-field source address is 
    copied to the A-field destination and vis versa).
    """

    I = "I",
    """
    A modifier that copies the entire instruction from a source to a 
    destination.
    """

    X = "X"
    """
    A modifier that copies both A- and B-field addresses from a source to a 
    destination, exchanging their current order (A-field source address is 
    copied to the B-field destination and vis versa).
    """

    Empty = None
    """
    A modifier that does nothing.
    
    Empty modifiers are allowed per the standard to facilitate backwards 
    compatibility.  That said, this is only used for random generation purposes.
    """


class Argument:
    """
    Represents a single argument to an instruction in Redcode.
    """

    def __init__(self, addr_mode=AddressMode.Direct, value=0):
        self.addr_mode = addr_mode
        self.value = value

    def __copy__(self):
        return Argument(self.addr_mode, self.value)

    def __eq__(self, other):
        if isinstance(other, Argument):
            return self.addr_mode == other.addr_mode and \
                   self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash((self.addr_mode, self.value))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "%s%i" % (self.addr_mode.value, self.value)


@unique
class OpCode(Enum):
    pass


class Instruction:
    """
    Represents a collection of symbols that together form a single
    instruction in Redcode.
    """

    def __init__(self, opcode, modifier=None, arg_a=None, arg_b=None):
        self.opcode = opcode
        self.modifier = modifier
        self.arg_a = arg_a
        self.arg_b = arg_b

    def __eq__(self, other):
        if isinstance(other, Instruction):
            return self.opcode == other.opcode and \
                   self.modifier == other.modifier and \
                self.arg_a == other.arg_a and self.arg_b == other.arg_b
        return NotImplemented

    def __hash__(self):
        return hash((self.opcode, self.modifier, self.arg_a, self.arg_b))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        ins_str = self.opcode.value
        if self.modifier:
            ins_str += ".%s" % self.modifier.value
        ins_str += " %s %s " % (self.arg_a, self.arg_b)
        return ins_str
