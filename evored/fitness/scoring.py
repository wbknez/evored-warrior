"""
Contains classes and functions concerned with obtaining fitness scores from a
Core Wars simulation.
"""
import subprocess
from abc import ABCMeta, abstractmethod


class ScoringException(Exception):
    """
    Represents an exception that is thrown when attempting to score the
    fitness of a list of warriors.
    """

    pass


class ScoreProvider(metaclass=ABCMeta):
    """
    Represents a mechanism to numerically determine the fitness of Redcode
    warriors by computing an overall score based on each warrior's
    performance against one another.
    """

    @abstractmethod
    def calculate(self, warriors, file_prefix, params):
        """
        Computes a score for each of the specified warriors that is used to
        determine whether the current iteration of their genome is worthwhile.

        Each element of the returned list of scores corresponds to the
        warrior at the index of the original argument list.

        Unlike earlier implementations of this project, the list of warriors
        represents the actual instruction lists.  It is up to deriving
        classes to correctly (and safely) output any required source code
        using the specified prefix as necessary.

        :param warriors: The list of warriors to evaluate.
        :param file_prefix: The prefix to use when creating Redcode source
        files (to avoid being overwritten by other processes).  Pure
        simulation implementations may ignore this.
        :param params: A dictionary of parameters.
        :return: A list of fitness scores.
        :raise ScoringException: If there was a problem evaluating the warriors.
        """
        pass


class PmarsScoreProvider(ScoreProvider):
    """
    Represents an implementation of FitnessEvaluator that uses an external
    program, PMARS, to evaluate warriors for fitness.
    """

    """
    Represents an implementation of FitnessEvaluator that uses an external
    program, PMARS, to evaluate warriors for fitness.
    """

    DEFAULT_ASM_OUTPUT = False
    """
    Whether or not to output assembly for inspection.
    """

    DEFAULT_CORE_SIZE = 8000
    """
    The default core memory size.
    """

    DEFAULT_PMARS_PATH = "bin/pmars"
    """
    The default location of the PMARS executable.
    
    Please note that this is a relative path.  PMARS must be compiled with 
    the -DSERVER switch in order to disable the graphical display entirely.
    """

    DEFAULT_ROUNDS = 50
    """
    The default number of rounds per invocation.
    """

    DEFAULT_VERBOSITY = False
    """
    Whether or not to display additional output.    
    """

    SCORE_OFFSET = len("scores") + 1
    """
    The number of characters to offset by when parsing PMARS output.
    """

    def __init__(self, params):
        exe = params.get("pmars.path", PmarsScoreProvider.DEFAULT_PMARS_PATH)

        # PMARS options.
        asm = params.get("pmars.asm", PmarsScoreProvider.DEFAULT_ASM_OUTPUT)
        core_size = params.get("pmars.core_size",
                               PmarsScoreProvider.DEFAULT_CORE_SIZE)
        rounds = params.get("pmars.rounds", PmarsScoreProvider.DEFAULT_ROUNDS)
        verbose = params.get("pmars.verbose",
                             PmarsScoreProvider.DEFAULT_VERBOSITY)

        self.cmd = [exe, "-r", str(rounds), "-s", str(core_size)]

        if not asm:
            self.cmd.append("-b")

        if verbose:
            self.cmd.append("-V")

    def calculate(self, warriors, file_prefix, params):
        if len(warriors) < 1 or (len(warriors) <= 1 and
                                 not params["benchmarks"]):
            raise ScoringException("Not enough warriors to score.")

        base_path = params["sim.temp_dir"] + "/" + file_prefix + "_"
        benchmarks = params.get("fitness.benchmarks", [])
        file_paths = [base_path + str(x) + ".RED" for x in range(len(warriors))]
        full_cmd = self.cmd + file_paths + benchmarks

        for warrior, file_path in zip(warriors, file_paths):
            warrior.write(file_path)

        pmars_pid = subprocess.Popen(full_cmd, shell=True,
                                     stdout=subprocess.PIPE)
        return self.parse_output(pmars_pid.stdout)

    def parse_output(self, stream):
        """
        Extracts the PMARS-generated fitness scores from the specified output
        stream.

        :param stream: The output stream to parse.
        :return: The generated fitness scores.
        """
        scores = []
        for line in stream:
            try:
                index = line.index("scores") + PmarsScoreProvider.SCORE_OFFSET
                scores.append(int(line[index:]))
            except ValueError:
                pass
        return scores
