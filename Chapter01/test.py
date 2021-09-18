import unittest
from isUnique import isUnique
from checkPermutation import checkPermutation
from URLify import urlLyfy
from palindromePermutation import palindromePermutation
from one_away import one_away
from stringCompression import string_compression

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

    def test_checkPermutation(self):
        self.assertTrue(checkPermutation(self.PAIRONE))
        self.assertFalse(checkPermutation(self.PAIRTWO))
        self.assertTrue(checkPermutation(self.PAIRTHREE))
        self.assertTrue(checkPermutation(self.PAIRFOUR))
        self.assertTrue(checkPermutation(self.PAIRFIVE))
        self.assertFalse(checkPermutation(self.PAIRSIX))
        self.assertTrue(checkPermutation(self.PAIRSEVEN))



# "Good for you  ", 14 -> "Good%20for%20you"
# "   Hello world ", 15 ->"Hello%20world"
# "asdfh fghfg fghf asdsd  ", 24 -> "asdfh%20fghfg%20fghf%20asdsd"
# "Emmanuel" , 8 -> "Emmanuel"      
# "Mexico Loose", 12 -> "Mexico%20Loose"  
# "PlayStation vs Xbox" , 19 -> "PlayStation%20vs%20Xbox"  

class TestURLify(unittest.TestCase):
    word_list = ["Good for you  ",
                "   Hello world ", 
                "asdfh fghfg fghf asdsd  ",
                "Emmanuel",
                "Mexico Loose",
                "PlayStation vs Xbox"  ]
    length_list = [12,11,22,8,12,19 ]
    res_list = ["Good%20for%20you", 
                "Hello%20world",
                "asdfh%20fghfg%20fghf%20asdsd",
                "Emmanuel",
                "Mexico%20Loose",
                "PlayStation%20vs%20Xbox"]

    def test_urlLify(self):
        for i in range(6):
            self.assertEqual(self.res_list[i],urlLyfy(self.word_list[i], self.length_list[i]))

class TestPalindromePermutation(unittest.TestCase):
    list_words = [
        "Dont nod",
        "Evil olive",
        "Tact Coa",
        "Amore Roma",
        "Borrow or rob",
        "Draw O coward",
        "Wont lovers revolt now",
        "Stella won no wallets",
        "coat suit",
        "remember the time",
        "man in the mirror",
        "smooth criminal",
        "billie jean",
        "thriller",
        
    ]
    
    def test_palindrome_permutation(self):
        for i in range(8):
            self.assertTrue(palindromePermutation(self.list_words[i]))
        for i in range(8, 14):
            self.assertFalse(palindromePermutation(self.list_words[i]))


class TestOneWay(unittest.TestCase):

    test = [
        {
            "str1" : "pale",
            "str2" : "ple",
            "result" : True
        },
        {
            "str1" : "pales",
            "str2" : "pale",
            "result" : True
        },
        {
            "str1" : "pale",
            "str2" : "bale",
            "result" : True
        },
        {
            "str1" : "pale",
            "str2" : "bake",
            "result" : False
        },
        {
            "str1" : "barco",
            "str2" : "arco",
            "result" : True
        },
        {
            "str1" : "sano",
            "str2" : "sapo",
            "result" : True
        },
        {
            "str1" : "nepe",
            "str2" : "pepe",
            "result" : True
        },
        {
            "str1" : "perro",
            "str2" : "pera",
            "result" : False
        },
    ]

    def test_one_way(self):
        for obj in self.test:
            self.assertEqual(obj["result"], one_away(obj["str1"], obj["str2"]))

class TestStringCompression(unittest.TestCase):
    list_word = [
        "aabcccccaaa",
        "rrrfghtj",
        "rrrgggtttthhhha",
        "aaggtthh",
        "gggaarrhh"
    ]
    list_answer = [
        "a2b1c5a3",
        "rrrfghtj",
        "r3g3t4h4a1",
        "aaggtthh",
        "g3a2r2h2"
    ]
    def test_string_compression(self):
        for i in range(len(self.list_word)):
            self.assertEqual(self.list_answer[i], string_compression(self.list_word[i]))
        
# Dont nod
# Evil olive
# Tact Coa
# Amore Roma
# Borrow or rob
# Draw O coward
# coat suit
# remember the time
# man in the mirror
# smooth criminal
# billie jean
# thriller

