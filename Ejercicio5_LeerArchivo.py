class LeerArchivo:
    @staticmethod
    def main():
        nombre_archivo = "C:/Users/EDNA/Documents/Universidad Nacional de Colombia/INGENIERÍA DE SISTEMAS/SEMESTRE 4/POO/ACTIVIDAD 5/Actividad-5-POO/prueba.txt"

        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    print(linea.strip())
        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al leer el archivo: {e}")
            print("No se pudo leer el archivo.")

if __name__ == "__main__":
    LeerArchivo.main()
    