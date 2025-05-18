# 📚 Asistente de Preguntas y Respuestas

Este es un asistente interactivo que permite consultar una base de conocimientos en formato JSON. Si una pregunta no existe, el usuario puede agregarla junto a su respuesta.

---

## 🚀 Cómo ejecutar el programa

Desde la raíz del proyecto, podés ejecutar el asistente usando Python 3:

```bash
python main.py
```

Por defecto, el programa buscará el archivo:

```
./data/preguntas.json
```

Si el archivo o el directorio `data/` no existen, **se crearán automáticamente** con una estructura vacía (`[]`).

---

## 📁 Usar otro archivo de preguntas

Podés especificar una ruta personalizada para el archivo JSON de preguntas con el parámetro `--file`:

```bash
python main.py --file ./ruta/a/mis_preguntas.json
```

> ✅ Si el archivo o su directorio no existen, se crearán automáticamente con una lista vacía.

---

## 📝 Cómo funciona

1. Se pide una pregunta al usuario.
2. Si la pregunta ya existe, se muestra la respuesta.
3. Si no existe:
   - Se buscan coincidencias parciales y se muestran opciones.
   - Podés elegir una opción, no hacer nada o agregar una nueva pregunta y respuesta.
4. Todas las preguntas nuevas se guardan en el archivo JSON.

---

## 🧱 Estructura de Archivos

```
preguntas_app/
├── main.py
├── data/
│   └── preguntas.json         ← archivo con preguntas (creado si no existe)
├── helpers/
│   ├── file_manager.py        ← manejo de lectura/escritura de JSON
│   ├── interact.py            ← lógica de interacción con el usuario
│   └── pregunta_service.py    ← lógica de negocio (validaciones, búsquedas)
```

---

## ✅ Requisitos

- Python 3.7 o superior

---

## 💡 Ejemplo de uso

```bash
¿Cuál es tu pregunta? (Escribe "salir" para terminar): ¿Qué es un DLC?
Respuesta: Un DLC (contenido descargable) es contenido adicional para un juego, como nuevos niveles o personajes, que se compra por separado.

¿Cuál es tu pregunta? (Escribe "salir" para terminar): salir
```

---

¡Listo para usar y ampliar! 🎉