from helpers.file_manager import guardar_preguntas

def buscar_respuesta(preguntas, pregunta):
    """
    Busca la respuesta a una pregunta en la lista de preguntas.
    Args:
        preguntas (list): Lista de preguntas y respuestas.
        pregunta (str): Pregunta a buscar.
    Returns:
        str: Respuesta correspondiente a la pregunta, o None si no se encuentra.
    """
    for p in preguntas:
        if p['pregunta'].lower() == pregunta.lower():
            return p['respuesta']
    return None

def buscar_coincidencias(preguntas, texto):
    # HOla
    """
    Busca coincidencias en la lista de preguntas que contengan el texto dado.
    Args:
        preguntas (list): Lista de preguntas y respuestas.
        texto (str): Texto a buscar en las preguntas.
    Returns:
        list: Lista de preguntas que contienen el texto dado.
    """
    coincidencias = []
    for p in preguntas:
        if texto.lower() in p['pregunta'].lower():
            coincidencias.append(p['pregunta'])
    return coincidencias

def es_pregunta_valida(pregunta: str) -> bool:
    """
    Verifica si la pregunta es válida.
    Args:
        pregunta (str): Pregunta a verificar.
    Returns:
        bool: True si la pregunta es válida, False en caso contrario.
    """
    def startsWithQuestionMark(pregunta):
        return pregunta[0] == '¿'
    def endsWithQuestionMark(pregunta):
        return pregunta[-1] == '?'
    
    return (
        startsWithQuestionMark(pregunta) and 
        endsWithQuestionMark(pregunta) and 
        len(pregunta) > 10
    )

def es_respuesta_valida(respuesta: str) -> bool:
    """
    Verifica si la respuesta es válida.
    Args:
        respuesta (str): Respuesta a verificar.
    Returns:
        bool: True si la respuesta es válida, False en caso contrario.
    """
    return bool(respuesta.strip())

def ya_existe_pregunta(preguntas, nueva_pregunta) -> bool:
    """
    Verifica si la pregunta ya existe en la lista de preguntas.
    Args:
        preguntas (list): Lista de preguntas existentes.
        nueva_pregunta (str): Pregunta a verificar.
    Returns:
        bool: True si la pregunta ya existe, False en caso contrario.
    """
    for p in preguntas:
        if p['pregunta'].strip().lower() == nueva_pregunta.strip().lower():
            return True
    return False

def agregar_pregunta_respuesta(preguntas, pregunta, respuesta):
    """
    Agrega una nueva pregunta y respuesta a la lista de preguntas.
    Args:
        preguntas (list): Lista de preguntas existentes.
        pregunta (str): Nueva pregunta a agregar.
        respuesta (str): Respuesta correspondiente a la nueva pregunta.
    Returns:
        None
    """
    preguntas.append({'pregunta': pregunta.strip(), 'respuesta': respuesta.strip()})
    guardar_preguntas(preguntas)