# Aquí se registrarán personas

class Familias:
    contador = 1
    familias = {}

    @staticmethod
    def agregar_familiares(func):
        def agregar_grupos(*args, **kwargs):
            resultado = func(*args, **kwargs)
            Familias.familias[Familias.contador] = resultado
            Familias.contador += 1
            return resultado
        return agregar_grupos


class Persona:
    """Esta es la clase Persona en la cual se definen las propiedades de las Personas"""

    def __init__(self, nombres: str, apellidos: str, edad: int, dni: str, correo: str, telefono: str):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.dni = dni
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        # Representación legible para impresión
        return (f'{self.nombres} {self.apellidos}, Edad: {self.edad}, DNI: {self.dni}, '
                f'Correo: {self.correo}, Teléfono: {self.telefono}')


class VerificarDatos:
    """Métodos estáticos para validar entradas de usuario"""

    @staticmethod
    def verificar_nombre() -> str:
        nombre = input('Ingrese sus nombres: ')
        while not (3 <= len(nombre) <= 30):
            print('Ingrese entre 3 y 30 caracteres')
            nombre = input('Ingrese sus nombres: ')
        return nombre

    @staticmethod
    def verificar_apellidos() -> str:
        apellidos = input('Ingrese sus apellidos: ')
        while not (2 <= len(apellidos) <= 30):
            print('Ingrese entre 2 y 30 caracteres')
            apellidos = input('Ingrese sus apellidos: ')
        return apellidos

    @staticmethod
    def verificar_edad() -> int:
        while True:
            try:
                edad = int(input('Ingrese su edad: '))
                if 1 <= edad <= 120:
                    return edad
                else:
                    print('Ingrese entre 1 y 120 años')
            except ValueError:
                print('Edad inválida, ingrese un número entero.')

    @staticmethod
    def verificar_dni() -> str:
        dni = input('Ingrese su dni: ')
        while not (len(dni) == 8 and dni.isdigit()):
            print('Ingrese un dni válido de 8 caracteres numéricos')
            dni = input('Ingrese su dni: ')
        return dni

    @staticmethod
    def verificar_correo() -> str:
        correo = input('Ingrese su correo: ')
        while not (5 <= len(correo) <= 50 and ('@' in correo and '.' in correo)):
            print('Ingrese un correo válido')
            correo = input('Ingrese su correo: ')
        return correo

    @staticmethod
    def verificar_telefono() -> str:
        telefono = input('Ingrese su teléfono: ')
        while not (len(telefono) == 9 and telefono.isdigit()):
            print('Ingrese un teléfono válido de 9 dígitos')
            telefono = input('Ingrese su teléfono: ')
        return telefono


@Familias.agregar_familiares
def generar_persona(personas: int):
    personas_creadas = []
    for _ in range(personas):
        persona = Persona(
            nombres=VerificarDatos.verificar_nombre(),
            apellidos=VerificarDatos.verificar_apellidos(),
            edad=VerificarDatos.verificar_edad(),
            dni=VerificarDatos.verificar_dni(),
            correo=VerificarDatos.verificar_correo(),
            telefono=VerificarDatos.verificar_telefono()
        )
        personas_creadas.append(persona)
    return personas_creadas


class Menu:
    @staticmethod
    def mostrar_menu():
        menu = {
            1: ['Agregar familia (personas)', Menu.agregar_familia],
            2: ['Mostrar familias y personas', Menu.mostrar_familias],
            3: ['Salir', None]
        }
        for k, v in menu.items():
            yield f'{k} - {v[0]}'

    @staticmethod
    def menu_opciones():
        opciones = {
            1: Menu.agregar_familia,
            2: Menu.mostrar_familias
        }

        while True:
            print("\nMenú:")
            for linea in Menu.mostrar_menu():
                print(linea)
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 3:
                    print("Saliendo del menú...")
                    break
                elif opcion in opciones:
                    opciones[opcion]()  # Ejecutar función
                else:
                    print("Opción inválida, intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

    @staticmethod
    def agregar_familia():
        while True:
            try:
                personas = int(input("¿Cuántas personas desea agregar a la familia? "))
                if personas <= 0:
                    print("Debe ingresar un número mayor que cero.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

        generar_persona(personas)
        print(f'Familia agregada con {personas} personas.\n')

    @staticmethod
    def mostrar_familias():
        if not Familias.familias:
            print("No hay familias registradas aún.")
            return

        print("\n--- Familias Registradas ---")
        for clave, lista_personas in Familias.familias.items():
            print(f'\nFamilia #{clave}:')
            for i, persona in enumerate(lista_personas, 1):
                print(f'  Persona {i}: {persona}')
        print('---------------------------\n')


if __name__ == "__main__":
    Menu.menu_opciones()