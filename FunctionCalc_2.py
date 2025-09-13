# CALCULADORA DE FUNCIONES EN PYTHON

import customtkinter as ctk
import matplotlib.pyplot as mtplt
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# VENTANA
app = ctk.CTk()
app.geometry("1200x600")

# ----------------------------------------------------------------
# FRAMES
# ----------------------------------------------------------------

# FUNCIONES


def Calculate_Function(entry):
    # CÁLCULO DEL RECORRIDO DE LA FUNCIÓN
    funcion = entry.get()
    x = sp.Symbol("x")
    f = sp.sympify(funcion)
    selectDominio = [-3, -1, 0, 3, 6]  # Selección personal del dominio
    selectRecorrido = []  # Almacenamiento del recorrido
    for entrada in selectDominio:
        imagen = f.subs(x, entrada)  # Cálculo de cada elemento del recorrido
        # (devuelve un objeto en lugar de un número)
        selectRecorrido.append(float(imagen))

    # GRAFICACIÓN
    # Limpieza del frame de la gráfica (reinicio)
    for widget in frGrafica.winfo_children():
        widget.destroy()

    # Crea la figura principal
    fig, ax = mtplt.subplots(figsize=(5, 4), dpi=100)
    # y se guardan los ejes en ax
    ax.plot(selectDominio, selectRecorrido, marker="o")  # Dibuja la línea
    ax.axhline(0, color="black", linewidth=0.8)  # Dibuja el eje X (Y=0)
    ax.axvline(0, color="black", linewidth=0.8)  # Dibuja el eye Y (X=0)
    # Dibuja la cuadrícula de la gráfica
    ax.grid(True, linestyle="--", alpha=0.5)

    # Inserción de la gráfica en la interfaz de CustomTkinter
    # Crea el widget conteniendo la gráfica
    canvas = FigureCanvasTkAgg(fig, master=frGrafica)
    canvas.draw()  # Renderiza la figura para que se vea en la interfaz
    # Agrega el widget al frGrafica
    canvas.get_tk_widget().pack(expand=True, fill="both")

    # Inserción de texto
    for x, y in zip(selectDominio, selectRecorrido):
        ax.text(x, y, f"({x}, {y})", fontsize=6, ha="left", va="bottom")


# FRAME TÍTULO
frTitulo = ctk.CTkFrame(master=app, width=600)
frTitulo.pack()
lblTitulo = ctk.CTkLabel(master=frTitulo, text="Calculadora de Funciones")
lblTitulo.pack()

# FRAME CALCULADORA
frCalculadora = ctk.CTkFrame(master=app, width=600)
frCalculadora.pack()
frInputs = ctk.CTkFrame(master=frCalculadora)
frInputs.pack()
entFuncion = ctk.CTkEntry(
    master=frInputs, placeholder_text="Ingrese la función...")
entFuncion.grid(row=0, column=0)
btnFuncion = ctk.CTkButton(
    master=frInputs, text="Ingresar", command=lambda: Calculate_Function(entFuncion))
btnFuncion.grid(row=0, column=1)

# FRAME GRÁFICA
frGrafica = ctk.CTkFrame(master=app)
frGrafica.pack()
"""
#entVarX = ctk.CTkEntry(
    master=frInputs, placeholder_text="Ingrese la variable x... ")
entVarX.grid(row=1, column=0)
btnVarX = ctk.CTkButton(master=frInputs, text="Ingresar")
btnVarX.grid(row=1, column=1)
"""


app.mainloop()
