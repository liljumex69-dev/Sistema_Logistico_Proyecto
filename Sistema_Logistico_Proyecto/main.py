#!/usr/bin/env python3
"""
================================================================================
PASTIPAN - SISTEMA DE GESTIÓN DE DESPACHO Y DELIVERY
PROYECTO: IS207 Estructura de Datos y Algoritmos - UPC 2026-I
--------------------------------------------------------------------------------
ARCHIVO: main.py
DESCRIPCIÓN: Punto de entrada y menú principal optimizado del sistema.
AUTORES: Anthony Alfredo Chaupis Aquino, Soto Quiñones Cesar Augusto,
Corcuera López Joseph Alexander, Ramos Pardo Juan, Reymundo Garamendi Víctor Josué,
Rivera Castillo Eliane Juana
================================================================================
NOTAS:
- Implementa menú interactivo con validación de entrada robusta.
- Manejo de excepciones global para prevenir cierres inesperados.
- Limpieza automática de consola entre módulos.
- Arquitectura modular: main.py solo coordina, no contiene lógica de negocio.
================================================================================
"""

import sys
import os
from datetime import datetime

# --- CONFIGURACIÓN DE RUTAS ---
# Agregar la carpeta raíz al path de Python para imports absolutos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ------------------------------


def limpiar_consola() -> None:
    """Limpia la pantalla de la consola (multiplataforma)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner() -> None:
    """
    Muestra el encabezado corporativo del sistema.
    Incluye fecha y hora actual para trazabilidad.
    """
    limpiar_consola()
    print("=" * 70)
    print("PASTIPAN - SISTEMA DE GESTION DE DESPACHO Y DELIVERY".center(70))
    print("=" * 70)
    print("Universidad Peruana de Ciencias Aplicadas - UPC".center(70))
    print("Curso: IS207 Estructura de Datos y Algoritmos".center(70))
    print("Periodo: 2026-I".center(70))
    print("=" * 70)
    print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}".center(70))
    print("=" * 70)


def mostrar_menu_principal() -> str:
    """
    Muestra el menú principal de opciones.
    
    Returns:
        str: Opción seleccionada por el usuario (validada)
    """
    print("\n" + "=" * 70)
    print("MENU PRINCIPAL".center(70))
    print("=" * 70)
    print("  1. Gestion de Rutas (FIFO / Arreglos Estaticos)")
    print("     - Ver rutas programadas")
    print("     - Detectar efecto domino por retrasos")
    print("=" * 70)
    print("  2. Gestion de Pedidos (Hash / Pilas LIFO / Listas)")
    print("     - Registrar nuevos pedidos con validacion geografica")
    print("     - Buscar pedidos por telefono (O(1))")
    print("     - Deshacer ultimo registro")
    print("=" * 70)
    print("  3. Reportes y Analisis (Recursion / QuickSort)")
    print("     - Calcular retardos acumulados (algoritmo recursivo)")
    print("     - Ranking de eficiencia (ordenamiento QuickSort)")
    print("=" * 70)
    print("  0. Salir del Sistema")
    print("=" * 70)
    
    return input("\n>> Seleccione una opcion [0-3]: ").strip()


def ejecutar_modulo_rutas() -> None:
    """Carga y ejecuta el Módulo 1: Gestión de Rutas."""
    try:
        from modules.rutas.views import RutasView
        vista = RutasView()
        vista.ejecutar()
    except ImportError as e:
        print(f"\n[ERROR] No se pudo cargar el modulo de rutas: {e}")
        print("[SOLUCION] Verifique que existan los archivos __init__.py")
    except Exception as e:
        print(f"\n[ERROR CRITICO] en modulo rutas: {e}")
    finally:
        input("\nPresione Enter para continuar...")


def ejecutar_modulo_pedidos() -> None:
    """Carga y ejecuta el Módulo 2: Gestión de Pedidos."""
    try:
        from modules.pedidos.views import PedidosView
        vista = PedidosView()
        vista.ejecutar()
    except ImportError as e:
        print(f"\n[ERROR] No se pudo cargar el modulo de pedidos: {e}")
        print("[SOLUCION] Verifique que existan los archivos __init__.py")
    except Exception as e:
        print(f"\n[ERROR CRITICO] en modulo pedidos: {e}")
    finally:
        input("\nPresione Enter para continuar...")


def ejecutar_modulo_reportes() -> None:
    """Carga y ejecuta el Módulo 3: Reportes."""
    try:
        from modules.reportes.views import ReportesView
        vista = ReportesView()
        vista.ejecutar()
    except ImportError as e:
        print(f"\n[ERROR] No se pudo cargar el modulo de reportes: {e}")
        print("[SOLUCION] Verifique que existan los archivos __init__.py")
    except Exception as e:
        print(f"\n[ERROR CRITICO] en modulo reportes: {e}")
    finally:
        input("\nPresione Enter para continuar...")


def main() -> None:
    """
    Función principal del sistema.
    Bucle infinito que mantiene el menú activo hasta que el usuario elija salir.
    """
    try:
        mostrar_banner()
        
        while True:
            opcion = mostrar_menu_principal()
            
            if opcion == "1":
                ejecutar_modulo_rutas()
                mostrar_banner()
                
            elif opcion == "2":
                ejecutar_modulo_pedidos()
                mostrar_banner()
                
            elif opcion == "3":
                ejecutar_modulo_reportes()
                mostrar_banner()
                
            elif opcion == "0":
                print("\n" + "=" * 70)
                print("SISTEMA CERRADO - Gracias por usar PASTIPAN".center(70))
                print("=" * 70 + "\n")
                sys.exit(0)
                
            else:
                print("\n[!] Opcion invalida. Por favor ingrese un numero del 0 al 3.")
                input("Presione Enter para reintentar...")
                mostrar_banner()
    
    except KeyboardInterrupt:
        print("\n\n[!] Sistema interrumpido por el usuario (Ctrl+C)")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR FATAL] El sistema ha encontrado un error inesperado: {e}")
        print("[ACCION] Contacte al administrador del sistema")
        sys.exit(1)


if __name__ == "__main__":
    main()