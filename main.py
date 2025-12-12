# PUNTO DE ENTRADA DEL SISTEMA

from data.data_store import DataStore
from business.cita_business import CitaBusiness
from ui.sistema_ui import SistemaUI

def main():
    data_store = DataStore()
    business = CitaBusiness(data_store)
    ui = SistemaUI(business)

    if ui.login_ui():
        ui.menu_principal()
    else:
        print("Acceso denegado.")

if __name__ == "__main__":
    main()
