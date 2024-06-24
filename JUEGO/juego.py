import tkinter as tk
import random
from tkinter import IntVar, scrolledtext
from datetime import datetime
import json
from functools import partial
from gestorjugador import gestor_jugadores
class aplicacion(tk.Tk):
    #botones
    __boton_verde:object
    __boton_rojo:object
    __boton_amarillo:object
    __boton_azul:object
    __botones:list
    __colores:list
    __boton_iluminado:list
    __lista_botones:list            
    __lista_botones_usuario:list    
    #ventana game over
    __game_over:object
    __texto_game_over:object
    __texto_con_el_puntaje:object
    __puntaje_final:object
    __boton_reintenar:object
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
    #para el tercer inciso:
    __menu_puntaje:object
    __boton_abrir_menu:object
    __frame_puntaje:object
    __boton_salida_menu:object
    __boton_puntaje:object
    __lista_jugadores:object
    __pantalla_puntajes:object
    __label_texto_datos:object
    __boton_cerrar:object
    def __init__(self):
        #esto es la ventana
        super().__init__()
        self.configure(bg='Black')
        ancho=self.winfo_screenwidth()
        alto=self.winfo_screenheight()
        tamaño=f'{ancho // 2}x{alto}+{ancho // 2}+0'
        self.geometry(tamaño)
        self.title("PySimon - Game")
        #esto es para el marcador de puntos
        self.__marcador = tk.LabelFrame(self, width='600', height='20')
        self.__marcador.grid(row=1, column=0, columnspan=2, sticky='nswe', ipady=50, ipadx=50, pady=10, padx=10)
        fuente = ('Arial', 20)    
        #esto es para poner el nombre del usuario 
        self.__texto_reemplazable=tk.StringVar()
        self.__texto_reemplazable.set('')
        self.__label_texto_puntaje = tk.Label(self.__marcador, textvariable=self.__texto_reemplazable, font=fuente)
        self.__label_texto_puntaje.pack(side='left', ipadx='70')
        #esto para poner la puntuación
        self.__contador_puntos = IntVar(value=0)
        self.__label_contador_puntos=tk.Label(self.__marcador, textvariable=self.__contador_puntos, font=fuente)
        self.__label_contador_puntos.pack(side='right', ipadx='70')
        
        self.__boton_verde = tk.Canvas(self, width=230, height=300, bg="#004d00")
        self.__boton_rojo = tk.Canvas(self, width=230, height=300, bg="#4d0000")
        self.__boton_amarillo = tk.Canvas(self, width=230, height=300, bg="#4d4d00")
        self.__boton_azul = tk.Canvas(self, width=230, height=300, bg="#00004d")
        self.__boton_iluminado=None

        self.__lista_botones=[]
        self.__lista_botones_usuario=[]
        
        self.__botones = [self.__boton_verde, self.__boton_rojo, self.__boton_amarillo, self.__boton_azul]
        self.__colores = ["#00FF00", "#FF0000", "#FFFF00", "#0000FF"]
        
        self.__boton_verde.grid(row=2, column=0, sticky='nswe', ipady=50, ipadx=50, padx=7, pady=7)
        self.__boton_rojo.grid(row=2, column=1, sticky='nswe', ipady=50, ipadx=50, padx=7, pady=7)
        self.__boton_amarillo.grid(row=3, column=0, sticky='nswe', ipady=50, ipadx=50, padx=7, pady=7)
        self.__boton_azul.grid(row=3, column=1, sticky='nswe', ipady=50, ipadx=50, padx=7, pady=7)
        #para que mantengan la proporcion de tamaño
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        #Para ventana game over
        self.__game_over=tk.LabelFrame(self, width=300, height=250, bg='grey')
        self.__game_over.place(relx=0.5, rely=0.5, anchor='center')
        self.__texto_game_over=tk.Label(self.__game_over, text='GAME OVER', font=('Arial', 20))
        self.__texto_game_over.grid(row=0, column=0, columnspan=3,sticky='nswe', ipady=10, ipadx=10)
        self.__texto_con_el_puntaje=tk.StringVar()
        self.__texto_con_el_puntaje.set('')
        self.__puntaje_final=tk.Label(self.__game_over, textvariable=self.__texto_con_el_puntaje, font=('Arial', 14))
        self.__puntaje_final.grid(row=1, column=0, columnspan=3, sticky='nswe', ipady=10, ipadx=10)
        self.__boton_reintenar=tk.Button(self.__game_over, text='Volver a intentar', font=('Arial',12), command=self.reintentar)
        self.__boton_reintenar.grid(row=3,column=0,columnspan=3,sticky='nswe', ipady=10, ipadx=10)
        self.__boton_reintenar.bind('<Enter>', self.on_enter)
        self.__boton_reintenar.bind('<Leave>', self.on_leave)
        self.__game_over.place_forget()
        fuente2=('Arial', 10)
        #item3
        self.__menu_puntaje=tk.Label(self,text='',font=fuente2, height=7, anchor='w', bg='white')
        self.__menu_puntaje.grid(row=0, column=0,columnspan=2, sticky='nswe')
        self.__frame_puntaje=tk.LabelFrame(self,text='====================', font=fuente2, width='150', height='100', relief='flat')
        self.__frame_puntaje.place(y=26, anchor='nw')
        self.__boton_salida_menu=tk.Button(self.__frame_puntaje, text='Salir', font=fuente2, command=self.destroy, anchor='w')
        self.__boton_salida_menu.pack(side='bottom', fill='x')
        self.__boton_salida_menu.bind('<Enter>', self.on_enter)
        self.__boton_salida_menu.bind('<Leave>', self.on_leave)
        self.__boton_puntaje=tk.Button(self.__frame_puntaje, text='Ver puntajes', font=fuente2, anchor='w', command=self.mostrar_puntajes)
        self.__boton_puntaje.pack(side='top', fill='x')
        self.__boton_puntaje.bind('<Enter>', self.on_enter)
        self.__boton_puntaje.bind('<Leave>', self.on_leave)
        self.__frame_puntaje.place_forget()
        self.__boton_abrir_menu = tk.Button(self.__menu_puntaje, text='Puntajes', font=fuente2, command=self.mostrar_menu, anchor='w', bg='white', relief='flat', borderwidth=0)
        self.__boton_abrir_menu.place(anchor='nw')
        self.__boton_abrir_menu.config(state='disabled')
        #item 3, puntajes
        self.__pantalla_puntajes=tk.LabelFrame(self, text='Galeria de puntos', font=('Arial', 15))
        self.__pantalla_puntajes.place(relx=0.5, rely=0.5, anchor='center',width=500, height=400)
        self.__label_texto_datos=tk.Label(self.__pantalla_puntajes, text=f'Jugador                Fecha                   Hora                   Puntaje', font=('Arial', 12), height=2, anchor='w')
        self.__label_texto_datos.pack(anchor='center')
        self.__lista_jugadores=scrolledtext.ScrolledText(self.__pantalla_puntajes, width=500, height=18)
        self.__lista_jugadores.pack(side='top')
        self.__boton_cerrar=tk.Button(self.__pantalla_puntajes, text='Cerrar', font=('Arial', 10), command=self.__pantalla_puntajes.place_forget)
        self.__boton_cerrar.pack(side='bottom')
        self.__pantalla_puntajes.place_forget()
        #item2
        self.__Ventana_Nombre_de_usuario=tk.LabelFrame(self, text='Datos del Jugador', font=fuente2, width= 220, height=200)
        self.__Ventana_Nombre_de_usuario.place(relx=0.5, rely=0.5, anchor='center')
        self.__label_ingresar_nombre=tk.Label(self.__Ventana_Nombre_de_usuario, text='Jugador', font=fuente2)
        self.__label_ingresar_nombre.grid(row=0, column=0, sticky='nswe', ipadx=5, ipady=5, padx=5, pady=5)
        limite=(self.register(self.limite_caracteres), '%P')
        self.__entry_nombre=tk.Entry(self.__Ventana_Nombre_de_usuario, validate='key', validatecommand=limite, font=fuente2)
        self.__entry_nombre.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
        self.__boton_confirmar=tk.Button(self.__Ventana_Nombre_de_usuario, text='Iniciar Juego',font=fuente2,command=self.guardar_Usuario)
        self.__boton_confirmar.grid(row=2, column=2, sticky='nswe', padx=5, pady=5)
        self.__boton_confirmar.bind('<Enter>', self.on_enter)
        self.__boton_confirmar.bind('<Leave>', self.on_leave)
        self.__Ventana_Nombre_de_usuario.wait_window()
        
    def comienzo(self):
        self.__lista_botones.append(random.randint(0, 3))       
        self.__lista_botones_usuario.clear()                    
        self.iluminar_secuencia(0)

    def iluminar_secuencia(self, indice):
        if indice < len(self.__lista_botones):
            boton_num = self.__lista_botones[indice]
            boton = self.__botones[boton_num]
            self.cambiar_color(boton, boton_num)
            self.after(700, partial(self.iluminar_secuencia, indice + 1))
        else:
            self.__boton_iluminado = None  

    def apretar_boton(self, boton_elegido):
        if self.__boton_iluminado is None:  
            if boton_elegido in self.__botones:                 
                numero = self.__botones.index(boton_elegido)
                self.__lista_botones_usuario.append(numero)     
                if self.__lista_botones_usuario == self.__lista_botones[:len(self.__lista_botones_usuario)]:
                    self.cambiar_color(boton_elegido, numero)
                    if len(self.__lista_botones_usuario) == len(self.__lista_botones):
                        self.__contador_puntos.set(self.__contador_puntos.get() + 1)
                        self.after(1000, self.comienzo)
                else:
                    self.guardar_json()
                    self.__boton_abrir_menu.config(state='normal')
                    self.__boton_abrir_menu.bind('<Enter>', self.on_enter)
                    self.__boton_abrir_menu.bind('<Leave>', self.on_leave)
                    self.llamar_gameover()
                    
    def detectar_clic(self, event):
        boton_clicado = event.widget
        self.apretar_boton(boton_clicado)
    
    def on_enter(self,boton):
        boton.widget.config(bg='light blue')
    def on_leave(self,boton):
        boton.widget.config(bg='SystemButtonFace')

    def cambiar_color(self,boton,num):
        col_original=boton.cget("bg")
        boton.configure(bg=self.__colores[num])
        boton.after(300, partial(boton.configure, bg=col_original))

    def llamar_gameover(self):
        for boton in self.__botones:            
            boton.unbind("<Button-1>")          
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
        user=self.__entry_nombre.get().strip()      
        if user:
            self.__Nombre_de_usuario=self.__entry_nombre.get().lstrip().rstrip()
            self.__Ventana_Nombre_de_usuario.destroy()
            self.__texto_reemplazable.set(self.__Nombre_de_usuario)
            for boton in self.__botones:
                boton.bind("<Button-1>", self.detectar_clic)
            self.ejecutar()

    def guardar_json(self):
        with open('psymonpuntajes.json', 'r+',encoding='utf-8') as archivo:
            if not archivo.read(1):                
                self.__datos = []                  
            else:               
                archivo.seek(0)                   
                self.__datos=json.load(archivo)   
            self.__datos.append(self.to_dict())   
            archivo.seek(0)                       
            json.dump(self.__datos, archivo, indent=4)  

    def mostrar_puntajes(self):
        if self.__pantalla_puntajes.winfo_viewable():                                                   
            self.__pantalla_puntajes.place_forget()   
        else:                                                                                           
            self.__pantalla_puntajes.place(relx=0.5, rely=0.5, anchor='center',width=470, height=400) 
            lista=[]
            gj=gestor_jugadores()
            gj.ordenar_puntaje()    
            lista = gj.getlista()   
            self.__lista_jugadores.tag_configure('fuente', font=('Courier', 11))
            self.__lista_jugadores.delete('1.0', tk.END)          
            for jugador in lista:
                self.__lista_jugadores.insert(tk.END, str(jugador) + "\n", 'fuente')

    def to_dict(self):
        fechayhora=datetime.now()
        fecha = fechayhora.strftime("%d/%m/%Y")
        hora = fechayhora.strftime("%H:%M")
        return{
            'Jugador': self.__Nombre_de_usuario,
            'Fecha': fecha,
            'Hora': hora,
            'Puntaje': self.__contador_puntos.get()
        }

    def limite_caracteres(self,cadena):
        if len(cadena)<=10:
            band=True
        else:
            band=False
        return band
    
    def mostrar_menu(self):
        if self.__frame_puntaje.winfo_viewable():           
            self.__frame_puntaje.place_forget()             
        else:                                              
            self.__frame_puntaje.place(y=26, anchor='nw')   

    def ejecutar(self):
        self.after(1500, self.comienzo)
        self.mainloop()

if __name__=='__main__':
    app=aplicacion()
    app.mainloop()
