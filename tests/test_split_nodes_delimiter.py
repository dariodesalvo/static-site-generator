from src.textnode import TextNode, TextType
from helpers.helper import split_nodes_delimiter
import unittest

class TestSplitDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("Esto tiene `code block` aquí", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Esto tiene ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" aquí", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_bold(self):
        node = TextNode("Texto con **negrita** al final", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Texto con ", TextType.TEXT),
            TextNode("negrita", TextType.BOLD),
            TextNode(" al final", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_double(self):
        node = TextNode("Uno `code` dos `code` tres", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)

    def test_exception_unclosed(self):
        node = TextNode("Esto no cierra **negrita", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()