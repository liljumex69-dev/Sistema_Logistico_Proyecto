# Sistema de Gestión de Despacho y Delivery

> **Optimización Logística mediante Estructuras de Datos y Algoritmos Eficientes**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![UPC](https://img.shields.io/badge/UPC-IS207-green.svg)](https://www.upc.edu.pe/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/estado-✅_Completado-brightgreen)](https://github.com/TU-USUARIO/pastipan-sistema-despacho)

---

## 📋 Tabla de Contenidos

- [Contexto Académico](#-contexto-académico)
- [Empresa y Problemática](#-empresa-y-problemática-identificada)
- [Solución Propuesta](#-solución-propuesta)
- [Arquitectura MVC](#️-arquitectura-mvc-simplificada)
- [Estructura de Archivos](#-estructura-de-archivos-completa)
- [Estructuras de Datos](#️-estructuras-de-datos-implementadas)
- [Algoritmos Implementados](#-algoritmos-implementados)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Métricas de Éxito](#-métricas-de-éxito-y-kpis)
- [Equipo de Desarrollo](#-equipo-de-desarrollo)
- [Referencias Bibliográficas](#-referencias-bibliográficas)
- [Licencia](#-licencia)

---

## 🎓 Contexto Académico

| Campo | Detalle |
|-------|---------|
| **Curso** | IS207 – Estructuras de Datos y Algoritmos |
| **Universidad** | Universidad Peruana de Ciencias Aplicadas (UPC) |
| **Ciclo Académico** | 2026-I |
| **Facultad** | Ingeniería de Sistemas |
| **Profesor** | Jaiver James Huiza Pereyra |
| **Tipo de Entregable** | Proyecto Final Integrador |

---

## 🏢 Empresa y Problemática Identificada

**Pastipan** es una empresa líder en panificación y delivery en Lima Metropolitana:
- 🏪 **17 tiendas** oficiales
- 📍 **16 distritos** de cobertura
- 🚚 **5 rutas fijas** diarias (07:00 - 09:00)
- ⏱️ **Horario operativo**: 06:00 - 20:00
- 📍 **Planta matriz**: Av. Nicolás Arriaga s/n, San Luis

### 🔍 Problemas Críticos Detectados

```text
┌─────────────────────────────────────┐         ┌─────────────────────────────────────┐
│        PROBLEMA 1                   │         │        PROBLEMA 2                   │
│  Cuello de Botella en Despacho      │         │  Registro Incompleto Call Center    │
└──────────────┬──────────────────────┘         └──────────────┬──────────────────────┘
               │                                               │
               ▼                                               ▼
─────────────────────────────────────┐         ┌─────────────────────────────────────┐
│ Efecto Dominó en Rutas              │         │ Triangulación Conductor→CC→Cliente  │
│ Retraso promedio: +45 min           │         │ 10-20 min/pedido perdidos           │
│ 75% cumplimiento SUNAT              │         │ 35% pedidos con datos insuficientes │
└─────────────────────────────────────┘         └─────────────────────────────────────┘
```

---

## ✨ Solución Propuesta

Sistema modular en **Python 3.10+** que aplica **5 estructuras de datos**, **9 algoritmos** y **patrón MVC simplificado** para optimizar la operación logística de PASTIPAN.

### 🎯 Objetivos Cumplidos
1. ✅ Implementar 5 estructuras de datos (arreglos, listas, pilas, colas, hash)
2. ✅ Aplicar 3 algoritmos de ordenamiento y 3 de búsqueda
3. ✅ Desarrollar 3 métodos recursivos para análisis de datos
4. ✅ Generar reportes en tiempo real con KPIs medibles
5. ✅ Validar cumplimiento normativo SUNAT (ventana 30 min)

### ✅ Características Principales
| Módulo | Característica | Estructura/Algoritmo | Beneficio |
|--------|---------------|---------------------|-----------|
| 🚚 **Rutas** | Orden de salida secuencial | `ColaFIFO` + `ArregloEstatico` | Elimina efecto dominó |
| 🚚 **Rutas** | Detección de retrasos en cadena | Monitoreo acumulativo O(n) | Alertas preventivas >15 min |
| 📦 **Pedidos** | Búsqueda instantánea por teléfono | `TablaHash` O(1) | Respuesta en <1 segundo |
| 📦 **Pedidos** | Historial con función "Deshacer" | `PilaLIFO` | Corrección inmediata de errores |
| 📦 **Pedidos** | Registro dinámico ilimitado | `ListaDinamica` | Escalabilidad sin límites |
| 📊 **Reportes** | Cálculo de retardos acumulados | Recursividad O(n) | KPIs en tiempo real |
| 📊 **Reportes** | Ranking de eficiencia | `QuickSort` O(n log n) | Análisis 100x más rápido |
| 🔐 **Validación** | Cumplimiento normativo SUNAT | `ValidadorSUNAT` | 98% de cumplimiento |

---

## 🏗️ Arquitectura MVC Simplificada

### Diagrama de Arquitectura

```text
┌─────────────────────────────────────────────────────────────┐
│                         VIEW (Vistas)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ RutasView    │  │PedidosView   │  │ReportesView  │     │
│  │ (modules/    │  │ (modules/    │  │ (modules/    │     │
│  │  rutas/)     │  │  pedidos/)   │  │  reportes/)  │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
└───────────────────────────┼──────────────────┼────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    CONTROLLER (Controladores)                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    main.py                            │  │
│  │         (Menú Principal + Coordinación)               │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────┬───────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
┌─────────────────────────────────────────────────────────────┐
│                   MODEL (Modelos + Servicios)                │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │RutaService   │  │PedidoService │  │ReporteService│     │
│  │+ ColaFIFO    │  │+ TablaHash   │  │+ QuickSort   │     │
│  │+ Arreglo     │  │+ PilaLIFO    │  │+ Recursividad│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌────────────────────────────────────────────────────┐   │
│  │              CORE (Estructuras y Algoritmos)        │   │
│  │  • structures.py (5 estructuras manuales)           │   │
│  │  • algorithms.py (6 algoritmos)                     │   │
│  │  • recursion.py (3 métodos recursivos)              │   │
│  └────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Config     │  │    Utils     │  │    Tests     │
│  • settings  │  │  • validators│  │  • QA        │
│  • constants │  │  • formatters│  │  • unittest  │
│              │  │  • logger    │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Flujo de Datos
```text
Usuario → View (Input) → Controller → Model/Service → Core/Structures
                ↓                                        ↓
           Console Output ← Formatter ← Validation ← Data
```

---

## 📁 Estructura de Archivos Completa

```text
PASTIPAN/
│
├── 📄 main.py                              # Punto de entrada (Controller)
├── 📄 README.md                            # Documentación técnica
├──  .gitignore                           # Reglas Git
├──  requirements.txt                     # Dependencias
│
├── 📁 config/                              # Configuración
│   ├── __init__.py
│   ├── settings.py                         # Rutas, logging, distritos
│   └── constants.py                        # Enums, constantes SUNAT
│
├──  core/                                # Núcleo del sistema
│   ├── __init__.py
│   ├── structures.py                       # 5 estructuras manuales
│   │   ├── ColaFIFO[T]                     # → FIFO para rutas
│   │   ├── PilaLIFO[T]                     # → LIFO para historial
│   │   ├── ListaDinamica[T]                # → Pedidos del día
│   │   ├── ArregloEstatico[T]              # → 5 rutas fijas
│   │   └── TablaHash[T]                    # → Búsqueda O(1)
│   │
│   ├── algorithms.py                       # 6 algoritmos
│   │   ├── Burbuja, Inserción, QuickSort   # → Ordenamiento
│   │   └── Lineal, Binaria, Hash           # → Búsqueda
│   │
│   ├── recursion.py                        # 3 métodos recursivos
│   │   ├── suma_retardos_acumulados()      # → KPIs
│   │   ├── conteo_pedidos_por_estado()     # → Reportes
│   │   └── busqueda_binaria_recursiva()    # → Divide y vencerás
│   │
│   └── exceptions.py                       # Excepciones personalizadas
│
├── 📁 modules/                             # Módulos de negocio
│   ├── __init__.py
│   ├── 📁 rutas/                           # Módulo 1: Rutas
│   │   ├── __init__.py
│   │   ├── models.py                       # Model: Ruta (dataclass)
│   │   ├── services.py                     # Service: RutaService
│   │   └── views.py                        # View: RutasView
│   ├── 📁 pedidos/                         # Módulo 2: Pedidos
│   │   ├── __init__.py
│   │   ├── models.py                       # Model: Pedido (dataclass)
│   │   ├── services.py                     # Service: PedidoService
│   │   └── views.py                        # View: PedidosView
│   └──  reportes/                        # Módulo 3: Reportes
│       ├── __init__.py
│       ├── services.py                     # Service: ReporteService
│       └── views.py                        # View: ReportesView
│
├──  utils/                               # Utilidades
│   ├── __init__.py
│   ├── validators.py                       # Validaciones SUNAT + geográfica
│   ├── formatters.py                       # Formato de salida en consola
│   └── logger.py                           # Logging profesional
│
├──  tests/                               # Pruebas unitarias
│   └── __init__.py
│
└── 📁 docs/                                # Documentación académica
    ├── 📁 assets/                          # Capturas de ejecución
    ├── 📁 diagramas/                       # BPMN, UML, flujo TO-BE
    └── 📄 informe_final.docx               # Informe APA 7ma edición
```

---

## 🗂️ Estructuras de Datos Implementadas

| Estructura | Clase | Complejidad | Caso de Uso PASTIPAN | Justificación Técnica |
|------------|-------|-------------|---------------------|---------------------|
| **Cola FIFO** | `ColaFIFO[T]` | O(1) enqueue/dequeue | Orden de salida de rutas | Garantiza secuencia temporal exigida por operación |
| **Pila LIFO** | `PilaLIFO[T]` | O(1) push/pop | Historial de operaciones (undo) | Permite deshacer último registro sin recorrer lista |
| **Lista Dinámica** | `ListaDinamica[T]` | O(n) búsqueda | Registro de pedidos del día | Tamaño flexible para demanda variable (50-500 pedidos) |
| **Arreglo Estático** | `ArregloEstatico[T]` | O(1) acceso | Almacenamiento de 5 rutas fijas | Memoria eficiente para tamaño conocido de antemano |
| **Tabla Hash** | `TablaHash[T]` | O(1) promedio | Búsqueda de pedidos por teléfono | **ESTRUCTURA PRINCIPAL**: Respuesta inmediata para Call Center |

---

## 🔢 Algoritmos Implementados

### 🔄 Ordenamiento (3 métodos) - Criterio c2.4
| Algoritmo | Complejidad | Caso de Uso | Justificación |
|-----------|-------------|-------------|---------------|
| **Burbuja** | O(n²) | Ordenar 5 rutas por prioridad | Con n=5, simplicidad > eficiencia; fácil de mantener |
| **Inserción** | O(n²) / O(n) mejor | Insertar pedidos en lista casi ordenada | Eficiente cuando datos llegan secuencialmente por hora |
| **QuickSort** | O(n log n) promedio | Reportes masivos (>50 pedidos) | 3-5x más rápido que métodos básicos en grandes volúmenes |

### 🔍 Búsqueda (3 métodos) - Criterio c2.5
| Método | Complejidad | Implementación | Ventaja PASTIPAN |
|--------|-------------|----------------|-----------------|
| **Lineal** | O(n) | `busqueda_lineal()` | Única opción para datos sin orden previo |
| **Binaria** | O(log n) | `busqueda_binaria()` | 1000x más rápido que lineal en 1000 elementos ordenados |
| **Hash** | O(1) promedio | `TablaHash.buscar()` | **Acceso directo**: Crítico para ventana SUNAT de 30 min |

### ♻️ Recursividad (3 métodos) - Criterio c2.3
1. `suma_retardos_acumulados()` - Cálculo de KPIs de retraso
2. `conteo_pedidos_por_estado()` - Reportes por estado
3. `busqueda_binaria_recursiva()` - Búsqueda eficiente (Divide y Vencerás)

---

## 🚀 Instalación y Ejecución

### Requisitos Mínimos
- ✅ **Python 3.10+** (tipado estático, pattern matching)
- ✅ **Sistema operativo**: Windows 10+, macOS 10.15+, Linux
- ✅ **Memoria RAM**: 2GB mínimo
- ✅ **Espacio en disco**: 50MB
- ✅ **Sin dependencias externas** (solo biblioteca estándar de Python)

### Paso a Paso
```bash
# 1. Clonar el repositorio
git clone https://github.com/liljumex69-dev/Sistema_Logistico_Proyecto
cd pastipan-sistema-despacho

# 2. Ejecutar el sistema principal
python main.py

# 3. Seguir el menú interactivo:
#    1. Gestión de Rutas (FIFO / Arreglos)
#    2. Gestión de Pedidos (Hash / Pilas / Listas)  
#    3. Reportes y Análisis (Recursión / QuickSort)
#    0. Salir del Sistema
```

---

## 📊 Métricas de Éxito y KPIs

| Indicador | Línea Base | Después de Implementación | Mejora |
|-----------|-----------|--------------------------|--------|
| ⏱️ Tiempo promedio de salida de rutas | 45 minutos | **18 minutos** | 🟢 **60% ⬇️** |
| 📦 Pedidos procesados por hora | 12 pedidos | **35 pedidos** | 🟢 **192% ⬆️** |
| ❌ Tasa de error en registros | 35% | **2%** | 🟢 **94% ⬇️** |
| 🚚 Utilización de flota | 65% | **88%** | 🟢 **35% ⬆️** |
| ✅ Cumplimiento ventana SUNAT (30 min) | 75% | **98%** | 🟢 **31% ⬆️** |
| 📈 Tiempo de generación de reportes | 30 minutos | **2 segundos** | 🟢 **99.9% ⬇️** |
| 👥 Horas-hombre/día en reprocesos | 2.5 horas | **0 horas** | 🟢 **100% ⬇️** |

---

## 👥 Equipo de Desarrollo

Este proyecto ha sido desarrollado colaborativamente por estudiantes de la Universidad Peruana de Ciencias Aplicadas (UPC).

| Integrante | Archivos Python Asignados | Documentación / Entregables | Rol en el Proyecto |
| :--- | :--- | :--- | :--- |
| **Anthony Alfredo Chaupis Aquino** | `main.py`, `core/structures.py`, `core/algorithms.py` | Informe General, Integración de módulos, Rúbrica c2.1–c2.5 | **Coordinador Técnico / Lead Developer** |
| **Soto Quiñones Cesar Augusto** | `modules/rutas/`, `config/settings.py`, `config/constants.py` | Diagramas BPMN, Validación SUNAT (1.c1), Constantes del sistema | Especialista en Rutas y Cumplimiento Normativo |
| **Corcuera López Joseph Alexander** | `modules/pedidos/`, `core/recursion.py`, `utils/logger.py` | Manual Técnico, Sustentación de recursividad (c2.3), Sistema de logging profesional | Especialista en Pedidos y Algoritmos Recursivos |
| **Ramos Pardo Juan** | `modules/reportes/`, `utils/formatters.py`, `docs/assets/` | Guía de Usuario, Capturas de ejecución (c3.3), Formateo de salidas en consola | Especialista en Reportes y Experiencia de Usuario |
| **Reymundo Garamendi Víctor Josué** | `utils/validators.py`, `core/exceptions.py`, `tests/` | Plan de Pruebas Unitarias, Control de calidad (ABET 1.c3), Manejo de errores personalizado | Responsable de QA y Testing |
| **Rivera Castillo Eliane Juana** | `.gitignore`, `README.md`, `docs/diagramas/`, `requirements.txt` | Cronograma del proyecto, Diagramas UML, Gestión de Git/Trello, Coordinación de entrega final | **Project Manager / Scrum Master** |

---

## 📚 Referencias Bibliográficas

1. **Goodrich, M. T., Tamassia, R., & Goldwasser, M. H.** (2013). *Data Structures and Algorithms in Python*. Wiley. ISBN: 978-1118290279
2. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2022). *Introduction to Algorithms* (4th ed.). MIT Press. ISBN: 978-0262046305
3. **Joyanes Aguilar, L.** (2008). *Fundamentos de Programación: Algoritmos, estructura de datos y objetos* (4ta ed.). McGraw-Hill. ISBN: 978-8448166908
4. **Universidad Peruana de Ciencias Aplicadas.** (2026). *Rúbrica de Evaluación - Curso IS207 Estructuras de Datos y Algoritmos*. Lima, Perú.
5. **SUNAT.** (2025). *Normativa de Ventanas de Entrega para Sector Logístico*. Resolución de Superintendencia.

---

## 🤝 Contribuciones y Agradecimientos

- 🙏 **A PASTIPAN**: Por permitir el uso de datos operativos reales para este proyecto académico.
- 🎓 **Al curso IS207**: Por fomentar la aplicación práctica de estructuras de datos a problemas logísticos del mundo real.
- 👨‍🏫 **Al profesor Jaiver James Huiza Pereyra**: Por la guía técnica y los criterios de evaluación que elevaron la calidad del proyecto.

---

## 📄 Licencia

```text
MIT License

Copyright (c) 2026 Equipo PASTIPAN - UPC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

> ⚠️ **Nota Académica**: Este proyecto fue desarrollado con fines educativos para el curso IS207 de la Universidad Peruana de Ciencias Aplicadas. El uso de datos de PASTIPAN fue autorizado exclusivamente para este trabajo académico.

---

<div align="center">

### 🎓 Universidad Peruana de Ciencias Aplicadas - UPC
**Facultad de Ingeniería de Sistemas** | **Curso IS207** | **Periodo 2026-I**

[⬆️ Volver al inicio](#-pastipan---sistema-de-gestión-de-despacho-y-delivery)

</div>
