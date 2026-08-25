PUBLICACIONES = [
    {"titulo": "Primer post", "contenido": "Bienvenidos al blog."},
    {"titulo": "Segundo post", "contenido": "Seguimos practicando Python."},
]


def listar_publicaciones() -> None:
    """Muestra todas las publicaciones con una numeración legible."""

    if not PUBLICACIONES:
        print("No hay publicaciones.")
        return

    for numero, publicacion in enumerate(PUBLICACIONES, start=1):
        print(f"{numero}. {publicacion['titulo']}")
        print(f"   {publicacion['contenido']}")


def mostrar_resumen() -> None:
    """Informa cuántas publicaciones existen actualmente."""

    cantidad = len(PUBLICACIONES)
    texto = "publicación" if cantidad == 1 else "publicaciones"
    print(f"Total: {cantidad} {texto}.")


if __name__ == "__main__":
    print("Mi blog por consola")
    listar_publicaciones()
    mostrar_resumen()


# __name__:
# __name__ es una variable especial que Python crea automáticamente para cada archivo (módulo).
# Su valor cambia según cómo se esté usando ese archivo
# Si ejecutás el archivo directamente (por ejemplo, python blog.py), Python le asigna a __name__
# el valor "__main__".
# Si el archivo es importado desde otro archivo (por ejemplo, con import blog),
# Python le asigna a __name__ el nombre del archivo (en este caso, "blog"), no "__main__"


# if __name__ == "__main__":
# Esto pregunta: "¿Este archivo se está ejecutando directamente (no fue importado)?"
# Si la respuesta es sí → ejecuta el bloque de código de adentro (imprime el título, lista publicaciones,
# muestra resumen).
# Si la respuesta es no (o sea, el archivo fue importado desde otro lugar) → no ejecuta ese bloque.
# if __name__ == "__main__": le dice a Python:
# ("ejecutá este bloque solo si este archivo es el que se corrió "
# "directamente, no si fue importado como una herramienta desde "
# "otro archivo").


# Tres estados:
# 1. Working Directory  →  2. Staging Area  →  3. Repository (commits)
#    (tu carpeta,            (área de           (historial guardado
#     donde editás)           preparación)        permanentemente)

# git status:
# te muestra el estado actual de tu repositorio: qué cambios hiciste, cuáles están listos para
# commitear y cuáles no, y en qué rama estás parado.

# git add:
# mueve cambios desde tu carpeta de trabajo hacia el staging area,
# marcándolos como "listos para el próximo commit".

# El staging area (también llamado "índice" o "index") es una zona intermedia entre los archivos de tu carpeta
# de trabajo y el historial de commits de Git. Podés pensarlo como una "sala de espera" o una "caja" donde vas
# juntando los cambios que querés que formen parte del próximo commit.

# 1. Estructura general (regla de las 7 reglas de Chris Beams)
#
# Es el estándar "clásico" más citado:
#
# Separar el asunto (subject) del cuerpo (body) con una línea en blanco
# Limitar el asunto a 50 caracteres (máximo ~72)
# Empezar el asunto con mayúscula
# No terminar el asunto con punto
# Usar modo imperativo en el asunto ("Add feature" en vez de "Added feature" o "Adds feature")
# Ajustar el cuerpo a 72 caracteres por línea
# Usar el cuerpo para explicar qué y por qué, no cómo
#
#
# Tipos más comunes:
#
# feat: nueva funcionalidad
# fix: corrección de un bug
# docs: cambios en documentación
# style: formato, espacios, punto y coma (sin cambios de lógica)
# refactor: cambio de código que no arregla bugs ni agrega features
# test: agregar o corregir tests
# chore: tareas de mantenimiento (dependencias, configs, etc.)
# perf: mejoras de rendimiento
# ci: cambios en integración continua
#
#
# feat(auth): agregar archivo blog.py