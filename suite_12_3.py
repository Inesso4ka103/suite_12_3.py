import unittest
import test_12_3

tester = unittest.TestSuite()
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tester)
