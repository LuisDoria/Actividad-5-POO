import tkinter as tk
from tkinter import messagebox

class Programador:

    def __init__(self, nombre: str, apellidos: str):

        self.nombre = nombre
        self.apellidos = apellidos

    def __repr__(self) -> str:
        return f"Programador(nombre='{self.nombre}', apellidos='{self.apellidos}')"

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"


def validar_campo(campo: str):

    if any(char.isdigit() for char in campo):
        raise ValueError("El campo no puede contener dígitos.")

    if len(campo) > 20:
        raise ValueError("La longitud del campo no debe ser superior a 20 caracteres.")


class EquipoMaratonProgramacion:

    MAX_INTEGRANTES = 3

    def __init__(self, nombre_equipo: str, universidad: str, lenguaje: str):

        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []
    def esta_lleno(self) -> bool:
        return len(self.programadores) >= self.MAX_INTEGRANTES

    def anadir_programador(self, programador: Programador):

        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar al programador.")

        self.programadores.append(programador)
        print(f"'{programador.nombre}' ha sido añadido al equipo '{self.nombre_equipo}'.")

    def __str__(self) -> str:
        info_equipo = (
            f"--- Información del Equipo ---\n"
            f"Nombre: {self.nombre_equipo}\n"
            f"Universidad: {self.universidad}\n"
            f"Lenguaje: {self.lenguaje}\n"
            f"Integrantes ({len(self.programadores)}/{self.MAX_INTEGRANTES}):"
        )

        if not self.programadores:
            info_integrantes = "\n- (Aún no hay integrantes)"
        else:
            info_integrantes = "\n" + "\n".join(
                f"- {i+1}. {programador}" for i, programador in enumerate(self.programadores)
            )

        return info_equipo + info_integrantes


def main():

    try:
        print("--- Creación de Equipo de Maratón de Programación ---")

        nombre_equipo = input("Nombre del equipo: ")
        universidad = input("Universidad: ")
        lenguaje = input("Lenguaje de programación: ")

        equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)

        print("\n--- Ingrese los datos de los integrantes ---")
        for i in range(EquipoMaratonProgramacion.MAX_INTEGRANTES):
            print(f"\nDatos del integrante #{i+1}:")

            nombre_prog = input("Nombre del integrante: ")
            validar_campo(nombre_prog)

            apellidos_prog = input("Apellidos del integrante: ")
            validar_campo(apellidos_prog)

            programador = Programador(nombre_prog, apellidos_prog)
            equipo.anadir_programador(programador)

        print("\n--- ¡Equipo creado exitosamente! ---")
        print(equipo)

    except (ValueError, Exception) as e:
        print(f"\nError: {e}")
    except KeyboardInterrupt:
        print("\n\nProceso cancelado por el usuario.")

class EquipoMaratonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Maratón de Programación")
        self.integrantes = []

        # Campos de equipo
        tk.Label(root, text="Nombre del equipo:").grid(row=0, column=0, sticky="e")
        self.nombre_equipo = tk.Entry(root)
        self.nombre_equipo.grid(row=0, column=1)

        tk.Label(root, text="Universidad:").grid(row=1, column=0, sticky="e")
        self.universidad = tk.Entry(root)
        self.universidad.grid(row=1, column=1)

        tk.Label(root, text="Lenguaje de programación:").grid(row=2, column=0, sticky="e")
        self.lenguaje = tk.Entry(root)
        self.lenguaje.grid(row=2, column=1)

        # Campos de integrantes
        self.integrante_frame = tk.LabelFrame(root, text="Integrante #1")
        self.integrante_frame.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(self.integrante_frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.nombre_integrante = tk.Entry(self.integrante_frame)
        self.nombre_integrante.grid(row=0, column=1)

        tk.Label(self.integrante_frame, text="Apellidos:").grid(row=1, column=0, sticky="e")
        self.apellidos_integrante = tk.Entry(self.integrante_frame)
        self.apellidos_integrante.grid(row=1, column=1)

        self.btn_agregar = tk.Button(root, text="Agregar integrante", command=self.agregar_integrante)
        self.btn_agregar.grid(row=4, column=0, columnspan=2, pady=5)

        self.btn_registrar = tk.Button(root, text="Registrar equipo", command=self.registrar_equipo, state="disabled")
        self.btn_registrar.grid(row=5, column=0, columnspan=2, pady=10)

    def agregar_integrante(self):
        nombre = self.nombre_integrante.get()
        apellidos = self.apellidos_integrante.get()
        if not nombre or not apellidos:
            messagebox.showerror("Error", "Debe ingresar nombre y apellidos del integrante.")
            return
        self.integrantes.append((nombre, apellidos))
        if len(self.integrantes) < 3:
            self.integrante_frame.config(text=f"Integrante #{len(self.integrantes)+1}")
            self.nombre_integrante.delete(0, tk.END)
            self.apellidos_integrante.delete(0, tk.END)
        else:
            self.btn_agregar.config(state="disabled")
            self.btn_registrar.config(state="normal")
            self.integrante_frame.config(text="Integrantes completos")

    def registrar_equipo(self):
        nombre_equipo = self.nombre_equipo.get()
        universidad = self.universidad.get()
        lenguaje = self.lenguaje.get()
        if not nombre_equipo or not universidad or not lenguaje:
            messagebox.showerror("Error", "Debe completar todos los campos del equipo.")
            return
        info = f"Equipo: {nombre_equipo}\nUniversidad: {universidad}\nLenguaje: {lenguaje}\nIntegrantes:\n"
        for i, (n, a) in enumerate(self.integrantes, 1):
            info += f"{i}. {n} {a}\n"
        messagebox.showinfo("Equipo registrado", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = EquipoMaratonGUI(root)
    root.mainloop()
