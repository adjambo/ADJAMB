import unittest
from main import affiche

class TestAffiche(unittest.TestCase):
    def test_affiche_sans_parametre(self):
        # On attend la séquence complète de 1 à 100 sans tronquer
        self.assertEqual(affiche(), 
            "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FrisBee3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FrisBee4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FrisBee6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FrisBee7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FrisBee9192Fizz94BuzzFizz9798FizzBuzz")

if __name__ == '__main__':
    unittest.main()
