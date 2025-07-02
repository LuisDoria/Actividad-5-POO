import tkinter as tk
from tkinter import scrolledtext, messagebox

class LeerArchivoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contenido del Archivo")
        master.geometry("500x400")

        self.nombre_archivo = "C:/Users/EDNA/Documents/Universidad Nacional de Colombia/INGENIERÍA DE SISTEMAS/SEMESTRE 4/POO/ACTIVIDAD 5/Actividad-5-POO/prueba.txt"

        self.label = tk.Label(master, text=f"Contenido de '{self.nombre_archivo.split('/')[-1]}':", font=("Arial", 12))
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15, font=("Courier New", 10))
        self.text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.read_button = tk.Button(master, text="Leer Archivo", command=self.leer_y_mostrar_archivo)
        self.read_button.pack(pady=10)

        self.leer_y_mostrar_archivo()

    def leer_y_mostrar_archivo(self):
        self.text_area.delete(1.0, tk.END)

        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                self.text_area.insert(tk.END, contenido)
        except FileNotFoundError:
            messagebox.showerror("Error de Archivo", f"Error: El archivo '{self.nombre_archivo}' no se encontró.")
            self.text_area.insert(tk.END, "ERROR: Archivo no encontrado. Por favor, verifica la ruta.")
        except Exception as e:
            messagebox.showerror("Error de Lectura", f"Ocurrió un error al leer el archivo: {e}")
            self.text_area.insert(tk.END, f"ERROR: No se pudo leer el archivo. Detalles: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LeerArchivoGUI(root)
    root.mainloop()
    
    
