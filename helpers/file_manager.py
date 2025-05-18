import json
import os

_file_path = None  # Variable interna

def set_file_path(path):
    """
    Establece la ruta del archivo de preguntas y se asegura que el directorio y archivo existan.
    
    Args:
        path (str): Ruta al archivo JSON.
    """
    global _file_path

    # Crear directorio si no existe
    dir_path = os.path.dirname(os.path.abspath(path))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
   
    # Crear archivo vacío si no existe
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as archivo:
            json.dump([], archivo, ensure_ascii=False, indent=2)

    _file_path = os.path.abspath(path)

def obtener_preguntas():
    """
    Obtiene preguntas desde el archivo JSON especificado.
    """
    if _file_path is None:
        raise ValueError("El file path no fue establecido. Llamá a set_file_path(path) primero.")
    try:
        with open(_file_path, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_preguntas(preguntas):
    """
    Guarda las preguntas en el archivo JSON especificado.
    """
    if _file_path is None:
        raise ValueError("El file path no fue establecido. Llamá a set_file_path(path) primero.")
    with open(_file_path, 'w', encoding='utf-8') as archivo:
        json.dump(preguntas, archivo, ensure_ascii=False, indent=2)