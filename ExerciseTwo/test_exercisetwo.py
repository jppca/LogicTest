import unittest
import exercisetwo

class TestUtils(unittest.TestCase):
    def test_convrom(self):
        self.assertEqual(exercisetwo.convrom(20),"XX")
        self.assertEqual(exercisetwo.convrom(5),"V")
        self.assertEqual(exercisetwo.convrom(10),"X")
        self.assertEqual(exercisetwo.convrom(15),"XV")

    def test_yrom(self):
        self.assertEqual(exercisetwo.yrom(300,"BC"),453)
        self.assertEqual(exercisetwo.yrom(2000,"AD"),2753)

    def test_maxcara(self):
        self.assertEqual(exercisetwo.maxcara(753,754),7)
        self.assertEqual(exercisetwo.maxcara(1,6),3)
        self.assertEqual(exercisetwo.maxcara(2753,2765),10)

if __name__ == '__main__': 
    unittest.main()