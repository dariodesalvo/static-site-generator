import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node
from helpers.helper import text_to_textnodes
from helpers.block_functions import markdown_to_blocks

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is some anchor text", TextType.LINK.value, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is some anchor text, link, https://www.boot.dev)")
        
    def test_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)
        
    def test_text_node_to_html_node_text(self):
        node = TextNode("Solo texto", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Solo texto")
        
    def test_text_to_textnodes_full(self):
        text = "Este es un texto con **negrita**, _itálica_, un `bloque de código`, una ![imagen](https://i.imgur.com/zjjcJKZ.png) y un [enlace](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Este es un texto con ", TextType.TEXT),
            TextNode("negrita", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("itálica", TextType.ITALIC),
            TextNode(", un ", TextType.TEXT),
            TextNode("bloque de código", TextType.CODE),
            TextNode(", una ", TextType.TEXT),
            TextNode("imagen", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" y un ", TextType.TEXT),
            TextNode("enlace", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(expected, nodes)
        
    def test_markdown_to_blocks(self):
                md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
                blocks = markdown_to_blocks(md)
                self.assertEqual(
                    blocks,
                    [
                        "This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items",
                    ],
                )
        

if __name__ == "__main__":
    unittest.main()