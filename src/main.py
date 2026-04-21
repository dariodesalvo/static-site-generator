import os
import sys
import shutil
from helpers.helper import copy_files
from helpers.markdown_html import generate_pages_recursive
      
def main():
    basepath = "/"
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    dir_path_static = "static"
    dir_path_docs = "docs" 
    dir_path_content = "content"
    template_path = "template.html"

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    os.makedirs(dir_path_docs)

    copy_files(dir_path_static, dir_path_docs)
    
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)
    
if __name__ == "__main__":
    main()