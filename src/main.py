# Ruta del archivo donde se almacenan las preguntas y respuestas
filePath = './data/preguntas.txt'

# Función para obtener las preguntas y respuestas del archivo
def obtener_preguntas():
    preguntas = []  # Lista para almacenar las preguntas y respuestas
    with open(filePath, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Elimina espacios en blanco al inicio y al final de la línea
            if '|' in linea:
                # Divide la línea en pregunta y respuesta usando el primer '|'
                pregunta, respuesta = linea.split('|', 1)
                preguntas.append({
                    'pregunta': pregunta.strip(),  # Elimina espacios en blanco de la pregunta
                    'respuesta': respuesta.strip()  # Elimina espacios en blanco de la respuesta
                })
    return preguntas  # Devuelve la lista de preguntas y respuestas

# Función para escribir una nueva pregunta en el archivo
def escribir_pregunta(pregunta):
    with open(filePath, 'a', encoding='utf-8') as archivo:
        # Escribe la pregunta en el archivo con una respuesta predeterminada
        archivo.write(f'{pregunta} | Sin respuesta\n')

# Función para buscar la respuesta a una pregunta en la lista de preguntas
def buscar_respuesta(preguntas, pregunta):
    for p in preguntas:
        if p['pregunta'] == pregunta:
            return p['respuesta']  # Devuelve la respuesta si la pregunta existe
    # Si la pregunta no existe, se escribe en el archivo y se agrega a la lista
    escribir_pregunta(pregunta)
    preguntas.append({
        'pregunta': pregunta,
        'respuesta': 'Sin respuesta'
    })
    return 'Sin respuesta'  # Devuelve 'Sin respuesta' si la pregunta no existe

# Función principal del programa
def main():
    preguntas = obtener_preguntas()  # Obtiene las preguntas y respuestas del archivo
    pregunta = input('¿Cuál es tu pregunta? (Escribe "salir" para terminar): ')
    while pregunta.lower() != 'salir':
        respuesta = buscar_respuesta(preguntas, pregunta)  # Busca la respuesta a la pregunta
        print(f'Respuesta: {respuesta}')
        pregunta = input('¿Cuál es tu pregunta? (Escribe "salir" para terminar): ')

# Ejecuta la función principal si el script se ejecuta directamente
if __name__ == '__main__':
    main()
