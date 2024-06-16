import tkinter as tk
import random
from tkinter import IntVar, messagebox
from datetime import datetime
import json

class aplicacion(tk.Tk):
    #botones
    __boton_verde:object
    __boton_rojo:object
    __boton_amarillo:object
    __boton_azul:object
    __botones:list
    __colores:list
    __boton_iluminado:list
    __lista_botones:list            #son los botones que se van a iluminar
    __lista_botones_usuario:list    #son los botones que va a ir pulsando el usuario
    #ventana game over
    __game_over:object
    __texto_game_over:object
    __texto_con_el_puntaje:object
    __puntaje_final:object
    __boton_reintenar:object
    __boton_salir:object
    #texto de arriba de la ventana que muestra usuario y puntaje
    __marcador:object
    __label_texto_puntaje:object
    __label_contador_puntos:object
    __contador_puntos:IntVar
    __texto_reemplazable:object
    #para el segundo inciso:
    __Ventana_Nombre_de_usuario:object
    __label_ingresar_nombre:object
    __entry_nombre:object
    __boton_confirmar:object
    __Nombre_de_usuario:str
    __datos:list
    def __init__(self):
        #esto es la ventana
        super().__init__()
        self.configure(bg='Black')
        self.geometry("600x700")
        self.title("PySimon - Game")
        #esto es para el marcador de puntos
        self.__marcador = tk.LabelFrame(self, width='600', height='20')
        self.__marcador.grid(row=0, column=0, columnspan=2, sticky='nswe', ipady=50, ipadx=50, pady=10, padx=10)
        fuente = ('Arial', 20)    
        #esto es para poner el nombre del usuario 
        self.__texto_reemplazable=tk.StringVar()
        self.__texto_reemplazable.set('')
        self.__label_texto_puntaje = tk.Label(self.__marcador, textvariable=self.__texto_reemplazable, font=fuente)
        self.__label_texto_puntaje.pack(side='left', ipadx='100')
        #esto para poner la puntuación
        self.__contador_puntos = IntVar(value=0)
        self.__label_contador_puntos=tk.Label(self.__marcador, textvariable=self.__contador_puntos, font=fuente)
        self.__label_contador_puntos.pack(side='right', ipadx='100')
        #estos son los botones de colores
        self.__boton_verde = tk.Canvas(self, width=230, height=300, bg="#004d00")
        self.__boton_rojo = tk.Canvas(self, width=230, height=300, bg="#4d0000")
        self.__boton_amarillo = tk.Canvas(self, width=230, height=300, bg="#4d4d00")
        self.__boton_azul = tk.Canvas(self, width=230, height=300, bg="#00004d")
        self.__boton_iluminado=None
        #aquí se van a guardar los botones que se iluminan para reproducirlos del primero al nuevo que se agrega
        #se establece una lista que va a guardar los botones que clickee el usuario
        self.__lista_botones=[]
        self.__lista_botones_usuario=[]
        #lista de botones y colores
        self.__botones = [self.__boton_verde, self.__boton_rojo, self.__boton_amarillo, self.__boton_azul]
        self.__colores = ["#00FF00", "#FF0000", "#FFFF00", "#0000FF"]
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
        #Para ventana game over
        self.__game_over=tk.LabelFrame(self, width=300, height=250)
        self.__game_over.place(relx=0.5, rely=0.5, anchor='center')
        self.__texto_game_over=tk.Label(self.__game_over, text='GAME OVER', font=('Arial', 20))
        self.__texto_game_over.grid(row=0, column=0, columnspan=3,sticky='nswe', ipady=10, ipadx=10)
        self.__texto_con_el_puntaje=tk.StringVar()
        self.__texto_con_el_puntaje.set('')
        self.__puntaje_final=tk.Label(self.__game_over, textvariable=self.__texto_con_el_puntaje, font=('Arial', 14))
        self.__puntaje_final.grid(row=1, column=0, columnspan=3, sticky='nswe', ipady=10, ipadx=10)
        self.__boton_salir=tk.Button(self.__game_over, text='Salir', font=('Arial', 12), command=self.destroy)
        self.__boton_salir.grid(row=3,column=2,sticky='nswe', ipady=10, ipadx=10)
        self.__boton_reintenar=tk.Button(self.__game_over, text='Volver a intentar', font=('Arial',12), command=self.reintentar)
        self.__boton_reintenar.grid(row=3,column=0,sticky='nswe', ipady=10, ipadx=10)
        self.__game_over.place_forget()
        #item2
        fuente2=('Arial', 9)
        self.__Ventana_Nombre_de_usuario=tk.LabelFrame(self, text='Datos del Jugador', font=fuente2, width= 220, height=200)
        self.__Ventana_Nombre_de_usuario.place(relx=0.5, rely=0.5, anchor='center')
        self.__label_ingresar_nombre=tk.Label(self.__Ventana_Nombre_de_usuario, text='Jugador', font=fuente2)
        self.__label_ingresar_nombre.grid(row=0, column=0, sticky='nswe', ipadx=5, ipady=5, padx=5, pady=5)
        self.__entry_nombre=tk.Entry(self.__Ventana_Nombre_de_usuario)
        self.__entry_nombre.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
        self.__boton_confirmar=tk.Button(self.__Ventana_Nombre_de_usuario, text='Iniciar Juego',font=fuente2,command=self.guardar_Usuario)
        self.__boton_confirmar.grid(row=2, column=2, sticky='nswe', padx=5, pady=5)
        self.__Ventana_Nombre_de_usuario.wait_window()

        
    def comienzo(self):
        self.__lista_botones.append(random.randint(0, 3))       #genera un número random de entre 4 y, dependiendo de cuál se generó, se prende un boton u otro
        self.__lista_botones_usuario.clear()                    #limpia la lista del anterior juego
        self.iluminar_secuencia(0)

    def iluminar_secuencia(self, indice):
        if indice < len(self.__lista_botones):
            boton_num = self.__lista_botones[indice]
            boton = self.__botones[boton_num]
            self.cambiar_color(boton, boton_num)
            self.after(700, lambda: self.iluminar_secuencia(indice + 1))
        else:
            self.__boton_iluminado = None  

    def apretar_boton(self, boton_elegido):
        if self.__boton_iluminado is None:  
            if boton_elegido in self.__botones:                 #si el boton que clickeo es uno de los 4 botones
                numero = self.__botones.index(boton_elegido)    #asigna la posición en la lista de ese botón elegido
                self.__lista_botones_usuario.append(numero)     
                if self.__lista_botones_usuario == self.__lista_botones[:len(self.__lista_botones_usuario)]:
                    self.cambiar_color(boton_elegido, numero)
                    if len(self.__lista_botones_usuario) == len(self.__lista_botones):
                        self.__contador_puntos.set(self.__contador_puntos.get() + 1)
                        self.after(1000, self.comienzo)
                else:
                    self.guardar_json()
                    self.llamar_gameover()
                    

    def detectar_clic(self, event):
        boton_clicado = event.widget
        self.apretar_boton(boton_clicado)

    def cambiar_color(self,boton,num):
        col_original=boton.cget("bg")
        boton.configure(bg=self.__colores[num])
        boton.after(300, lambda: boton.configure(bg=col_original))

    def llamar_gameover(self):
        for boton in self.__botones:            #cuando muestra la pantalla de game over, desvincula el evento de click de los canvas.
            boton.unbind("<Button-1>")          #esto lo hace para que, si está esa pantalla, no puedas darle click a los botones de fondo. sino, en el json detecta que sigue perdiendo y sigue escribiendo el mismo dato
        self.__texto_con_el_puntaje.set(f"Puntuación: {self.__contador_puntos.get()}")
        self.__game_over.place(relx=0.5, rely=0.5, anchor='center')
    
    def reintentar(self):
        for boton in self.__botones:
            boton.bind("<Button-1>", self.detectar_clic)
        self.__lista_botones.clear()
        self.__contador_puntos.set(0)
        self.__game_over.place_forget()
        self.ejecutar()

    def guardar_Usuario(self):
        self.__Nombre_de_usuario=self.__entry_nombre.get()
        self.__Ventana_Nombre_de_usuario.destroy()
        self.__texto_reemplazable.set(self.__Nombre_de_usuario)
        for boton in self.__botones:
            boton.bind("<Button-1>", self.detectar_clic)
        self.ejecutar()

    def guardar_json(self):
        with open('psymonpuntajes.json', 'r+') as archivo:
            if not archivo.read(1):                #para ver si está vacío
                self.__datos = []                  #si lo está, inicia la lista vacía
            else:               
                archivo.seek(0)                   #se pone al inicio de nuevo
                self.__datos=json.load(archivo)   #lee lo que tiene el archivo
            self.__datos.append(self.to_dict())   #agrega un diccionario con los datos pedidos
            archivo.seek(0)                       #se vuelve a posicionar al inicio para sobreescribir
            json.dump(self.__datos, archivo, indent=4)  #carga la nueva lista de datos
            archivo.truncate()                    #se usa para reducir el tamaño al mínimo posible y evitar que queden espacios vacíos debajo del contenido

    def to_dict(self):                            #diccionario con los datos del jugador
        fechayhora=datetime.now()
        fechayhora=fechayhora.strftime("%d/%m/%Y %H:%M:%S")
        if self.__Nombre_de_usuario=='':
            self.__Nombre_de_usuario='Jugador'
        return{
            'Usuario': self.__Nombre_de_usuario,
            'Fecha y hora': fechayhora,
            'Puntaje': self.__contador_puntos.get()
        }

    def ejecutar(self):
        self.after(1500, self.comienzo)
        self.mainloop()

if __name__=='__main__':
    app=aplicacion()
    app.mainloop()
