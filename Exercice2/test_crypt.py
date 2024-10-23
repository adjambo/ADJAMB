import unittest
from main_crypt import crypt, decrypt

class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        self.assertEqual(crypt("abc1"), "bcd2")
    
    def test_crypt_avec_pas(self):
        self.assertEqual(crypt("abc1", 2), "cde3")

    def test_decrypt(self):
        # Teste le décryptage pour obtenir le message original
        self.assertEqual(decrypt("bcd2"), "abc1")

if __name__ == '__main__':
    unittest.main()