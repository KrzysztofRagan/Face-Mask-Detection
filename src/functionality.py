import subprocess
import os, sys, glob
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mbox

detect_path = ('./yolov5/runs/train/exp/control')




def choose_folder():
    global detect_path
    folder_path = StringVar()
    try:
      detect_path = filedialog.askdirectory(initialdir=detect_path)
    except Exception as ex:
      print(f'Choosing directory problem: {ex}')
    folder_path.set(detect_path)
    print(detect_path)

def detect_function():
  try:
    subprocess.call(['python3.10', './yolov5/detect.py', '--source', detect_path, '--weights', './yolov5/runs/train/exp/weights/best.pt'])
    mbox.showinfo("Information", "Detection finished")
  except Exception as ex:
    print(f'Detection problem {ex}')

def show_results():
    folder_list = os.listdir('./yolov5/runs/detect')
    list_of_folders = glob.glob('./yolov5/runs/detect/*')
    show_results.latest_folder = max(list_of_folders, key=os.path.getctime)

    if sys.platform == "win32":
        os.startfile(show_results.latest_folder)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, show_results.latest_folder])

