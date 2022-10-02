import os
import unittest
from ibm-watson import LanguageTranslatorV3
from ibm-cloud-sdk-core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

from translator import english_to_french
from translator import french_to_english

class TestMachineTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()