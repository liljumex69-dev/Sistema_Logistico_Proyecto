"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: views.py
DESCRIPCIÓN: Interfaz de consola para Módulo de Pedidos.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.pedidos.services import PedidoService
from utils.formatters import Formatters

class PedidosView:
    """Controlador de la vista para gestión de pedidos."""
    
    def __init__(self) -> None:
        self.service = PedidoService()

    def ejecutar(self) -> None:
        while True:
            print(Formatters.separador("MODULO 2: GESTION DE PEDIDOS"))
            print("1. Ver Todos los Pedidos")
            print("2. Buscar Pedido por Telefono (Hash O(1))")
            print("3. Registrar Nuevo Pedido")
            print("4. Deshacer Ultimo Registro (Pila LIFO)")
            print("0. Volver al Menu Principal")
            
            opcion = input("Seleccione opcion: ").strip()
            
            if opcion == "1":
                self._ver_todos()
            elif opcion == "2":
                self._buscar()
            elif opcion == "3":
                self._registrar()
            elif opcion == "4":
                self._deshacer()
            elif opcion == "0":
                break
            else:
                print("Opcion invalida.")
            input("\nPresione Enter para continuar...")

    def _ver_todos(self) -> None:
        print("\n--- LISTA COMPLETA DE PEDIDOS ---")
        pedidos = self.service.obtener_todos()
        for p in pedidos:
            print(p)
        print(f"Total pedidos: {len(pedidos)}")

    def _buscar(self) -> None:
        tel = input("Ingrese numero de telefono: ").strip()
        resultado = self.service.buscar_por_telefono(tel)
        if resultado:
            print(f"ENCONTRADO: {resultado}")
        else:
            print("NO ENCONTRADO: No existe pedido con ese telefono.")

    def _registrar(self) -> None:
        print("\n--- NUEVO REGISTRO ---")
        id_p = input("ID Pedido (ej: P004): ").strip()
        tel = input("Telefono: ").strip()
        dir_ = input("Direccion: ").strip()
        dist = input("Distrito: ").strip()
        
        print(self.service.registrar_pedido(id_p, tel, dir_, dist))

    def _deshacer(self) -> None:
        print(self.service.deshacer_ultimo_registro())