import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, f"{os.path.dirname(test_root)}")
sys.path.insert(0, test_root)

from fileutils import organize_files

class TestCase05(unittest.TestCase):

    def organize_test(self):
        
        organize_files(source_dir=".\\etc", 
                       destination_dir=".\\organized_files", 
                       copy=True,
                       verbose=True)
       
               
if __name__ == '__main__':
    unittest.main()