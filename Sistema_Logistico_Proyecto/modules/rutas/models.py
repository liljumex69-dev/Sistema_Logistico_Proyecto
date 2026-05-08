"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: models.py
DESCRIPCIÓN: Modelo de datos para Rutas.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
"""

# --- SOLUCIÓN TÉCNICA PARA IMPORTS ---
# Estas líneas permiten que Python encuentre la carpeta 'config' 
# aunque este archivo esté dentro de 'modules/rutas/'.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
# ------------------------------------

from dataclasses import dataclass
from datetime import time
from config.constants import EstadoRuta

@dataclass
class Ruta:
    """
    Representa una ruta de despacho de PASTIPAN.
    Atributos tipados para asegurar integridad de datos.
    """
    id: str
    nombre: str
    distrito_principal: str
    hora_salida: time
    conductor: str
    estado: EstadoRuta = EstadoRuta.PENDIENTE
    tiempo_retraso: float = 0.0

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.conductor} ({self.estado.value})"