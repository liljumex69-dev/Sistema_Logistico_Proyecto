"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: exceptions.py
DESCRIPCIÓN: Jerarquía de excepciones personalizadas para manejo de errores.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Permite diferenciar errores de lógica, validación y estructura.
- Facilita el debugging y cumple con buenas prácticas de programación defensiva.
- Base: PastipanException -> hereda de Exception estándar.
================================================================================
"""

class PastipanException(Exception):
    """Excepción base del dominio PASTIPAN."""
    pass

class ValidacionException(PastipanException):
    """Error durante la validación de datos de entrada."""
    pass

class RutaException(PastipanException):
    """Error relacionado con la gestión de rutas."""
    pass

class PedidoException(PastipanException):
    """Error relacionado con la gestión de pedidos."""
    pass

class EstructuraVaciaException(PastipanException):
    """Error al operar sobre una estructura de datos sin elementos."""
    pass