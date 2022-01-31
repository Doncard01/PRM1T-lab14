import unittest
import funkcje as f

class PierwszyTest(unittest.TestCase):
    def test(self):
        ile = f.Funkcja2("./chess_games.csv", "Gambit")[0]
        uniq = f.Funkcja2("./chess_games.csv", "Gambit")[1]
        self.assertEqual(ile, 2518)
        self.assertEqual(uniq, 379)

if __name__ == '__main__':
    unittest.main()