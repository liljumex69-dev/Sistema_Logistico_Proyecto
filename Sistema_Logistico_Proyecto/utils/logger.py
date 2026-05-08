"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: logger.py
DESCRIPCIÓN: Configuración centralizada del sistema de logging.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Implementa logging profesional para trazabilidad de errores y auditoría.
- Genera archivos .log automáticos en la carpeta 'logs' para análisis posterior.
- Utiliza handlers separados para consola y archivo.
================================================================================
"""

# --- SOLUCIÓN TÉCNICA PARA IMPORTS ---
# Esta sección asegura que Python pueda encontrar la carpeta 'config' 
# aunque ejecutemos este archivo desde dentro de la carpeta 'utils'.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
# ------------------------------------

import logging
from config.settings import LOGS_DIR, LOG_LEVEL, LOG_FORMAT

def obtener_logger(nombre_modulo: str) -> logging.Logger:
    """
    Crea y configura un logger específico para cada módulo.
    Permite separar los logs de rutas, pedidos y reportes en archivos distintos.
    
    Args:
        nombre_modulo: Nombre identificativo (ej: 'modulo_rutas').
    
    Returns:
        Objeto Logger configurado.
    """
    # 1. Asegurar que la carpeta de logs exista físicamente
    # parents=True crea carpetas intermedias si faltan
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 2. Crear instancia del logger
    logger = logging.getLogger(nombre_modulo)
    logger.setLevel(getattr(logging, LOG_LEVEL.upper()))
    
    # 3. Evitar duplicación de mensajes si se llama varias veces
    if not logger.handlers:
        # Configuración de formato: Fecha - Nivel - Mensaje
        formatter = logging.Formatter(LOG_FORMAT)
        
        # Handler 1: Salida a consola (para ver errores en tiempo real)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Handler 2: Salida a archivo (para historial y auditoría)
        archivo_log = LOGS_DIR / f"{nombre_modulo}.log"
        file_handler = logging.FileHandler(archivo_log, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger