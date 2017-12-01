"""
Contains all classes and functions necessary to describe the Redcode language
per the 1994 standard.
"""
from enum import unique, Enum


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
