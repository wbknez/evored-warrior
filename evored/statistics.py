"""
Contains all classes and functions related to deriving, storing, and writing
statistics information.
"""


class FitnessStatistics:
    """
    Represents a mechanism for deriving and storing statistical data from a
    list of tiness-related objects.
    """

    def __init__(self, max=0, mean=0, min=0, variance=0):
        self.max = max
        self.mean = mean
        self.min = min
        self.variance = variance

    def __copy__(self):
        return FitnessStatistics(self.max, self.mean, self.min, self.variance)

    def __eq__(self, other):
        if isinstance(other, FitnessStatistics):
            return self.max == other.max and self.mean == other.mean and \
                   self.min == other.min and self.variance == other.variance
        return NotImplemented

    def __hash__(self):
        return hash((self.max, self.mean, self.min, self.variance))

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return repr((self.max, self.mean, self.min, self.variance))

    def __str__(self):
        return "+: " + str(self.max) + \
               " -: " + str(self.min) + \
               " mu: " + str(self.mean) + \
               " var: " + str(self.variance)

    def update(self, fitnessables, extractor=lambda val: val):
        """
        Computes new statistics and stores them from the specified list of
        tiness-related objects.

        :param fitnessables: The list of fitness-related objects to compute
        various statistics from.
        :param extractor: A function to use to extract a fitness score from
        an object.
        """
        self.max = self.min = self.mean = self.variance = 0
        sum, sum_sq, score = 0, 0, 0
        n = len(fitnessables)

        for fit in fitnessables:
            score = extractor(fit)
            sum += score
            sum_sq += score * score

            if score < self.min:
                self.min = score
            if score > self.max:
                self.max = score

        self.mean = sum / n
        self.variance = (n * sum_sq - (sum * sum)) / (n * (n - 1))
