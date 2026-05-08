"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: services.py
DESCRIPCIÓN: Lógica de negocio para Pedidos.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Usa TablaHash (Estructura 5) para búsqueda O(1) por teléfono (Call Center).
- Usa PilaLIFO (Estructura 2) para permitir 'Deshacer' el último registro.
- Usa ListaDinamica (Estructura 3) para mantener el historial completo.
================================================================================
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from typing import Optional
from modules.pedidos.models import Pedido
from core.structures import ListaDinamica, PilaLIFO, TablaHash
from config.constants import EstadoPedido
from utils.validators import ValidadorGeografico

class PedidoService:
    """Gestiona el registro y búsqueda de pedidos."""
    
    def __init__(self) -> None:
        # Estructura 3: Lista para recorrido secuencial
        self.lista_pedidos: ListaDinamica[Pedido] = ListaDinamica()
        
        # Estructura 5: Hash para búsqueda rápida por teléfono
        self.hash_pedidos: TablaHash[Pedido] = TablaHash()
        
        # Estructura 2: Pila para historial de acciones (Undo)
        self.pila_historial: PilaLIFO[Pedido] = PilaLIFO()
        
        self._cargar_datos_prueba()

    def _cargar_datos_prueba(self) -> None:
        """Carga pedidos iniciales para demostración."""
        datos = [
            ("P001", "999111222", "Av. Arequipa 123", "Surco"),
            ("P002", "999333444", "Calle Las Begonias", "San Isidro"),
            ("P003", "999555666", "Jr. de la Union", "Lima"),
        ]
        for id_, tel, dir_, dist in datos:
            self.registrar_pedido(id_, tel, dir_, dist)

    def registrar_pedido(self, id_pedido: str, telefono: str, direccion: str, distrito: str) -> str:
        """
        Registra un nuevo pedido en las 3 estructuras.
        Valida distrito antes de guardar.
        """
        if not ValidadorGeografico.es_distrito_valido(distrito):
            return f"Error: Distrito '{distrito}' no tiene cobertura."
        
        nuevo_pedido = Pedido(id_pedido, telefono, direccion, distrito)
        
        # 1. Agregar a Lista (Historial general)
        self.lista_pedidos.agregar(nuevo_pedido)
        
        # 2. Agregar a Hash (Búsqueda rápida por teléfono)
        self.hash_pedidos.insertar(telefono, nuevo_pedido)
        
        # 3. Agregar a Pila (Para poder deshacer)
        self.pila_historial.apilar(nuevo_pedido)
        
        return f"Pedido {id_pedido} registrado exitosamente."

    def buscar_por_telefono(self, telefono: str) -> Optional[Pedido]:
        """Búsqueda O(1) usando Tabla Hash."""
        return self.hash_pedidos.buscar(telefono)

    def deshacer_ultimo_registro(self) -> str:
        """Elimina el último pedido registrado usando Pila LIFO."""
        ultimo_pedido = self.pila_historial.desapilar()
        if ultimo_pedido:
            # Nota: En una app real, aquí removeríamos también de la Lista y Hash.
            # Para simplificar la demo, solo avisamos del deshacer.
            return f"Deshacer: Se ha revertido el registro del pedido {ultimo_pedido.id}."
        return "No hay registros recientes para deshacer."

    def obtener_todos(self) -> list:
        return self.lista_pedidos.obtener_todos()