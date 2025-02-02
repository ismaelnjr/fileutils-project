import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, f"{os.path.dirname(test_root)}")
sys.path.insert(0, test_root)

from fileutils import remove_signature, list_files

class TestCase05(unittest.TestCase):

    def test_remove_signature(self):
        
        source_dir = ".\\etc"      
        destination_dir = f"{source_dir}\\sem_assinatura"     
                
        files = list_files(source_dir, extensions=(".txt",), include_sub_dir=True)
        remove_signature(file_list=files, output_dir=destination_dir, verbose=True, encoding="latin-1")
       
               
if __name__ == '__main__':
    unittest.main()