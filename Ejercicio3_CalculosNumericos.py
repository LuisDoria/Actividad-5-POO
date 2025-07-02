import tkinter as tk
from tkinter import messagebox
import math

def calcular_logaritmo_neperiano(valor: float) -> None:

    try:
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo.")

        resultado = math.log(valor)
        print(f"Resultado del logaritmo = {resultado}")

    except ValueError as e:
        print(f"Error al calcular el logaritmo: {e}")

def calcular_raiz_cuadrada(valor: float) -> None:

    try:
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo.")

        resultado = math.sqrt(valor)
        print(f"Resultado de la raíz cuadrada = {resultado}")

    except ValueError as e:
        print(f"Error al calcular la raíz cuadrada: {e}")

def main():

    try:
        entrada_usuario = input("Ingrese un valor numérico: ")
        valor = float(entrada_usuario)

        calcular_logaritmo_neperiano(valor)
        calcular_raiz_cuadrada(valor)

    except ValueError:
        print("Error: El valor ingresado debe ser numérico.")

def calcular_logaritmo():
    entrada = entry_valor.get()
    try:
        valor = float(entrada)
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo.")
        resultado = math.log(valor)
        label_resultado.config(text=f"Logaritmo neperiano: {resultado:.5f}")
    except ValueError as e:
        label_resultado.config(text="")
        messagebox.showerror("Error", f"Manejo de errores: {e}")

def calcular_raiz():
    entrada = entry_valor.get()
    try:
        valor = float(entrada)
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo.")
        resultado = math.sqrt(valor)
        label_resultado.config(text=f"Raíz cuadrada: {resultado:.5f}")
    except ValueError as e:
        label_resultado.config(text="")
        messagebox.showerror("Error", f"Manejo de errores: {e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cálculos Numéricos")

# Etiqueta y campo de entrada
tk.Label(ventana, text="Ingrese un valor numérico:").grid(row=0, column=0, padx=10, pady=10)
entry_valor = tk.Entry(ventana)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

# Botones de cálculo
btn_log = tk.Button(ventana, text="Calcular logaritmo neperiano", command=calcular_logaritmo)
btn_log.grid(row=1, column=0, padx=10, pady=5)

btn_raiz = tk.Button(ventana, text="Calcular raíz cuadrada", command=calcular_raiz)
btn_raiz.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta de resultado
label_resultado = tk.Label(ventana, text="", fg="blue")
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
