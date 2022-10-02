import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
import unittest

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