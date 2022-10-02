class TestMachineTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual(englishToFrench("Hello"), "Hello")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test_frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")