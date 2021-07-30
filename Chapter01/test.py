import unittest
from isUnique import isUnique, isUniqueTwoFors, isUniqueVector

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

    def test_isUniqueFors(self):
        self.assertTrue(isUniqueTwoFors(self.PALABRA1))
        self.assertTrue(isUniqueTwoFors(self.PALABRA4))
        self.assertTrue(isUniqueTwoFors(self.PALABRA5))
        self.assertTrue(isUniqueTwoFors(self.PALABRA7))
        self.assertTrue(isUniqueTwoFors(self.PALABRA8))

        self.assertFalse(isUniqueTwoFors(self.PALABRA2))
        self.assertFalse(isUniqueTwoFors(self.PALABRA3))
        self.assertFalse(isUniqueTwoFors(self.PALABRA6))

    def test_isUniqueVector(self):
        self.assertTrue(isUniqueVector(self.PALABRA1))
        self.assertTrue(isUniqueVector(self.PALABRA4))
        self.assertTrue(isUniqueVector(self.PALABRA5))
        self.assertTrue(isUniqueVector(self.PALABRA7))
        self.assertTrue(isUniqueVector(self.PALABRA8))

        self.assertFalse(isUniqueVector(self.PALABRA2))
        self.assertFalse(isUniqueVector(self.PALABRA3))
        self.assertFalse(isUniqueVector(self.PALABRA6))
