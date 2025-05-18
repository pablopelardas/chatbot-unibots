from helpers.pregunta_service import (
    buscar_respuesta, 
    es_pregunta_valida, 
    es_respuesta_valida, 
    ya_existe_pregunta, 
    agregar_pregunta_respuesta
)

def mostrar_coincidencias(coincidencias):
    """
    Muestra las coincidencias encontradas en la base de datos.

    Args:
        coincidencias (list): Lista de coincidencias encontradas.

    Returns:
        None
    """
    print('No encontré una respuesta exacta, pero estas preguntas podrían ayudarte:')
    
    for i in range(len(coincidencias)):
        print(f'  {i + 1}. {coincidencias[i]}')

    print('\nElegí una opción:')
    print('  [número] para ver la respuesta de una coincidencia')
    print('  [n] para crear una nueva pregunta y respuesta')
    print('  [Enter] para no hacer nada')

def pedir_pregunta_valida(preguntas):
    """
    Pide al usuario una pregunta válida.
    Args:
        preguntas (list): Lista de preguntas existentes.
    Returns:
        str: Pregunta válida ingresada por el usuario.
    """
    preguntaValida = False
    pregunta = ''

    while not preguntaValida:
        pregunta = input('Ingresá la nueva pregunta: ').strip()
        if es_pregunta_valida(pregunta):
            preguntaValida = True
        else:
            print('⚠️ La pregunta debe comenzar con "¿", terminar con "?" y tener más de 10 caracteres.')

        if ya_existe_pregunta(preguntas, pregunta):
            print('⚠️ Esa pregunta ya existe en la base de datos.')
            preguntaValida = False

    return pregunta

def pedir_respuesta_valida():
    """
    Pide al usuario una respuesta válida.
    Returns:
        str: Respuesta válida ingresada por el usuario.
    """
    respuesta = ''
    respuestaValida = False
    while not respuestaValida:
        respuesta = input('Ingresá la respuesta para esa pregunta: ').strip()
        if not es_respuesta_valida(respuesta):
            print('⚠️ La respuesta no puede estar vacía.')
        else:
            respuestaValida = True
    return respuesta
    
def agregar_nueva_pregunta(preguntas):
    """
    Agrega una nueva pregunta y respuesta a la lista de preguntas.
    Args:
        preguntas (list): Lista de preguntas y respuestas.
    """
    pregunta = pedir_pregunta_valida(preguntas)
    respuesta = pedir_respuesta_valida()
    agregar_pregunta_respuesta(preguntas, pregunta, respuesta)
    print('✅ Pregunta agregada correctamente.')

def handler_coincidencias(preguntas, coincidencias):
    """
    Maneja las coincidencias encontradas en la base de datos.
    Args:
        preguntas (list): Lista de preguntas existentes.
        coincidencias (list): Lista de coincidencias encontradas.
    """
    mostrar_coincidencias(coincidencias)
    seleccion = input('Tu elección: ').strip()

    try:
        indice = int(seleccion)
        if 1 <= indice <= len(coincidencias):
            pregunta_seleccionada = coincidencias[indice - 1]
            respuesta = buscar_respuesta(preguntas, pregunta_seleccionada)
            print(f'Respuesta: {respuesta}')
        else:
            print('⚠️ Número inválido.')
    except ValueError:
        if seleccion.lower() == 'n':
            agregar_nueva_pregunta(preguntas)
        else:
            print('No se seleccionó ninguna acción.')
            
def handler_sin_coincidencias(preguntas):
    """
    Maneja el caso en que no se encuentran coincidencias.
    Args:
        preguntas (list): Lista de preguntas existentes.
    """
    crear = input('No encontré ninguna coincidencia. ¿Querés agregar una nueva pregunta y respuesta? (s/n): ')
    if crear.lower() == 's':
        agregar_nueva_pregunta(preguntas)
