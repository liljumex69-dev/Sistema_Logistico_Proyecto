"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: views.py
DESCRIPCIÓN: Interfaz de consola para Módulo de Rutas.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.rutas.services import RutaService
from utils.formatters import Formatters

class RutasView:
    """Controlador de la vista para gestión de rutas."""
    
    def __init__(self) -> None:
        self.service = RutaService()

    def ejecutar(self) -> None:
        """Bucle principal del menú de rutas."""
        while True:
            print(Formatters.separador("MODULO 1: GESTION DE RUTAS"))
            print("1. Ver Rutas Programadas")
            print("2. Verificar Efecto Domino (Retrasos)")
            print("3. Simular Retraso en Ruta (Prueba)")
            print("0. Volver al Menu Principal")
            
            opcion = input("Seleccione opcion: ").strip()
            
            if opcion == "1":
                self._mostrar_rutas()
            elif opcion == "2":
                self._verificar_dominio()
            elif opcion == "3":
                self._simular_retraso()
            elif opcion == "0":
                break
            else:
                print("Opcion invalida.")
            input("\nPresione Enter para continuar...")

    def _mostrar_rutas(self) -> None:
        print("\n--- LISTA DE RUTAS (Arreglo Estatico) ---")
        rutas = self.service.obtener_lista_rutas()
        for r in rutas:
            if r:
                print(f"{r.id} | {r.nombre.ljust(12)} | Salida: {r.hora_salida.strftime('%H:%M')} | {r.conductor}")
        print(f"Total rutas: {len(rutas)}")

    def _verificar_dominio(self) -> None:
        print("\n--- ANALISIS DE EFECTO DOMINO (Cola FIFO) ---")
        alertas = self.service.verificar_efecto_dominio()
        if not alertas:
            print("TODO NORMAL: No hay efecto domino detectado.")
        else:
            for alerta in alertas:
                print(f">> {alerta}")

    def _simular_retraso(self) -> None:
        ruta_id = input("Ingrese ID de ruta (ej: R1): ").strip().upper()
        try:
            minutos = float(input("Ingrese minutos de retraso: "))
            print(self.service.simular_retraso(ruta_id, minutos))
        except ValueError:
            print("Error: Ingrese un numero valido.")