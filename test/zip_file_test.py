import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, f"{os.path.dirname(test_root)}//src")
sys.path.insert(0, test_root)


from fileutils import list_files, zip_files

class TestFindFiles(unittest.TestCase):

    def test_list_files(self):
        
       files = list_files(source_dir=".\\copied_files", extensions=(".py"))
       print("Numero de arquivos encontrados:", len(files))
       
       zip_files(files_to_zip=files, output_zip="arquivos.zip")
       
       files = list_files(source_dir=".", extensions=(".zip"))
       self.assertTrue(len(files) > 0)
               
if __name__ == '__main__':
    unittest.main()