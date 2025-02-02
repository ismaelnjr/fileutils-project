import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, f"{os.path.dirname(test_root)}")
sys.path.insert(0, test_root)

from fileutils import list_files, copy_files

class TestCase02(unittest.TestCase):

    def test_copy_files(self):
        
       files = list_files(source_dir=".", extensions=(".py"))
       print("Numero de arquivos encontrados:", len(files))
       self.assertTrue(len(files) > 0)
       
       num_files = len(files)
       
       copy_files(file_list=files, destination_dir="copied_files")
       
       copied_files = list_files(source_dir="copied_files", extensions=(".py"))
       print("Numero de arquivos copiados:", len(copied_files))
       self.assertTrue(len(copied_files) == num_files)
               
if __name__ == '__main__':
    unittest.main()