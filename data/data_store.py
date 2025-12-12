# CAPA DE DATOS

class DataStore:
    def __init__(self):
        self.usuarios = {
            "admin": "1234",
            "doctor": "medico"
        }
        self.citas = []

    def validar_usuario(self, usuario, contraseña):
        return usuario in self.usuarios and self.usuarios[usuario] == contraseña

    def guardar_cita(self, cita):
        self.citas.append(cita)

    def obtener_citas(self):
        return self.citas
