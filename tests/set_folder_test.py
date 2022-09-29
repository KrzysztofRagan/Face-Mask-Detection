import sys
sys.path.insert(1, '../src')
from functionality import *
import unittest


class Set_folder_test(unittest.TestCase):

    def test_proper_path(self):
        assert(set_folder('/Users/krzysztofragan/Desktop/vscode/Face Mask Detection/tests') == '/Users/krzysztofragan/Desktop/vscode/Face Mask Detection/tests')

    def test_no_path(self):   
        assert (set_folder('') == '../ext/yolov5/runs/train/exp/control')
    
    def test_wrong_path(self):     
        assert (set_folder('wrong_path') == '../ext/yolov5/runs/train/exp/control')

    def test_path_with_polish_characters(self):
        assert (set_folder('/Users/krzysztofragan/Desktop/vscode/demo1/polish_łćążźć') == '/Users/krzysztofragan/Desktop/vscode/demo1/polish_łćążźć')


    def test_argument_type_int(self):       
        assert (set_folder(123) == '../ext/yolov5/runs/train/exp/control')

if __name__ == '__main__':
    unittest.main()