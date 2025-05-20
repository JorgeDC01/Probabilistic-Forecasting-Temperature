import json
import os

# Ruta del notebook (ajusta si es necesario)
notebook_path = os.path.abspath("EDA_Preprocessing.ipynb")

# Verifica que el archivo exista
if not os.path.exists(notebook_path):
    print(f"❌ No se encontró el archivo: {notebook_path}")
    exit(1)

# Cargar el notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Eliminar 'widgets' de metadata si existe
if 'widgets' in nb.get('metadata', {}):
    print("🧹 Eliminando metadata.widgets...")
    del nb['metadata']['widgets']

# Guardar el notebook corregido
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("✅ Notebook corregido (metadata.widgets eliminado).")
