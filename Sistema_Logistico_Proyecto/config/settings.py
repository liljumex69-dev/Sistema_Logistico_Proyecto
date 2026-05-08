"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: settings.py
DESCRIPCIÓN: Configuración global del sistema y rutas de archivos.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Usa pathlib para manejo multiplataforma de rutas (buena práctica).
- DISTRITOS_COBERTURA define el alcance geográfico real de PASTIPAN.
- Configuración centralizada facilita mantenimiento y escalabilidad (c1.3).
================================================================================
"""
from pathlib import Path

# Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

# Configuración de logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Cobertura geográfica oficial de PASTIPAN (16 distritos)
DISTRITOS_COBERTURA = [
    "San Miguel", "Pueblo Libre", "Magdalena", "Jesús María",
    "La Victoria", "Lince", "Surquillo", "Lima",
    "San Borja", "San Isidro", "La Molina",
    "Surco", "Barranco", "Miraflores",
    "Ate", "San Luis", "San Juan de Miraflores"
]