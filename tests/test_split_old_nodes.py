import unittest
from src.textnode import TextNode, TextType
from helpers.helper import split_nodes_image, split_nodes_link    

class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_links_multiple(self):
        node = TextNode(
            "Links: [one](url1), [two](url2)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Links: ", TextType.TEXT),
                TextNode("one", TextType.LINK, "url1"),
                TextNode(", ", TextType.TEXT),
                TextNode("two", TextType.LINK, "url2"),
            ],
            new_nodes,
        )
        
if __name__ == "__main__":
    unittest.main()