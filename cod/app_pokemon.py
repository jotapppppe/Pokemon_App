# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:28:31 2024

@author: Personal
"""

import tkinter as tk
import pandas as pd
from tkinter import ttk
import tkinter.font as tkf
from PIL import Image, ImageTk
import pygame
from Funciones import *
from entrenadores import *

# INTERFAZ 

############################################################
# Sonido de fondo

# Inicializar pygame
pygame.mixer.init()

# Rutas de los archivos de música para cada generación 
music_paths = {
    "Primera Generación": r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\music\Palette_Town - FRLG.mp3",
    "Segunda Generación": r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\music\National_Park - HGSS.mp3",
    "Tercera Generación": r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\music\Route_120 - RSE.mp3",
    "Cuarta Generación": r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\music\Route_209 - DPP.mp3",
    "Quinta Generación": r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\music\N-s Farewell - BW.mp3"
}
def reproducir_musica(generacion):
    # Detener la música actual si se está reproduciendo
    pygame.mixer.music.stop()
    
    # Obtener la ruta del archivo de música según la generación seleccionada
    music_path = music_paths.get(generacion)
    
    # Cargar y reproducir la nueva música si hay una ruta válida
    if music_path:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # -1 para reproducir en bucle, 0 para reproducir una vez

##################################

# Crear la ventana principal
root = tk.Tk()
root.title("Analisis de Pokemon por generaciones")
root.geometry("800x566")

# Crear un marco para contener los widgets
main_frame = tk.Frame(root)
main_frame.pack(expand=1, fill="both")

icono = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\imag\pokeicon.png")
root.iconphoto(True, icono)


# Función para cambiar la imagen de fondo según la selección de la generación
def update_background(event=None):
    global gym
    selection = generation_var.get()
    for widget in additional_widgets:
        widget.destroy()
    additional_widgets.clear()

    if selection == "Primera Generación":
        background_label.config(image=background_image1)
        region_label.config(text="Kanto Region")
    elif selection == "Segunda Generación":
        background_label.config(image=background_image2)
        region_label.config(text="Johto Region")
    elif selection == "Tercera Generación":
        background_label.config(image=background_image3)
        region_label.config(text="Hoenn Region")
    elif selection == "Cuarta Generación":
        background_label.config(image=background_image4)
        region_label.config(text="Sinnoh Region")
    elif selection == "Quinta Generación":
        
        gym = unova
        region_label.config(text="Unova Region")
        # Crear radiobuttons adicionales
        # Crear radiobuttons adicionales
        background_label.config(image=background_image5_1)
        radio_button_var = tk.StringVar(value="1")  # Inicializar con la opción "1"
        
        radio_button1 = ttk.Radiobutton(main_frame, text="Blanco / Negro", variable=radio_button_var, value="1")
        radio_button1.pack(anchor=tk.NW, padx=10, pady=10)
        additional_widgets.append(radio_button1)
        
        radio_button2 = ttk.Radiobutton(main_frame, text="Blanco 2 / Negro 2", variable=radio_button_var, value="2")
        radio_button2.pack(anchor=tk.NW, padx=10, pady=10)
        additional_widgets.append(radio_button2)
        
        # Configurar función para manejar la selección de los radiobuttons
        radio_button1.config(command=lambda: handle_radio_selection(radio_button_var.get()))
        radio_button2.config(command=lambda: handle_radio_selection(radio_button_var.get()))
        
    reset_buttons()

    reproducir_musica(selection)
# Función para resetear los botones
def reset_buttons():
    best_starter_button.config(text="Mejor Inicial")
    top_10_button.config(text="Top 20")
    best_team_button.config(text="Mejor Equipo")

# Función de quinta generación


def handle_radio_selection(value):
    global gym
    if value == "1":
        background_label.config(image=background_image5_1)
        gym = unova
        # Aquí puedes agregar más acciones según la opción seleccionada
    elif value == "2":
        background_label.config(image=background_image5_2)
        gym = unova_bw2
        # Aquí puedes agregar más acciones según la opción seleccionada
    else:
        print("Ninguna opción seleccionada")

# Cargar las imágenes de fondo
background_image1 = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\mapas_pkmn\kanto_map.png")
background_image2 = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\mapas_pkmn\johto_map.png")
background_image3 = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\mapas_pkmn\hoenn_map.png")
background_image4 = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\mapas_pkmn\sinnoh_map.png")
background_image5_1 = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\mapas_pkmn\unova_map.png")
background_image5_2 = tk.PhotoImage(file=r"C:\Users\Personal\OneDrive\Documentos\CA0305\Pokemon_App\docs\mapas_pkmn\unova_map_2.png")


# Crear un label para la imagen de fondo
background_label = tk.Label(main_frame)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un label para el nombre de la región
region_label = ttk.Label(main_frame, text="", font=("Helvetica", 12))
region_label.pack(pady=10)

# Crear una variable para la selección de la generación
generation_var = tk.StringVar(value="Primera Generación")

# Crear una lista desplegable (combobox) para seleccionar la generación
generation_combobox = ttk.Combobox(main_frame, textvariable=generation_var, values=["Primera Generación", "Segunda Generación", "Tercera Generación",
                                                                                    "Cuarta Generación", "Quinta Generación"])
generation_combobox.pack(anchor=tk.NW, padx=10, pady=10)
generation_combobox.bind("<<ComboboxSelected>>", update_background)

def mejor_equipo(generacion):
    global gym
    starters = ''
    # Obtener los diccionarios (starters y gym) según la generación
    if generacion == "Primera Generación":
        mejor_starter = {'Número de Pokédex': 'Venusaur', 'Puntaje': 16.25, 'Stats': 525, 'Tipo_1': 'Grass', 'Tipo_2': 'Poison'}
        gym = kanto
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 1]
    elif generacion == "Segunda Generación":
        mejor_starter = {'Número de Pokédex': 'Typhlosion', 'Puntaje': -30.25, 'Stats': 534, 'Tipo_1': 'Fire', 'Tipo_2': ' '}
        gym = johto
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 2]
    elif generacion == "Tercera Generación":
        mejor_starter = {'Número de Pokédex': 'Swampert', 'Puntaje': 34.0, 'Stats': 535, 'Tipo_1': 'Water', 'Tipo_2': 'Ground'}
        gym = hoenn
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 3]
    elif generacion == "Cuarta Generación":
        mejor_starter = {'Número de Pokédex': 'Empoleon', 'Puntaje': 20.5, 'Stats': 530, 'Tipo_1': 'Water', 'Tipo_2': 'Steel'}
        gym = sinnoh
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 4]
    elif generacion == "Quinta Generación":
        mejor_starter = {'Número de Pokédex': 'Emboar', 'Puntaje': 36.5, 'Stats': 528, 'Tipo_1': 'Fire', 'Tipo_2':'Fighting'}
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 5]
    
    # Crear el DataFrame con los mejores 5 del Top Regional que no repitan Tipo_1
    top_5_no_repetir = []
    count = 0
    tipos_utilizados = set()

    for index, row in Top_regional(gym, pkdx, pokedex_completa).iterrows():
        if row['Tipo_1'] != mejor_starter['Tipo_1'] and row['Tipo_1'] not in tipos_utilizados and row['Tipo_2'] not in tipos_utilizados  and count < 5:
            top_5_no_repetir.append(row)
            tipos_utilizados.add(row['Tipo_1'])
            tipos_utilizados.add(row['Tipo_2'])
            count += 1

    # Crear la tabla resultante con el mejor starter y los 5 siguientes
    resultado_equipo = pd.DataFrame(top_5_no_repetir)
    resultado_equipo = resultado_equipo.head(5)
    resultado_equipo = pd.concat([pd.DataFrame([mejor_starter]), resultado_equipo])

    # Crear una nueva ventana para mostrar el resultado del equipo
    equipo_window = tk.Toplevel(root)
    equipo_window.title("Mejor Equipo")
    equipo_window.geometry("600x400")

    # Crear un Treeview (tabla) para mostrar los resultados del equipo
    tabla_equipo = ttk.Treeview(equipo_window, columns=('Número de Pokédex', 'Puntaje', 'Stats', 'Tipo_1', 'Tipo_2'), show='headings')
    tabla_equipo.heading('Número de Pokédex', text='Pokemon')
    tabla_equipo.heading('Puntaje', text='Puntaje')
    tabla_equipo.heading('Stats', text='Stats')
    tabla_equipo.heading('Tipo_1', text='Tipo 1')
    tabla_equipo.heading('Tipo_2', text='Tipo 2')

    # Insertar los datos en la tabla
    for index, row in resultado_equipo.iterrows():
        tabla_equipo.insert("", "end", values=(row['Número de Pokédex'], row['Puntaje'], row['Stats'], row['Tipo_1'], row['Tipo_2']))

    for col in ('Número de Pokédex', 'Puntaje', 'Stats', 'Tipo_1', 'Tipo_2'):
        tabla_equipo.column(col, width=tkf.Font().measure(col))  # Ajustar el ancho inicial según el encabezado
        # Ajustar el ancho basado en el contenido más largo en la columna
        max_width = max([tkf.Font().measure(str(row[col])) for _, row in resultado_equipo.head(10).iterrows()])
        tabla_equipo.column(col, width=max_width + 20)  # Agregar un pequeño margen adicional
        tabla_equipo.column(col, anchor='center')  # Alinear el texto en el centro de la columna
    
    tabla_equipo.pack(padx=10, pady=10, fill='both', expand=True)

    # Resto de tu código de interfaz...

# Ejemplo de uso en un botón de tkinter
def on_mejor_equipo_click():
    generacion_elegida = generation_var.get()  # Obtener la generación seleccionada
    mejor_equipo(generacion_elegida)

#######################################

# Crear los botones
# Crear un frame para los botones y colocarlo en el marco principal
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=20)

# Crear los botones y empaquetarlos en el frame de botones
best_starter_button = ttk.Button(button_frame, text="Mejor Inicial")
best_starter_button.pack(side=tk.LEFT, padx=10)

top_10_button = ttk.Button(button_frame, text="Top 15")
top_10_button.pack(side=tk.LEFT, padx=10)

best_team_button = ttk.Button(button_frame, text="Mejor Equipo", command=on_mejor_equipo_click)
best_team_button.pack(side=tk.LEFT, padx=10)

# Lista para almacenar widgets adicionales
additional_widgets = []

# Inicializar con la opción A seleccionada
radio_button_var1 = tk.IntVar(value=1)  # Inicializar con el valor 1 (Opción A)
radio_button1 = ttk.Radiobutton(main_frame, text="Opción A", variable=radio_button_var1, value=1)
radio_button1.pack(anchor=tk.NW, padx=10, pady=10)
additional_widgets.append(radio_button1)

radio_button_var2 = tk.IntVar()
radio_button2 = ttk.Radiobutton(main_frame, text="Opción B", variable=radio_button_var2, value=2)
radio_button2.pack(anchor=tk.NW, padx=10, pady=10)
additional_widgets.append(radio_button2)

# Configurar función para manejar la selección de los radiobuttons
radio_button1.config(command=lambda: handle_radio_selection(radio_button_var1.get()))
radio_button2.config(command=lambda: handle_radio_selection(radio_button_var2.get()))

def mostrar_mejor_starter():
    global gym
    # Definir los starters y gym según la generación seleccionada
    generacion = generation_var.get()
    
    if generacion == "Primera Generación":
        starters = starter_kanto  # Ejemplo de lista de starters para la Primera Generación
        gym = kanto
    elif generacion == "Segunda Generación":
        starters = starter_johto  # Ejemplo de lista de starters para la Segunda Generación
        gym = johto # Ejemplo de diccionario de gimnasios para la Segunda Generación
    
    elif generacion == "Tercera Generación":
        starters = starter_hoenn  # Ejemplo de lista de starters para la Tercera Generación
        gym = hoenn # Ejemplo de diccionario de gimnasios para la Tercera Generación
    elif generacion == "Cuarta Generación":
        starters = starter_sinnoh  # Ejemplo de lista de starters para la Cuarta Generación
        gym = sinnoh
    elif generacion == "Quinta Generación":
        starters = starter_unova

    
    # Calcular el resultado utilizando la función starter
    resultado = starter(starters, gym, pokedex_completa)

    # Obtener el nombre del mejor starter
    mejor_starter = pokedex_completa.iloc[starters[resultado[resultado['Puntaje'] == resultado['Puntaje'].max()].index[0]]]['Name']
    # Crear una nueva ventana para mostrar la tabla
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Mejor Starter")
    resultado_window.geometry("450x300")

    mejor_starter_label = tk.Label(resultado_window, text=f"El mejor inicial es: {mejor_starter}")
    mejor_starter_label.pack(pady=10)

    
    gif_path = f"C:\\Users\\Personal\\OneDrive\\Documentos\\CA0305\\Pokemon_App\\docs\\imag\\{mejor_starter.lower()}.gif"
    # Cargar el GIF usando PIL
    img = Image.open(gif_path)
    frames = []
    target_width = 150 
    
    try:
        while True:
            # Obtener las dimensiones originales del frame actual
            original_width, original_height = img.size
            
            # Calcular el nuevo alto proporcional al ancho objetivo
            target_height = int(original_height * (target_width / original_width))
            
            # Redimensionar el frame actual al tamaño objetivo
            frame = img.copy().resize((target_width, target_height), Image.LANCZOS)
            
            # Convertir el frame redimensionado a formato ImageTk
            frame_image = ImageTk.PhotoImage(frame)
            frames.append(frame_image)
            
            # Buscar el siguiente frame del GIF
            img.seek(len(frames))
    except EOFError:
        pass

    # Crear una etiqueta para mostrar el GIF
    gif_label = tk.Label(resultado_window)
    gif_label.pack(pady=10)

    # Función para animar el GIF
    def animate(index):
        frame = frames[index]
        gif_label.configure(image=frame)
        resultado_window.after(100, animate, (index + 1) % len(frames))

    # Iniciar la animación del GIF
    animate(0)


    # Crear un Treeview (tabla) para mostrar los resultados
    tabla_resultado = ttk.Treeview(resultado_window, columns=('Tipo', 'Puntaje'), show='headings')
    tabla_resultado.heading('Tipo', text='Tipo')
    tabla_resultado.heading('Puntaje', text='Puntaje')

    # Insertar los datos en la tabla
    for index, row in resultado.iterrows():
        tabla_resultado.insert("", "end", values=(row['Tipo'], row['Puntaje']))

    for col in ('Tipo', 'Puntaje'):
        tabla_resultado.column(col, width=tkf.Font().measure(col))  # Ajustar el ancho inicial según el encabezado
        # Ajustar el ancho basado en el contenido más largo en la columna
        max_width = max([tkf.Font().measure(str(row[col])) for _, row in resultado.head(10).iterrows()])
        tabla_resultado.column(col, width=max_width + 20)  # Agregar un pequeño margen adicional
        tabla_resultado.column(col, anchor='center')  # Alinear el texto en el centro de la columna
    # Ajustar el tamaño de las columnas
    tabla_resultado.pack(padx=10, pady=10, fill='both', expand=True)

    resultado_window.update_idletasks()  # Asegura que todas las tareas pendientes se completen
    resultado_window.geometry("420x350")



# Función para mostrar la tabla con el Top 10 según la generación seleccionada
def mostrar_top10():
    # Definir gym según la generación seleccionada
    global gym
    generacion = generation_var.get()
    
    if generacion == "Primera Generación":
        gym = kanto # Ejemplo de diccionario de gimnasios para la Primera Generación
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 1]
    elif generacion == "Segunda Generación":
        gym = johto  # Ejemplo de diccionario de gimnasios para la Segunda Generación
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 2]
    elif generacion == "Tercera Generación":
        gym = hoenn  # Ejemplo de diccionario de gimnasios para la Tercera Generación
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 3]
    elif generacion == "Cuarta Generación":
        gym = sinnoh
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 4]
    elif generacion == "Quinta Generación":
        pkdx = pokedex_completa.loc[pokedex_completa['Generation'] == 5]
    # Calcular el resultado utilizando la función Top_regional
    resultado = Top_regional(gym, pkdx, pokedex_completa)

    # Crear una nueva ventana para mostrar la tabla
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Top 10 Pokémon")
    resultado_window.geometry("680x400")

    # Crear un Treeview (tabla) para mostrar los resultados
    tabla_resultado = ttk.Treeview(resultado_window, columns=('Número de Pokédex', 'Puntaje', 'Stats', 'Tipo_1', 'Tipo_2'), show='headings')
    tabla_resultado.heading('Número de Pokédex', text='Pokemon')
    tabla_resultado.heading('Puntaje', text='Puntaje')
    tabla_resultado.heading('Stats', text='Stats')
    tabla_resultado.heading('Tipo_1', text='Tipo 1')
    tabla_resultado.heading('Tipo_2', text='Tipo 2')

    # Insertar los datos en la tabla
    for index, row in resultado.head(20).iterrows():
        tabla_resultado.insert("", "end", values=(row['Número de Pokédex'], row['Puntaje'], row['Stats'], row['Tipo_1'], row['Tipo_2']))


    for col in ('Número de Pokédex', 'Puntaje', 'Stats', 'Tipo_1', 'Tipo_2'):
        tabla_resultado.column(col, width=tkf.Font().measure(col))  # Ajustar el ancho inicial según el encabezado
        # Ajustar el ancho basado en el contenido más largo en la columna
        max_width = max([tkf.Font().measure(str(row[col])) for _, row in resultado.head(10).iterrows()])
        tabla_resultado.column(col, width=max_width + 20)  # Agregar un pequeño margen adicional
        tabla_resultado.column(col, anchor='center')  # Alinear el texto en el centro de la columna

    tabla_resultado.pack(padx=10, pady=10, fill='both', expand=True)




# Configurar el botón Mejor Starter
best_starter_button.config(command=mostrar_mejor_starter)

# Configurar el botón Top 10
top_10_button.config(command=mostrar_top10)


# Ejecutar la función para establecer la imagen inicial
update_background()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
