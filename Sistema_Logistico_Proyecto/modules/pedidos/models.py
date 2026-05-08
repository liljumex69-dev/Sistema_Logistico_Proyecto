"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: models.py
DESCRIPCIÓN: Modelo de datos para Pedidos.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
"""

# --- SOLUCIÓN TÉCNICA PARA IMPORTS ---
# Estas líneas aseguran que Python busque en la carpeta raíz (donde está 'config')
# aunque este archivo esté profundamente dentro de 'modules/pedidos/'.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
# ------------------------------------

from dataclasses import dataclass
from config.constants import EstadoPedido

@dataclass
class Pedido:
    """
    Representa un pedido de delivery.
    """
    id: str
    telefono: str
    direccion: str
    distrito: str
    estado: EstadoPedido = EstadoPedido.REGISTRADO
    retraso: float = 0.0

    def __str__(self) -> str:
        return f"#{self.id} | Tel: {self.telefono} | {self.distrito} ({self.estado.value})"