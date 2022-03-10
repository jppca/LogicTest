import unittest
import exerciseone

class TestUtils(unittest.TestCase):
    def test_rules(self):
        self.assertFalse(exerciseone.par(15))
        self.assertTrue(exerciseone.par(2000))
        self.assertEqual(exerciseone.rules(1,1),"R")
        self.assertEqual(exerciseone.rules(2,2),"L")
        self.assertEqual(exerciseone.rules(3,1),"D")
        self.assertEqual(exerciseone.rules(3,3),"R")

if __name__ == '__main__':
    unittest.main()