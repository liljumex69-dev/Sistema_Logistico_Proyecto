"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: services.py
DESCRIPCIÓN: Lógica de negocio para Rutas.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Usa ArregloEstatico (Estructura 4) porque las 5 rutas son fijas e inmutables.
- Usa ColaFIFO (Estructura 1) para garantizar el orden de salida secuencial.
- Implementa detección de 'Efecto Dominó' (acumulación de retrasos).
================================================================================
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from typing import List
from modules.rutas.models import Ruta
from core.structures import ColaFIFO, ArregloEstatico
from config.constants import EstadoRuta, ALERTA_CRITICA_MINUTOS
from datetime import time

class RutaService:
    """Gestiona el ciclo de vida de las rutas de despacho."""
    
    def __init__(self) -> None:
        # Estructura 4: Arreglo de tamaño fijo 5 (5 rutas reales de PASTIPAN)
        self.rutas_fijas: ArregloEstatico[Ruta] = ArregloEstatico(5)
        
        # Estructura 1: Cola FIFO para controlar el orden de salida
        self.cola_salida: ColaFIFO[Ruta] = ColaFIFO()
        
        self._cargar_rutas_reales()

    def _cargar_rutas_reales(self) -> None:
        """Inicializa el sistema con las 5 rutas operativas de PASTIPAN."""
        datos_rutas = [
            ("R1", "Norte", "San Miguel", time(7, 0), "Conductor A"),
            ("R2", "Centro", "La Victoria", time(7, 15), "Conductor B"),
            ("R3", "Este", "San Borja", time(7, 30), "Conductor C"),
            ("R4", "Sur", "Surco", time(7, 45), "Conductor D"),
            ("R5", "Extremo Sur", "Ate", time(8, 0), "Conductor E"),
        ]
        
        for i, (id_, nombre, distrito, hora, conductor) in enumerate(datos_rutas):
            ruta = Ruta(id_, nombre, distrito, hora, conductor)
            self.rutas_fijas.asignar(i, ruta)  # Acceso O(1)
            self.cola_salida.encolar(ruta)     # Encolamiento O(1)

    def obtener_lista_rutas(self) -> List[Ruta]:
        """Retorna todas las rutas cargadas en el arreglo."""
        return self.rutas_fijas.obtener_todos()

    def verificar_efecto_dominio(self) -> List[str]:
        """
        Analiza la cola de salida para detectar si un retraso arrastra a las siguientes rutas.
        Complejidad: O(n) donde n es el número de rutas (5).
        """
        alertas = []
        retraso_acumulado = 0.0
        
        # Creamos una copia temporal para iterar sin destruir la cola original
        cola_temporal = ColaFIFO()
        
        while not self.cola_salida.esta_vacia():
            ruta = self.cola_salida.desencolar()
            retraso_acumulado += ruta.tiempo_retraso
            
            if retraso_acumulado > ALERTA_CRITICA_MINUTOS:
                alertas.append(f"ALERTA CRITICA: {ruta.id} acumula {retraso_acumulado} min de retraso.")
            
            cola_temporal.encolar(ruta)
        
        # Restauramos la cola original
        while not cola_temporal.esta_vacia():
            self.cola_salida.encolar(cola_temporal.desencolar())
            
        return alertas

    def simular_retraso(self, ruta_id: str, minutos: float) -> str:
        """Simula un retraso en una ruta específica para pruebas."""
        for i in range(len(self.rutas_fijas)):
            ruta = self.rutas_fijas.obtener(i)
            if ruta and ruta.id == ruta_id:
                ruta.tiempo_retraso += minutos
                if ruta.tiempo_retraso > 0:
                    ruta.estado = EstadoRuta.RETRASADA
                return f"Retraso de {minutos} min aplicado a {ruta_id}."
        return "Ruta no encontrada."