import subprocess
import tkinter
import customtkinter
from tkinter import filedialog
from tkinter import *
import os, sys, glob


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x600")

def choose_folder():
    global detect_path
    folder_path = StringVar()
    detect_path = filedialog.askdirectory()
    folder_path.set(detect_path)
    print(detect_path)

def detect_function():
    print("button pressed")
    subprocess.call(['python3.10', './yolov5/detect.py', '--source', detect_path, '--weights', './yolov5/runs/train/exp/weights/best.pt'])

# def show_results():
    # subprocess.Popen(r'./yolov5/runs/detect/exp2', shell=True)


def show_results():
    folder_list = os.listdir('./yolov5/runs/detect')
    list_of_folders = glob.glob('./yolov5/runs/detect/*')
    latest_folder = max(list_of_folders, key=os.path.getctime)

    if sys.platform == "win32":
        os.startfile(latest_folder)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, latest_folder])

detect_path = str()

# Use CTkButton instead of tkinter Button
detect_button = customtkinter.CTkButton(master=app, text="DETECT", command=detect_function)
detect_button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

choose_folder_button = customtkinter.CTkButton(master=app, text="WHAT DETECT?", command=choose_folder)
choose_folder_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

show_results_button = customtkinter.CTkButton(master=app, text="SHOW RESULTS", command=show_results)
show_results_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()






    # subprocess.call(['python3.10', './yolov5/detect.py', '--source', './yolov5/runs/train/exp/control', '--weights', './yolov5/runs/train/exp/weights/best.pt'])