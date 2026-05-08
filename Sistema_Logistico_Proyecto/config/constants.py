"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: constants.py
DESCRIPCIÓN: Constantes del sistema y enumeraciones de estados.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Centraliza valores inmutables para evitar 'hardcoding' en la lógica de negocio.
- Las enumeraciones (Enum) garantizan integridad de datos y autocompletado en IDE.
- VENTANA_SUNAT_MINUTOS cumple el criterio 1.c1 (aspectos normativos).
================================================================================
"""
from enum import Enum

class EstadoRuta(Enum):
    """Estados posibles para una ruta de despacho."""
    PENDIENTE = "pendiente"
    EN_CURSO = "en_curso"
    COMPLETADA = "completada"
    RETRASADA = "retrasada"
    CANCELADA = "cancelada"

class EstadoPedido(Enum):
    """Estados posibles para un pedido en el sistema."""
    REGISTRADO = "registrado"
    ASIGNADO = "asignado"
    EN_REPARTO = "en_reparto"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"

# Constantes normativas y operativas
VENTANA_SUNAT_MINUTOS = 30
ALERTA_TEMPRANA_MINUTOS = 15
ALERTA_CRITICA_MINUTOS = 30