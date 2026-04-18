import unittest
from helpers.helper import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractors(unittest.TestCase):
    
    # --- Tests para IMÁGENES ---
    
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![one](https://url1.com/1.png) and ![two](https://url2.com/2.gif)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("one", "https://url1.com/1.png"), ("two", "https://url2.com/2.gif")], 
            matches
        )

    def test_extract_images_no_images(self):
        # Un link normal NO debe ser detectado como imagen
        text = "This is a [link](https://boot.dev) but no image."
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    # --- Tests para LINKS ---

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_multiple_links(self):
        text = "Check [Google](https://google.com) and [Youtube](https://youtube.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("Google", "https://google.com"), ("Youtube", "https://youtube.com")], 
            matches
        )



if __name__ == "__main__":
    unittest.main()