import unittest
from main import affiche

class TestAffiche(unittest.TestCase):
    def test_affiche_avec_deux_parametre(self):

        self.assertEqual(affiche(5, 10), 
            "BuzzFizz78FizzBuzz")
        
        self.assertEqual(affiche(10, 16), 
            "Buzz11Fizz1314FrisBee16")

if __name__ == '__main__':
    unittest.main()
