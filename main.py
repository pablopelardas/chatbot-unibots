import argparse
import os
from helpers.file_manager import obtener_preguntas, set_file_path
from helpers.pregunta_service import buscar_respuesta, buscar_coincidencias
from helpers.interact import handler_coincidencias, handler_sin_coincidencias



def main():

    # Argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Asistente de preguntas y respuestas")
    parser.add_argument('--file', type=str, default='./data/preguntas.json',
                        help='Ruta al archivo JSON de preguntas (por defecto: ./data/preguntas.json)')
    args = parser.parse_args()

    # Establecer ruta absoluta al archivo
    abs_path = os.path.abspath(args.file)
    set_file_path(abs_path)

    preguntas = obtener_preguntas()
    pregunta = input('¿Cuál es tu pregunta? (Escribe "salir" para terminar): ')
    while pregunta.lower() != 'salir':
        respuesta = buscar_respuesta(preguntas, pregunta)
        
        if respuesta:
            print(f'Respuesta: {respuesta}')
        else:
            coincidencias = buscar_coincidencias(preguntas, pregunta)
            if coincidencias:
                handler_coincidencias(preguntas, coincidencias)
            else:
                handler_sin_coincidencias(preguntas)

        pregunta = input('\n¿Cuál es tu pregunta? (Escribe "salir" para terminar): ')

if __name__ == '__main__':
    main()
