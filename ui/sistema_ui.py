# CAPA DE PRESENTACIÓN (UI)

class SistemaUI:
    def __init__(self, business):
        self.business = business

    # LOGIN
    def login_ui(self):
        print("\n=== INICIO DE SESIÓN ===")
        print("=== HealthCare360 ===")
        print("=== SIGH ===")
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        if self.business.login(usuario, contraseña):
            print("\n✔ Inicio de sesión exitoso\n")
            return True
        else:
            print("\n❌ Usuario o contraseña incorrectos\n")
            return False

    # CREAR CITA
    def crear_cita_ui(self):
        print("\n=== CREAR CITA MÉDICA ===")

        paciente = input("Nombre del paciente: ")
        cedula = input("Cédula: ")
        fecha = input("Fecha (DD/MM/AAAA): ")
        hora = input("Hora (HH:MM): ")
        motivo = input("Motivo de la consulta: ")

        self.business.crear_cita(paciente, cedula, fecha, hora, motivo)
        print("\n✔ Cita creada exitosamente\n")

    # MOSTRAR CITAS
    def mostrar_citas_ui(self):
        citas = self.business.listar_citas()

        print("\n=== LISTA DE CITAS REGISTRADAS ===")

        if not citas:
            print("No hay citas registradas.\n")
            return

        for i, c in enumerate(citas, 1):
            print(f"\nCita #{i}")
            for clave, valor in c.items():
                print(f"{clave}: {valor}")
        print()

    # MENÚ PRINCIPAL
    def menu_principal(self):
        while True:
            print("=== MENÚ PRINCIPAL ===")
            print("1. Crear cita médica")
            print("2. Ver citas registradas")
            print("3. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear_cita_ui()
            elif opcion == "2":
                self.mostrar_citas_ui()
            elif opcion == "3":
                print("\nSaliendo del sistema...\n")
                break
            else:
                print("❌ Opción inválida\n")
