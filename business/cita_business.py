# CAPA DE NEGOCIO

class CitaBusiness:
    def __init__(self, data_store):
        self.data = data_store

    def login(self, usuario, contraseña):
        return self.data.validar_usuario(usuario, contraseña)

    def crear_cita(self, paciente, cedula, fecha, hora, motivo):
        cita = {
            "Paciente": paciente,
            "Cédula": cedula,
            "Fecha": fecha,
            "Hora": hora,
            "Motivo": motivo
        }
        self.data.guardar_cita(cita)

    def listar_citas(self):
        return self.data.obtener_citas()
