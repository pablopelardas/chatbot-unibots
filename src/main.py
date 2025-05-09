
filePath = './data/preguntas.txt'

def obtener_preguntas():
    preguntas = []
    with open(filePath, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if '|' in linea:
                pregunta, respuesta = linea.split('|', 1)  # divide solo en el primer '|'
                preguntas.append({
                    'pregunta': pregunta.strip(),
                    'respuesta': respuesta.strip()
                })
    return preguntas

def escribir_pregunta(pregunta):
    with open(filePath, 'a', encoding='utf-8') as archivo:
        archivo.write(f'{pregunta} | Sin respuesta\n')
        
def buscar_respuesta(preguntas,pregunta):
    for p in preguntas:
        if p['pregunta'] == pregunta:
            return p['respuesta']
    escribir_pregunta(pregunta)
    preguntas.append({
        'pregunta': pregunta,
        'respuesta': 'Sin respuesta'
    })
    return 'Sin respuesta'

def main():
    preguntas = obtener_preguntas()
    pregunta = input('¿Cuál es tu pregunta? (Escribe "salir" para terminar): ')
    while pregunta.lower() != 'salir':
        respuesta = buscar_respuesta(preguntas,pregunta)
        print(f'Respuesta: {respuesta}')
        pregunta = input('¿Cuál es tu pregunta? (Escribe "salir" para terminar): ')


if __name__ == '__main__':
    main() 