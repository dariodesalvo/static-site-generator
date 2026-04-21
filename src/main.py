import os
import shutil
from helpers.helper import copy_files
from helpers.markdown_html import generate_pages_recursive
      
def main():
    destination_path = os.path.abspath("public")
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    copy_files("static","public")
    generate_pages_recursive("content", "template.html", "public")
    
if __name__ == "__main__":
    main()