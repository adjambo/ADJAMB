import unittest
from main_crypt import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        # Teste le cryptage sans paramètre "pas"
        self.assertEqual(crypt("abc1"), "bcd2")

if __name__ == '__main__':
    unittest.main()

