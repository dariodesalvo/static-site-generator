import unittest
from helpers.markdown_html import extract_title

class TestExtractTitle(unittest.TestCase):
    # Test 1: Caso estándar
    def test_extract_title_base(self):
        md = "# Tolkien Fan Club"
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    # Test 2: Caso sin H1 (debe lanzar excepción)
    def test_extract_title_exception(self):
        md = """
        ## Esto es un H2
        Esto es solo un párrafo.
        """
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "No se encontraron títulos")
        
if __name__ == "__main__":
    unittest.main()