from PySide6.QtCore import QJsonDocument


# --- 1 Leer JSON desde texto ---
texto = """
{
    "curso": "Seguridad informática",
    "horas": 120,
    "modulos": ["Bastionado", "Auditoría", "Criptografía"]
}
"""

doc2 = QJsonDocument.fromJson(texto.encode("utf-8"))
objeto = doc2.toVariant()  # Convierte a dict/list de Python

print("\nCurso leído desde el JSON:")
print("Nombre:", objeto["curso"])
print("Horas:", objeto["horas"])
print("Primer módulo:", objeto["modulos"][0])
