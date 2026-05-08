"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: services.py
DESCRIPCIÓN: Lógica de negocio para Reportes y Análisis.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Este módulo demuestra el uso práctico de algoritmos complejos.
- Cumple c2.3: Usa Recursividad para sumar retardos acumulados.
- Cumple c2.4: Usa QuickSort para ordenar grandes volúmenes de datos eficientemente.
- No almacena datos propios; opera sobre la lista de pedidos recibida.
================================================================================
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from typing import List, Tuple
from core.recursion import RecursividadPASTIPAN
from core.algorithms import AlgoritmosOrdenamiento

class ReporteService:
    """
    Genera reportes analíticos aplicando algoritmos de ordenamiento y recursión.
    """
    
    def generar_reporte_retardos(self, lista_pedidos: List[any]) -> float:
        """
        REPORTE 1: Suma Total de Retardos.
        
        ALGORITMO: Recursividad (Criterio c2.3).
        PROPÓSITO: Calcular el impacto total de los retrasos en la operación.
        
        Retorna el total de minutos de retraso de todos los pedidos.
        """
        if not lista_pedidos:
            return 0.0
        
        # Llamada al método recursivo
        # Enviamos el índice del último elemento para empezar a recorrer hacia atrás
        total = RecursividadPASTIPAN.suma_retardos_acumulados(
            lista_pedidos, 
            len(lista_pedidos) - 1
        )
        return total

    def generar_reporte_eficiencia(self, lista_pedidos: List[any]) -> Tuple[List[any], dict]:
        """
        REPORTE 2: Eficiencia por Retraso (Ordenamiento).
        
        ALGORITMO: QuickSort (Criterio c2.4).
        PROPÓSITO: Identificar qué pedidos han sido los más problemáticos (mayor retraso).
        
        Retorna: (lista_ordenada, metricas_de_ejecucion)
        """
        if not lista_pedidos:
            return [], {}
        
        # Aplicamos QuickSort ordenando por el atributo 'retraso'
        lista_ordenada, metricas = AlgoritmosOrdenamiento.quicksort(
            lista_pedidos, 
            key=lambda p: p.retraso
        )
        
        return lista_ordenada, metricas