# sistema_citas
Descripción del Proyecto

Este proyecto implementa un Sistema de Gestión de Citas Médicas en consola, desarrollado en Python, utilizando una arquitectura en N capas, con conexión a una base de datos MySQL.

El objetivo es demostrar la estructura y el funcionamiento de un sistema real para la administración de citas, integrando:

Inicio de sesión (login)

Creación de citas médicas

Visualización de citas

Gestión modular y escalable mediante N capas

Este proyecto forma parte de la macroactividad del Primer Parcial de Ingeniería de Software.

/ProyectoCitasMedicas
│── main.py
│── requirements.txt
│── README.md
│
├── presentation
│   └── menu.py
│
├── business
│   ├── auth_service.py
│   └── cita_service.py
│
├── data
│   ├── db_connection.py
│   └── cita_dao.py
│
└── models
    └── cita.py

    ⚙️ Requisitos Previos
🔧 Software

Python 3.10 o superior

MySQL Server 5.7+ o 8+

MySQL Workbench (opcional)
