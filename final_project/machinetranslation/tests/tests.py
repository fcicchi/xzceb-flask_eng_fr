import unittest
from translator import english_to_french, french_to_english

class TestsEnglishToFrench(unittest.TestCase):
    """
    Class to test the function englishToFrench
    """
    def testForNone(self):
        """
        Function to test the function englishToFrench for None
        """
        self.assertIsNone(english_to_french(None))

    def testHello(self):
        """
        Function to test the function englishToFrench for Hello
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestsFrenchToEnglish(unittest.TestCase):
    """
    Class to test the function frenchToEnglish
    """
    def testForNone(self):
        """
        Function to test the function frenchToEnglish for None
        """
        self.assertIsNone(french_to_english(None))

    def testForBonjour(self):
        """
        Function to test the function frenchToEnglish for Bonjour
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()