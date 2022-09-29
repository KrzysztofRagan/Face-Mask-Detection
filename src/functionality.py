import subprocess
import os, sys, glob
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mbox

"""
Functionality contains:
- choosing folder - in which photos will be detected
- detection - process of detection of chosen folder
- results - the folder will be opened with results
"""

def set_folder(try_path):
    try:
      detect_path = try_path
    except:
      detect_path = ('../ext/yolov5/runs/train/exp/control')
      print('Default path. No chosen path.')
    if detect_path == "":
      detect_path = ('../ext/yolov5/runs/train/exp/control')

    return detect_path

def detect_function(detect_path):
  try:
    subprocess.call(['python3.10', '../ext/yolov5/detect.py', '--source', detect_path, '--weights', '../ext/yolov5/runs/train/exp/weights/best.pt'])
  except Exception as ex:
    print(f'Detection problem {ex}')

def results():
    list_of_folders = glob.glob('../ext/yolov5/runs/detect/*')
    results.latest_folder = max(list_of_folders, key=os.path.getctime)
    return results.latest_folder


