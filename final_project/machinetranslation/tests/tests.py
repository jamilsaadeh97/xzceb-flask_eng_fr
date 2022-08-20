import unittest
from translator import english_to_french, french_to_english

class TranslatorE2FTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "")
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test3(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TranslatorF2ETest(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "")
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test3(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
    

unittest.main()
