from tkinter import *
from tkinter import ttk
class aplicacion():
    __ventana:object
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry("1280x720")
        self.__ventana.title("PySimon - Game")
        
    def ejecutar(self):
        self.__ventana.mainloop()