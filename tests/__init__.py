"""
Contains all utility methods and classes necessary for the unit tests
contained within to run correctly.
"""
from random import randint

from evored.genome import Genome


def random_genome_list(fitness_scores, max_chromosome_num=10,
                       max_chromosome_value=100):
    """
    Creates a list of genomes whose structures are randomly generated but
    whose fitness scores are not, making them suitable for testing algorithms
    that use that score as part of their logic.

    :param fitness_scores: The list of fitness scores to use.
    :param max_chromosome_num: The maximum number of chromosomes a genome may
    have.
    :param max_chromosome_value: The maximum value a single chromosome may have.
    :return: A list of randomly generated genomes.
    """
    genomes = []
    for score in fitness_scores:
        chromosomes = [randint(0, max_chromosome_value) \
                       for _ in range(randint(1, max_chromosome_num))]
        genomes.append(Genome(chromosomes=chromosomes, fitness=score))
    return genomes
