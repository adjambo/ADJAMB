import unittest
from main import affiche

class TestAffiche(unittest.TestCase):
    def test_affiche_avec_parametre(self):
        
        self.assertEqual(affiche(15), 
            "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")

if __name__ == '__main__':
    unittest.main()
