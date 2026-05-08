"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: validators.py
DESCRIPCIÓN: Validadores de negocio y cumplimiento normativo.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS (Criterio 1.c1):
- ValidadorGeografico asegura que los pedidos solo se registren en distritos
  con cobertura logística real, evitando asignaciones inviables.
- ValidadorSUNAT verifica el cumplimiento de la ventana de 30 minutos,
  aspecto normativo crítico para la operación legal de PASTIPAN.
================================================================================
"""

# --- SOLUCIÓN TÉCNICA PARA IMPORTS ---
# Estas líneas aseguran que Python encuentre la carpeta 'config' 
# aunque ejecutemos este archivo desde dentro de 'utils'.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
# ------------------------------------

from config.constants import VENTANA_SUNAT_MINUTOS
from config.settings import DISTRITOS_COBERTURA

class ValidadorGeografico:
    """
    Validador para asegurar que los pedidos se asignen solo a zonas cubiertas.
    Evita errores operativos donde un conductor intenta ir a un distrito sin ruta.
    """
    
    @staticmethod
    def es_distrito_valido(distrito: str) -> bool:
        """
        Verifica si el distrito ingresado pertenece a la cobertura oficial.
        Normaliza la entrada (quita espacios y pone mayúsculas iniciales)
        para evitar falsos negativos por errores de tipeo.
        """
        if not distrito:
            return False
        
        # Normalización: "  surco " -> "Surco"
        distrito_limpio = distrito.strip().title()
        
        return distrito_limpio in DISTRITOS_COBERTURA

class ValidadorSUNAT:
    """
    Validador para cumplimiento de normativas SUNAT.
    Garantiza que los tiempos estimados de entrega no excedan la ventana permitida.
    """
    
    @staticmethod
    def cumple_ventana_entrega(tiempo_estimado_minutos: float) -> bool:
        """
        Retorna True si el tiempo estimado está dentro de los 30 minutos.
        Esto es crítico para evitar multas y mantener el SLA (Service Level Agreement).
        """
        return tiempo_estimado_minutos <= VENTANA_SUNAT_MINUTOS