"""
Contains unit tests for verifying correctness of PMARS related fitness
evaluation algorithms.
"""
from unittest import TestCase

from evored.evaluation import PmarsFitnessEvaluator


class PmarsFitnessEvaluatorTest(TestCase):
    """
    Test suite for PmarsFitnessEvaluator.
    """

    EXAMPLE_RESULTS = """
    Iron Gate scores 22
    Results: 0 0 2 0 0 0 8
    Paperone scores 48
    Results: 0 0 3 1 1 0 5
    Tornado scores 7
    Results: 0 0 0 0 1 0 9
    Thermite 1.0 scores 26
    Results: 0 0 1 1 1 0 7
    TimeScape (1.0) scores 98
    Results: 0 1 6 1 1 0 1
    Marcia Trionfale 1.3 scores 133
    Results: 1 1 6 1 1 0 0
    """.split("\n")

    def setUp(self):
        self.evaluator = PmarsFitnessEvaluator()

    def tearDown(self):
        pass

    def test_build_command_with_defaults(self):
        expected = [PmarsFitnessEvaluator.DEFAULT_PMARS_PATH,
                    "-r", str(PmarsFitnessEvaluator.DEFAULT_ROUNDS),
                    "-s", str(PmarsFitnessEvaluator.DEFAULT_CORE_SIZE),
                    "-b"]
        params = dict()

        self.evaluator.build_command(params)
        self.assertEqual(expected, self.evaluator.cmd)

    def test_build_command_with_custom_parameters(self):
        expected = """%s -r %i -s %i -V"""
        params = {"pmars.asm": True,
                  "pmars.core_size": 9000,
                  "pmars.path": "/usr/bin/pmars",
                  "pmars.rounds": 30,
                  "pmars.verbose": True}

        expected = expected % (params["pmars.path"], params["pmars.rounds"],
                               params["pmars.core_size"])
        expected = expected.split(' ')

        self.evaluator.build_command(params)
        self.assertEqual(expected, self.evaluator.cmd)

    def test_parse_output(self):
        scores = self.evaluator.parse_output(
            PmarsFitnessEvaluatorTest.EXAMPLE_RESULTS)

        self.assertEqual(6, len(scores))
        self.assertEqual(22, scores[0])
        self.assertEqual(48, scores[1])
        self.assertEqual(7, scores[2])
        self.assertEqual(26, scores[3])
        self.assertEqual(98, scores[4])
        self.assertEqual(133, scores[5])
