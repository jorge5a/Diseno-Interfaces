from openpyxl import load_workbook

class IncluyeAlumno:           
    def __init__(self, nombre , edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
 
        # 1. Abrir el archivo Excel existente
        self.archivo = "datos_ejemplo.xlsx"
        self.wb = load_workbook(self.archivo)

        # 2. Seleccionar la hoja (por nombre o la activa)
        self.hoja = self.wb["Datos"]  # Si sabes el nombre

        # 3. Nuevas filas a insertar
        self.fila= [self.nombre, self.edad, self.ciudad]

        # 4. Añadirlas al final del Excel
        self.hoja.append(self.fila)

        # 5. Guardar cambios
        self.wb.save(self.archivo)

        print("Nuevas filas añadidas a", self.archivo)
