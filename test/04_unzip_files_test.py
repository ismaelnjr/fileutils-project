import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, f"{os.path.dirname(test_root)}")
sys.path.insert(0, test_root)

from fileutils import unzip_files, list_files

class TestCase04(unittest.TestCase):

    def test_unzip_files(self):

       unzip_files(zip_file="arquivos.zip", extract_to="unzipped_files")
       
       files = list_files(source_dir="unzipped_files", extensions=(".py"), include_sub_dir=True)
       print("Numero de arquivos encontrados:", len(files))
       self.assertTrue(len(files) > 0)
               
if __name__ == '__main__':
    unittest.main()