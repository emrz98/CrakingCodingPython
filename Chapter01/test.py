import unittest
from isUnique import isUnique
from checkPermutation import checkPermutation
#664 pdf hints
#101 problems
#abcda badc
#https://dzone.com/articles/vs-code-setup-for-python-development-and-testing
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

class TestCheckPermutation(unittest.TestCase):
    PAIRONE = ("abc", "cba") #permutatino
    PAIRTWO = ("ab", "cd")
    PAIRTHREE = ("abcdef", "abcdef")
    PAIRFOUR = ("aaaabb", "bbaaaa")
    PAIRFIVE = ("a", "a")
    PAIRSIX = ("b", "a")
    PAIRSEVEN = ("kkkkk", "kkkkk" )
# abcdef, abcdef -> true
# aaaabb, bbaaaa -> true
# abcde, bcdef -> false
# a, a -> true
# b,a -> false
# kkkkk, kkkk -> false
    def test_checkPermutation(self):
        self.assertTrue(checkPermutation(self.PAIRONE))
        self.assertFalse(checkPermutation(self.PAIRTWO))
        self.assertTrue(checkPermutation(self.PAIRTHREE))
        self.assertTrue(checkPermutation(self.PAIRFOUR))
        self.assertTrue(checkPermutation(self.PAIRFIVE))
        self.assertFalse(checkPermutation(self.PAIRSIX))
        self.assertTrue(checkPermutation(self.PAIRSEVEN))