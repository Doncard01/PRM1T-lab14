import unittest
import funkcje as f

class PierwszyTest(unittest.TestCase):
    def test(self):
        self.assertRaises(AssertionError, f.Funkcja1('./sdasd/chess', 'whites'))
    def test2(self):
        with self.assertRaises(AssertionError):
            file = open('./sdasd/chess', 'r')
    def test3(self):
        ile = f.Funkcja1("./chess_games.csv", "white")[0]
        procent = f.Funkcja1("./chess_games.csv", "white")[1]
        self.assertEqual(ile, 20058)
        self.assertAlmostEqual(procent, 49.9, places=1)

if __name__ == '__main__':
    unittest.main()
