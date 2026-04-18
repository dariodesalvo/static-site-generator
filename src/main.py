import os
import shutil
from helpers.helper import copy_files
      
def main():
    destination_path = os.path.abspath("public")
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    copy_files("static","public")
    
if __name__ == "__main__":
    main()