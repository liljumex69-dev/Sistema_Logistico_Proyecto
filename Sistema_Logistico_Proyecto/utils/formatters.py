"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: formatters.py
DESCRIPCIÓN: Utilidades de formato para salida en consola y reportes.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Centraliza el formato visual para mantener consistencia en la interfaz CLI.
- separador() genera líneas alineadas para menús y encabezados de reportes.
- formato_fecha_hora() estandariza timestamps en logs y bitácoras.
================================================================================
"""
from datetime import datetime

class Formatters:
    """Métodos estáticos para estandarización de salida visual."""
    
    @staticmethod
    def formato_fecha_hora() -> str:
        """Retorna fecha y hora actual en formato DD/MM/YYYY HH:MM:SS."""
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    @staticmethod
    def separador(titulo: str = "", caracter: str = "=", longitud: int = 60) -> str:
        """
        Genera una línea separadora con título centrado opcional.
        Mejora la legibilidad de la consola durante la demostración.
        """
        linea = caracter * longitud
        if titulo:
            return f"\n{linea}\n{titulo.center(longitud)}\n{linea}\n"
        return f"\n{linea}\n"
    
    @staticmethod
    def formato_porcentaje(valor: float, decimales: int = 2) -> str:
        """Convierte un decimal a string con símbolo de porcentaje."""
        return f"{valor:.{decimales}f}%"