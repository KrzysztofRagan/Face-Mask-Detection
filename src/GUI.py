from functionality import *
import tkinter
import customtkinter
from tkinter import messagebox as mbox

class GUI(tkinter.Tk):

    detect_path = ""

    def __init__(self) -> None:
        super().__init__()
        self.configure(bg = "#339966")
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.geometry("600x600")

        choose_folder_button = customtkinter.CTkButton(master=self, text="WHAT DETECT?", command=self.choose_folder)
        choose_folder_button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        
        detect_button = customtkinter.CTkButton(master=self, text="DETECT", command=self.detect_function)
        detect_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


        show_results_button = customtkinter.CTkButton(master=self, text="SHOW RESULTS", command=self.show_results)
        show_results_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


    def choose_folder(self):
        try:
            self.detect_path = filedialog.askdirectory(initialdir='../ext/yolov5/runs/train/exp/control')
        except Exception as ex:
            print(f'Choosing directory problem: {ex}')




    def detect_function(self):
        self.current_folder = set_folder(self.detect_path)
        print(self.current_folder)
        print(type(self.current_folder))
        detect_function(self.current_folder)
        mbox.showinfo("Information", "Detection finished")


    def show_results(self):
        if sys.platform == "win32":
            os.startfile(results())
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, results()])

app = GUI()

app.mainloop()
