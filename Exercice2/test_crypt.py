import unittest
from main_crypt import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt_avec_pas(self):
        # Teste le cryptage avec un paramètre de décalage "pas"
        self.assertEqual(crypt("abc1", 2), "cde3")

if __name__ == '__main__':
    unittest.main()


