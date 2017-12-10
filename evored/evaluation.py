"""
Contains all classes and functions necessary to evaluate individual Redcode
warriors for fitness.
"""
import subprocess
from abc import ABCMeta, abstractmethod


class EvaluationException(Exception):
    """
    Represents an exception that is thrown when attempting to evaluate a list of
    warriors in order to determine their fitness relative to each other.
    """

    pass


class FitnessEvaluator(metaclass=ABCMeta):
    """
    Represents a mechanism to numerically evaluate Redcode warriors by
    computing an overall score based on each warrior's performance against
    any others.
    """

    @abstractmethod
    def evaluate(self, warriors, params):
        """
        Computes a score for each of the specified warriors that is used to
        determine whether the current iteration of their genome is worthwhile.

        Each element of the returned list of scores corresponds to the
        warrior at the index of the original argument list.

        Please note that contrary to the initial version of this project,
        the variable argument list contains the warriors as Python objects.
        Evaluators that use external programs - for example, PMARS - must
        perform any conversions (e.g. output to filenames) to appropriate
        mediums themselves.  All additional required arguments are expected
        to be included as user-selected parameters.

        :param warriors: The list of warriors to evaluate.
        :param params: A dictionary of parameters.
        :return: A list of fitness scores.
        :raise EvaluationException: If there was a problem evaluating the
        warriors.
        """
        pass


def convert_to_temp_files(warriors):
    return []


def parse_output(stdout):
    """

    :param stdout:
    :return:
    """
    scores = []
    for line in stdout:
        try:
            index = line.index("scores") + PmarsFitnessEvaluator.SCORE_OFFSET
            scores.append(int(line[index:]))
        except ValueError:
            pass
    return scores


class PmarsFitnessEvaluator(FitnessEvaluator):
    """
    Represents an implementation of FitnessEvaluator that uses an external
    program, PMARS, to evaluate warriors for fitness against to one or more
    benchmarks.
    """

    DEFAULT_ASM_OUTPUT = False
    """
    Whether or not to output assembly for inspection.
    """

    DEFAULT_CORE_SIZE = 8000
    """
    The default core memory size.
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

    def __init__(self):
        self.cmd = []

    def build_command(self, params):
        """

        :param params:
        """
        exe = params.get("pmars_path", "/usr/bin/pmars")

        # PMARS options.
        asm = params.get("pmars.asm",
                         PmarsFitnessEvaluator.DEFAULT_ASM_OUTPUT)
        coresize = params.get("pmars.core_size",
                          PmarsFitnessEvaluator.DEFAULT_CORE_SIZE)
        rounds = params.get("pmars.rounds",
                            PmarsFitnessEvaluator.DEFAULT_ROUNDS)
        verbose = params.get("pmars.verbose",
                             PmarsFitnessEvaluator.DEFAULT_VERBOSITY)

        self.cmd = [exec, "-r", str(rounds), "-s", str(coresize)]

        if asm:
            self.cmd.extend("-b")

        if verbose:
            self.cmd.extend("-V")

    def evaluate(self, warriors, params):
        if not warriors:
            raise EvaluationException("There are no warriors to evaluate.")

        if not params["benchmarks"]:
            raise EvaluationException("There are not benchmarks to use for "
                                      "evaluation.")

        if not self.cmd:
            self.build_command(params)

        sources = convert_to_temp_files(warriors)
        full_cmd = self.cmd + sources + params["benchmarks"]
        pmars_pid = subprocess.Popen(full_cmd, shell=True,
                                     stdout=subprocess.PIPE)
        return parse_output(pmars_pid.stdout)
