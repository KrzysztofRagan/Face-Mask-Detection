import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "src"))
from functionality import *
import unittest

class Detection_function_test(unittest.TestCase):

    def test_proper_path(self):
        assert detect_function('/Users/krzysztofragan/Desktop/vscode/Face Mask Detection/ext/yolov5/runs/train/exp/control') == True

    def test_no_path(self):
        assert detect_function('') == False
    
    def test_polish_characters(self):
        assert detect_function('/Users/krzysztofragan/Desktop/vscode/demo1/polish_łćążźć') == True

    def test_wrong_path(self):
        assert detect_function('wrong_path') == False

    
if __name__ == '__main__':
    unittest.main()
