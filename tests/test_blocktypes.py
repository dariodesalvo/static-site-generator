import unittest
from helpers.block_functions import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        # Casos válidos de encabezados
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        # Casos inválidos (deberían ser párrafos)
        self.assertEqual(block_to_block_type("####### Too many hashes"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#No space after hash"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        code_block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        # Código mal cerrado o mal abierto
        self.assertEqual(block_to_block_type("``not enough backticks```"), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        quote_block = "> This is a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)
        # Una línea falla, todo el bloque es párrafo
        bad_quote = "> First line ok\nSecond line fails"
        self.assertEqual(block_to_block_type(bad_quote), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        ul = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)
        # Sin espacio después del guion
        bad_ul = "-Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(bad_ul), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)
        # Número incorrecto (no incrementa en 1)
        bad_seq = "1. First\n3. Third"
        self.assertEqual(block_to_block_type(bad_seq), BlockType.PARAGRAPH)
        # No empieza en 1
        start_wrong = "2. Second\n3. Third"
        self.assertEqual(block_to_block_type(start_wrong), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        text = "Just a normal paragraph of text."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()