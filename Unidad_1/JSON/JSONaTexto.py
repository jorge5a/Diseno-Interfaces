from PySide6.QtCore import QJsonDocument

# --- 1 Crear un "objeto JSON" en Python ---
persona = {
    "nombre": "Jorge",
    "edad": 25,
    "aficiones": ["programar", "música", "senderismo"],
    "activo": True
}

# --- 2 Convertir a QJsonDocument ---
doc = QJsonDocument.fromVariant(persona)  # fromVariant acepta dict/list

# --- 3 Convertir a texto JSON ---
texto_json = doc.toJson().data().decode("utf-8")
print("JSON generado:")
print(texto_json)


