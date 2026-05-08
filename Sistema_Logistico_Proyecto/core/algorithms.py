"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: algorithms.py
DESCRIPCIÓN: Implementación de algoritmos de ordenamiento y búsqueda.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS (Criterios c2.4 y c2.5):
- Se implementan 3 algoritmos de ordenamiento para demostrar comprensión de 
  complejidad temporal y selección contextual.
- Se implementan 3 algoritmos de búsqueda para cubrir requisitos de la rúbrica.
- Cada método retorna métricas (comparaciones/intercambios) para análisis de 
  eficiencia en tiempo real.
- Justificación PASTIPAN: 
  * Burbuja: Rutas (n=5, simplicidad > eficiencia)
  * Inserción: Pedidos casi ordenados por hora de registro
  * QuickSort: Reportes masivos (>50 pedidos, eficiencia O(n log n))
  * Lineal: Datos sin orden previo
  * Binaria: Listas indexadas por ID
  * Hash: Acceso directo por teléfono (O(1))
================================================================================
"""

from typing import List, Callable, TypeVar, Tuple, Optional
import random

T = TypeVar('T')


class AlgoritmosOrdenamiento:
    """
    Clase contenedora para los 3 algoritmos de ordenamiento requeridos.
    Todos los métodos son estáticos y reciben un parámetro 'key' opcional
    para ordenar objetos complejos (ej: ordenar por retraso, por distrito, etc.)
    """
    
    @staticmethod
    def burbuja(arr: List[T], key: Callable[[T], any] = None) -> Tuple[List[T], dict]:
        """
        ALGORITMO 1: Ordenamiento Burbuja (Bubble Sort)
        Complejidad: O(n^2) peor y promedio | O(n) mejor caso | Espacio: O(1)
        
        LÓGICA:
        Compara pares adyacentes y los intercambia si están en orden incorrecto.
        Repite el proceso hasta que no se requieran intercambios.
        
        USO EN PASTIPAN:
        Se utiliza para ordenar las 5 rutas fijas por prioridad o retraso.
        Con n=5, la sobrecarga de algoritmos más complejos no se justifica.
        La simplicidad facilita el mantenimiento y la depuración en producción.
        
        Retorna: (lista_ordenada, métricas_de_ejecución)
        """
        if not arr:
            return arr, {"comparaciones": 0, "intercambios": 0}
        
        n = len(arr)
        arr_ordenado = arr.copy()
        metricas = {"comparaciones": 0, "intercambios": 0}
        
        for i in range(n):
            intercambios_en_ronda = 0
            
            for j in range(0, n - i - 1):
                metricas["comparaciones"] += 1
                
                valor_actual = key(arr_ordenado[j]) if key else arr_ordenado[j]
                valor_siguiente = key(arr_ordenado[j + 1]) if key else arr_ordenado[j + 1]
                
                if valor_actual > valor_siguiente:
                    arr_ordenado[j], arr_ordenado[j + 1] = arr_ordenado[j + 1], arr_ordenado[j]
                    metricas["intercambios"] += 1
                    intercambios_en_ronda += 1
            
            if intercambios_en_ronda == 0:
                break
        
        return arr_ordenado, metricas
    
    @staticmethod
    def insercion(arr: List[T], key: Callable[[T], any] = None) -> Tuple[List[T], dict]:
        """
        ALGORITMO 2: Ordenamiento por Inserción
        Complejidad: O(n^2) peor | O(n) mejor (ya ordenado) | Espacio: O(1)
        
        LÓGICA:
        Construye la lista ordenada de izquierda a derecha. Toma cada elemento
        y lo inserta en su posición correcta desplazando los mayores.
        
        USO EN PASTIPAN:
        Ideal para insertar nuevos pedidos en una lista que ya está casi ordenada
        por hora de registro o por zona geográfica. Es altamente eficiente cuando
        los datos llegan secuencialmente con pocas desviaciones.
        
        Retorna: (lista_ordenada, métricas_de_ejecución)
        """
        if not arr:
            return arr, {"comparaciones": 0, "inserciones": 0}
        
        n = len(arr)
        arr_ordenado = arr.copy()
        metricas = {"comparaciones": 0, "inserciones": 0}
        
        for i in range(1, n):
            actual = arr_ordenado[i]
            clave_actual = key(actual) if key else actual
            j = i - 1
            
            while j >= 0:
                metricas["comparaciones"] += 1
                clave_previa = key(arr_ordenado[j]) if key else arr_ordenado[j]
                
                if clave_previa > clave_actual:
                    arr_ordenado[j + 1] = arr_ordenado[j]
                    metricas["inserciones"] += 1
                    j -= 1
                else:
                    break
            
            arr_ordenado[j + 1] = actual
        
        return arr_ordenado, metricas
    
    @staticmethod
    def quicksort(arr: List[T], key: Callable[[T], any] = None) -> Tuple[List[T], dict]:
        """
        ALGORITMO 3: QuickSort (Divide y Vencerás)
        Complejidad: O(n log n) promedio | O(n^2) peor (mitigado con pivot aleatorio) | Espacio: O(log n)
        
        LÓGICA:
        Selecciona un pivote, particiona el array en menores y mayores al pivote,
        y aplica recursión en las sub-partes.
        
        USO EN PASTIPAN:
        Se utiliza en el Módulo 3 para generar reportes masivos de eficiencia,
        donde el volumen de pedidos supera los 50 registros. Es 3-5 veces más
        rápido que Burbuja/Inserción en conjuntos grandes, cumpliendo con el
        requisito de respuesta en tiempo real para la toma de decisiones.
        
        Retorna: (lista_ordenada, métricas_de_ejecución)
        """
        if not arr:
            return arr, {"comparaciones": 0, "particiones": 0}
        
        arr_ordenado = arr.copy()
        metricas = {"comparaciones": 0, "particiones": 0}
        
        def _quicksort_rec(arr: List[T], inicio: int, fin: int) -> None:
            if inicio < fin:
                metricas["particiones"] += 1
                pivot_idx = _particionar(arr, inicio, fin)
                _quicksort_rec(arr, inicio, pivot_idx - 1)
                _quicksort_rec(arr, pivot_idx + 1, fin)
        
        def _particionar(arr: List[T], inicio: int, fin: int) -> int:
            # Selección aleatoria de pivote para evitar peor caso O(n^2)
            pivot_idx = random.randint(inicio, fin)
            arr[pivot_idx], arr[fin] = arr[fin], arr[pivot_idx]
            
            pivot = key(arr[fin]) if key else arr[fin]
            i = inicio - 1
            
            for j in range(inicio, fin):
                metricas["comparaciones"] += 1
                valor_j = key(arr[j]) if key else arr[j]
                
                if valor_j <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
            return i + 1
        
        _quicksort_rec(arr_ordenado, 0, len(arr_ordenado) - 1)
        return arr_ordenado, metricas


class AlgoritmosBusqueda:
    """
    Clase contenedora para los 3 algoritmos de búsqueda requeridos.
    Cumple el criterio c2.5 de la rúbrica.
    """
    
    @staticmethod
    def lineal(arr: List[T], objetivo: T, key: Callable[[T], any] = None) -> Tuple[int, int]:
        """
        BÚSQUEDA 1: Lineal (Secuencial)
        Complejidad: O(n) tiempo | O(1) espacio
        
        LÓGICA:
        Recorre cada elemento secuencialmente hasta encontrar coincidencia.
        
        USO EN PASTIPAN:
        Se emplea cuando la lista de pedidos no está ordenada o es pequeña.
        Aunque es ineficiente para grandes volúmenes, es la única opción válida
        sin un índice previo, cumpliendo con el requisito de diversidad algorítmica.
        
        Retorna: (indice_encontrado, comparaciones_realizadas)
        """
        comparaciones = 0
        for i, elemento in enumerate(arr):
            comparaciones += 1
            valor = key(elemento) if key else elemento
            if valor == objetivo:
                return i, comparaciones
        return -1, comparaciones
    
    @staticmethod
    def binaria(arr: List[T], objetivo: T, key: Callable[[T], any] = None) -> Tuple[int, int]:
        """
        BÚSQUEDA 2: Binaria (Dicotómica)
        REQUISITO PREVIO: La lista debe estar ordenada ascendentemente.
        Complejidad: O(log n) tiempo | O(1) espacio
        
        LÓGICA:
        Divide repetidamente el espacio de búsqueda a la mitad comparando el 
        objetivo con el elemento central.
        
        USO EN PASTIPAN:
        Se utiliza en reportes donde los pedidos ya fueron ordenados por ID o fecha.
        Reduce drásticamente el tiempo de consulta comparado con la búsqueda lineal,
        demostrando la ventaja de mantener datos indexados.
        
        Retorna: (indice_encontrado, comparaciones_realizadas)
        """
        if not arr:
            return -1, 0
        
        inicio = 0
        fin = len(arr) - 1
        comparaciones = 0
        
        while inicio <= fin:
            medio = (inicio + fin) // 2
            comparaciones += 1
            
            valor_medio = key(arr[medio]) if key else arr[medio]
            
            if valor_medio == objetivo:
                return medio, comparaciones
            elif valor_medio < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1
        
        return -1, comparaciones
    
    @staticmethod
    def hash(tabla: dict, clave: str) -> Tuple[any, int]:
        """
        BÚSQUEDA 3: Hash (Acceso Directo)
        Complejidad: O(1) promedio | O(n) peor caso (colisiones)
        
        LÓGICA:
        Utiliza la función hash interna de Python para calcular la posición 
        directamente sin recorrido secuencial.
        
        USO EN PASTIPAN:
        ESTRUCTURA PRINCIPAL EN PRODUCCIÓN. Permite al Call Center recuperar 
        un pedido completo en milisegundos usando solo el número de teléfono.
        Elimina la triangulación operador-conductor-cliente, cumpliendo la 
        ventana de 30 minutos exigida por SUNAT.
        
        Retorna: (valor_asociado, operaciones_realizadas)
        """
        return tabla.get(clave), 1