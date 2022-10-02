import unittest

#from translator import english_to_french
#from translator import french_to_english

def english_to_french(english_text):
    """Translates English text to French text"""
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    """Translates French text to English text"""
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text


class TestMachineTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if__name__=='__main__':
    unittest.main()