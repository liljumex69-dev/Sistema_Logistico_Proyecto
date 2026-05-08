"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: views.py
DESCRIPCIÓN: Interfaz de consola para Módulo de Reportes.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.reportes.services import ReporteService
from modules.pedidos.services import PedidoService
from utils.formatters import Formatters

class ReportesView:
    """Controlador de la vista para reportes."""
    
    def __init__(self) -> None:
        self.reporte_service = ReporteService()
        # Instanciamos PedidoService para obtener datos reales con los que trabajar
        self.pedido_service = PedidoService()

    def ejecutar(self) -> None:
        while True:
            print(Formatters.separador("MODULO 3: REPORTES Y ANALISIS"))
            print("1. Reporte de Retardos Acumulados (Recursividad)")
            print("2. Ranking de Eficiencia (QuickSort)")
            print("0. Volver al Menu Principal")
            
            opcion = input("Seleccione opcion: ").strip()
            
            if opcion == "1":
                self._mostrar_retardos()
            elif opcion == "2":
                self._mostrar_ranking()
            elif opcion == "0":
                break
            else:
                print("Opcion invalida.")
            input("\nPresione Enter para continuar...")

    def _mostrar_retardos(self) -> None:
        """Muestra la suma total de retrasos usando el algoritmo recursivo."""
        print("\n--- REPORTE DE RETARDOS (Algoritmo Recursivo) ---")
        
        pedidos = self.pedido_service.obtener_todos()
        
        if not pedidos:
            print("No hay pedidos para analizar.")
            return
        
        total_retardos = self.reporte_service.generar_reporte_retardos(pedidos)
        
        print(f"Total de pedidos analizados: {len(pedidos)}")
        print(f"Suma total de retrasos: {total_retardos} minutos")
        print(f"Promedio de retraso: {total_retardos / len(pedidos):.2f} minutos/pedido")

    def _mostrar_ranking(self) -> None:
        """Muestra los pedidos ordenados por mayor retraso usando QuickSort."""
        print("\n--- RANKING DE EFICIENCIA (QuickSort) ---")
        
        pedidos = self.pedido_service.obtener_todos()
        
        if not pedidos:
            print("No hay pedidos para analizar.")
            return
            
        pedidos_ordenados, metricas = self.reporte_service.generar_reporte_eficiencia(pedidos)
        
        print(f"\nMetricas del algoritmo:")
        print(f"- Comparaciones realizadas: {metricas.get('comparaciones', 0)}")
        print(f"- Particiones realizadas: {metricas.get('particiones', 0)}")
        
        print("\nPedidos ordenados por Mayor Retraso (Peor a Mejor):")
        # Invertimos la lista para mostrar el mayor retraso primero
        for i, p in enumerate(reversed(pedidos_ordenados)):
            print(f"  {i+1}. {p.id} | Retraso: {p.retraso} min | {p.distrito}")