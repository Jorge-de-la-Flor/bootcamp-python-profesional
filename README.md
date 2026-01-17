# Bootcamp Python Profesional 🐍

Repositorio del **Bootcamp Python Profesional**, cuyo objetivo principal es ofrecer un diagnóstico práctico de tus conocimientos de Python, desde lo más básico hasta programación orientada a objetos, todo concentrado en un único script.

## 🚀 Objetivo del diagnóstico

- Evaluar tu nivel real de Python leyendo y ejecutando código “del mundo real”.
- Exponer en un solo archivo muchos conceptos clave del lenguaje.
- Ayudarte a detectar qué partes entiendes bien y cuáles necesitas reforzar.

## 📂 Contenido actual

- `diagnostico_inicial.py`: Programa de consola que permite registrar familias y personas, e incluye, entre otros conceptos:
  - Clases y objetos (`Persona`, `Familias`, `Menu`, `VerificarDatos`).
  - Atributos de clase y de instancia.
  - Métodos especiales como `__str__`.
  - Métodos estáticos (`@staticmethod`).
  - Decoradores aplicados a funciones (`@Familias.agregar_familiares`).
  - Manejo de colecciones (`dict`, `list`, `enumerate`).
  - Estructuras de control (`if`, `while`, `for`, manejo de errores con `try/except`).
  - Entrada y salida por consola con `input()` y `print()`.
  - Bloque `if __name__ == "__main__":` para definir el punto de entrada.

Todo eso integrado en un pequeño sistema de menú para agregar familias, listar personas y trabajar con los datos en memoria.

## ▶️ Cómo usar este diagnóstico

1. Clona el repositorio y entra a la carpeta:

   ```bash
   git clone https://github.com/Jorge-de-la-Flor/bootcamp-python-profesional.git
   cd bootcamp-python-profesional
    ```

2. Ejecuta el script:

   ```bash
   python diagnostico_inicial.py
   ```

3. Interactúa con el menú:

    - Prueba cada opción varias veces.
    - Lee el código y trata de explicar qué hace cada clase, función y línea importante.
    - Marca con comentarios (# TODO, # no entiendo esto) las partes que no tengas claras.

4. Usa lo que no entiendas como guía para planificar tu estudio del bootcamp.

🧰 Requisitos:

- Python 3.10+ instalado.
- Editor de código recomendado: VS Code, PyCharm o similar.
- Conocimientos básicos de consola/terminal para ejecutar scripts.

📝 Ideas para el bootcamp

- Pedir al alumno que refactorice el código (por ejemplo, separar en módulos, añadir tests, mejorar validaciones).
- Proponer extensiones: eliminar, buscar o editar personas; guardar y cargar familias desde archivo o base de datos; añadir más campos.
- Usar este mismo diagnóstico como punto de partida para introducir buenas prácticas (tipado, docstrings, manejo de errores avanzado, etc.).
