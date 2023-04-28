import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    
    def test_englishToFrench(self):
        # Test null input
        self.assertEqual(englishToFrench(None), None)
        
        # Test translati
        # on of "Hello"
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        
    def test_frenchToEnglish(self):
        # Test null input
        self.assertEqual(frenchToEnglish(None), None)
        # Test translation of "Bonjour"
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        
if __name__ == '__main__':
    unittest.main()

    