"""Versión para publicar una rama y abrir un Pull Request."""

PUBLICACIONES = [
    {"titulo": "Primer post", "contenido": "Bienvenidos al blog."},
    {"titulo": "Segundo post", "contenido": "Seguimos practicando Python."},
    {"titulo": "Git y Python", "contenido": "Un cambio pequeño puede ser un commit."},
]


def listar_publicaciones(publicaciones: list[dict[str, str]] | None = None) -> None:
    elementos = PUBLICACIONES if publicaciones is None else publicaciones
    if not elementos:
        print("No hay publicaciones para mostrar.")
        return

    for numero, publicacion in enumerate(elementos, start=1):
        print(f"{numero}. {publicacion['titulo']}")
        print(f"   {publicacion['contenido']}")


def mostrar_resumen() -> None:
    cantidad = len(PUBLICACIONES)
    texto = "publicación" if cantidad == 1 else "publicaciones"
    print(f"Total: {cantidad} {texto}.")


def buscar_publicaciones(termino: str) -> list[dict[str, str]]:
    """Devuelve publicaciones cuyo título contiene el término indicado."""

    termino_normalizado = termino.strip().lower()
    if not termino_normalizado:
        return []

    return [
        publicacion
        for publicacion in PUBLICACIONES
        if termino_normalizado in publicacion["titulo"].lower()
    ]


def mostrar_menu() -> None:
    while True:
        print("\n=== Mi blog ===")
        print("1. Listar publicaciones")
        print("2. Mostrar resumen")
        print("3. Buscar por título")
        print("0. Salir")
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            listar_publicaciones()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            termino = input("Ingresá parte del título: ")
            listar_publicaciones(buscar_publicaciones(termino))
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Elegí 0, 1, 2 o 3.")


if __name__ == "__main__":
    mostrar_menu()





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

# git branch nombre-rama
#
#
# Moverte a una rama existente
# git checkout nombre-rama
#
#
# Crear y moverte a una rama en un solo paso (lo más común)
# git checkout -b nombre-rama
#
#
#
# git switch -c nombre-rama