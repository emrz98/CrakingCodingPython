import unittest
from isUnique import isUnique
class TestIsUnique(unittest.TestCase):
    PALABRA1 = "abcde"        # unique
    PALABRA2 = "palabra"      # no unique
    PALABRA3 = "foco"         # no unique
    PALABRA4 = "hospital"     # unique
    PALABRA5 = "ema"          # unique
    PALABRA6 = "palindromo"   # no unique
    PALABRA7 = "submarino"    # unique
    PALABRA8 = "auditores"    # unique

    def test_isUnique(self):
        self.assertTrue(isUnique(self.PALABRA1))
        self.assertTrue(isUnique(self.PALABRA4))
        self.assertTrue(isUnique(self.PALABRA5))
        self.assertTrue(isUnique(self.PALABRA7))
        self.assertTrue(isUnique(self.PALABRA8))

        self.assertFalse(isUnique(self.PALABRA2))
        self.assertFalse(isUnique(self.PALABRA3))
        self.assertFalse(isUnique(self.PALABRA6))
