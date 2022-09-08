from functionality import *
import tkinter
import customtkinter
from tkinter import messagebox as mbox

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x600")

detect_button = customtkinter.CTkButton(master=app, text="DETECT", command=detect_function)
detect_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

choose_folder_button = customtkinter.CTkButton(master=app, text="WHAT DETECT?", command=choose_folder)
choose_folder_button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


show_results_button = customtkinter.CTkButton(master=app, text="SHOW RESULTS", command=show_results)
show_results_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()