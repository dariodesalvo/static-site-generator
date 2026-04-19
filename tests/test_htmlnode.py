import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from helpers.markdown_html import markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "google.com", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", "TextType.LINK.value")
        self.assertEqual(repr(node), "HTMLNode(p, TextType.LINK.value, None, None)")
        
    def test_type(self):
        node = HTMLNode("a", "This is a text node", None, "TextType=BOLD")
        node2 = HTMLNode("j", "This is a text node", None, "TextType=LINK")
        self.assertNotEqual(node, node2)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)
        
                    

if __name__ == "__main__":
    unittest.main()