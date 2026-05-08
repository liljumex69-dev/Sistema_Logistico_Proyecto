"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: recursion.py
DESCRIPCIÓN: Implementación de 3 métodos recursivos sustentados.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS (Criterio c2.3):
- La recursividad reemplaza bucles iterativos para simplificar lógica compleja.
- Se exige documentar explícitamente el CASO BASE y el PASO RECURSIVO.
- Justificación PASTIPAN: 
  * Suma de retrasos: Cálculo acumulativo para KPIs de eficiencia.
  * Conteo por estado: Reportes de satisfacción y cumplimiento.
  * Búsqueda binaria recursiva: Demostración técnica del paradigma Divide y Vencerás.
- Referencia Bibliográfica: Joyanes (2008), Cormen (2022).
================================================================================
"""

from typing import List, TypeVar, Optional, Callable

T = TypeVar('T')


class RecursividadPASTIPAN:
    """
    Clase estática que encapsula los 3 métodos recursivos requeridos.
    No mantiene estado interno; opera puramente sobre los argumentos de entrada.
    """
    
    @staticmethod
    def suma_retardos_acumulados(pedidos: List[any], indice: int) -> float:
        """
        MÉTODO RECURSIVO 1: Suma de Retardos Acumulados.
        
        PROPÓSITO:
        Calcular el tiempo total de retraso de una lista de pedidos para 
        determinar el cumplimiento de la ventana SUNAT (30 minutos).
        
        CASO BASE:
        indice == 0 -> Retorna el retraso del primer pedido (lista_pedidos[0].retraso).
        Detiene la recursión para evitar 'IndexError' o recursión infinita.
        
        PASO RECURSIVO:
        retraso_actual + suma_retardos_acumulados(pedidos, indice - 1)
        Acumula el retraso del pedido actual con la suma de los anteriores.
        
        COMPLEJIDAD:
        Temporal: O(n) -> Visita cada elemento una vez.
        Espacial: O(n) -> Profundidad de la pila de llamadas.
        """
        # Validación de seguridad
        if not pedidos or indice < 0:
            return 0.0
        
        # CASO BASE
        if indice == 0:
            # Asumimos que los objetos tienen atributo 'retraso' o son números directos
            return pedidos[0].retraso if hasattr(pedidos[0], 'retraso') else float(pedidos[0])
        
        # PASO RECURSIVO
        actual = pedidos[indice].retraso if hasattr(pedidos[indice], 'retraso') else float(pedidos[indice])
        return actual + RecursividadPASTIPAN.suma_retardos_acumulados(pedidos, indice - 1)
    
    @staticmethod
    def conteo_pedidos_por_estado(pedidos: List[any], indice: int, estado_objetivo: str) -> int:
        """
        MÉTODO RECURSIVO 2: Conteo de Pedidos por Estado.
        
        PROPÓSITO:
        Determinar cuántos pedidos se encuentran en un estado específico 
        (ej: "retrasado", "entregado") para reportes gerenciales.
        
        CASO BASE:
        indice < 0 -> Retorna 0.
        Indica que se ha recorrido toda la lista hacia atrás.
        
        PASO RECURSIVO:
        Si el pedido coincide: 1 + conteo(pedidos, indice - 1, estado)
        Si no coincide: 0 + conteo(pedidos, indice - 1, estado)
        
        COMPLEJIDAD:
        Temporal: O(n)
        Espacial: O(n)
        """
        # CASO BASE
        if indice < 0:
            return 0
        
        # Verificar coincidencia (maneja objetos con atributo 'estado' o strings directos)
        estado_actual = ""
        if hasattr(pedidos[indice], 'estado'):
            estado_actual = pedidos[indice].estado.value if hasattr(pedidos[indice].estado, 'value') else str(pedidos[indice].estado)
        else:
            estado_actual = str(pedidos[indice])
            
        coincide = 1 if estado_actual == estado_objetivo else 0
        
        # PASO RECURSIVO
        return coincide + RecursividadPASTIPAN.conteo_pedidos_por_estado(pedidos, indice - 1, estado_objetivo)
    
    @staticmethod
    def busqueda_binaria_recursiva(
        arr: List[T], 
        objetivo: any, 
        inicio: int, 
        fin: int, 
        key: Callable[[T], any] = None
    ) -> int:
        """
        MÉTODO RECURSIVO 3: Búsqueda Binaria Recursiva.
        
        PROPÓSITO:
        Buscar un elemento en una lista ordenada usando Divide y Vencerás.
        
        CASOS BASE:
        1. inicio > fin -> Retorna -1 (No encontrado).
           Ocurre cuando el rango de búsqueda se vacía.
        2. arr[medio] == objetivo -> Retorna medio (Encontrado).
        
        PASO RECURSIVO:
        Si objetivo < medio: Busca en la mitad izquierda [inicio, medio - 1]
        Si objetivo > medio: Busca en la mitad derecha [medio + 1, fin]
        
        COMPLEJIDAD:
        Temporal: O(log n) -> Reduce el espacio de búsqueda a la mitad en cada paso.
        Espacial: O(log n) -> Profundidad de la recursión.
        
        REFERENCIA: Cormen (2022), Capítulo 2.
        """
        # CASO BASE 1: Rango inválido (No encontrado)
        if inicio > fin:
            return -1
        
        # Calcular punto medio
        medio = (inicio + fin) // 2
        
        # Obtener valor del medio (soporta objetos con atributo o valores directos)
        valor_medio = key(arr[medio]) if key else arr[medio]
        valor_objetivo = key(objetivo) if key and hasattr(objetivo, '__dict__') else objetivo
        
        # CASO BASE 2: Encontrado
        if valor_medio == valor_objetivo:
            return medio
        
        # PASO RECURSIVO
        elif valor_objetivo < valor_medio:
            # Búsqueda en mitad izquierda
            return RecursividadPASTIPAN.busqueda_binaria_recursiva(
                arr, objetivo, inicio, medio - 1, key
            )
        else:
            # Búsqueda en mitad derecha
            return RecursividadPASTIPAN.busqueda_binaria_recursiva(
                arr, objetivo, medio + 1, fin, key
            )