import tkinter as tk

class aplicacion(tk.Tk):
    __boton_verde:object
    __boton_rojo:object
    __boton_amarillo:object
    __boton_azul:object
    __marcador:object
    __texto_puntuacion:object

    def __init__(self):
        #esto es la ventana
        super().__init__()
        self.configure(bg='Black')
        self.geometry("800x600")
        self.title("PySimon - Game")
        
        #esto es para el marcador de puntos
        self.__marcador = tk.LabelFrame(self, width='600', height='20')
        self.__marcador.grid(row=0, column=0,columnspan=2,sticky='we', ipady=50, ipadx=50, padx=10, pady=10)
        
        #esto es para poner el texto "Puntuación"
        self.__texto_puntuacion = ('Arial', 14)
        label = tk.Label(self.__marcador, text='Puntuación', font=self.__texto_puntuacion)
        label.pack(expand=True, fill='both')

        #estos son los botones de colores
        self.__boton_verde = tk.Canvas(self, width=300, height=200, bg="#00FF00")
        self.__boton_rojo = tk.Canvas(self, width=300, height=200, bg="#FF0000")
        self.__boton_amarillo = tk.Canvas(self, width=300, height=200, bg="#FFFF00")
        self.__boton_azul = tk.Canvas(self, width=300, height=200, bg="#0000FF")
        #posicionamiento de los botones
        self.__boton_verde.grid(row=1, column=0, sticky='nswe', ipady=50, ipadx=50, padx=10, pady=10)
        self.__boton_rojo.grid(row=1, column=1, sticky='nswe', ipady=50, ipadx=50, padx=10, pady=10)
        self.__boton_amarillo.grid(row=2, column=0, sticky='nswe', ipady=50, ipadx=50, padx=10, pady=10)
        self.__boton_azul.grid(row=2, column=1, sticky='nswe', ipady=50, ipadx=50, padx=10, pady=10)
        #para que mantengan la proporcion de tamaño
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def ejecutar(self):
        self.mainloop()