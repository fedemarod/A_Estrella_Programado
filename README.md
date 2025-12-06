# Algoritmo A* - Implementación y Visualización

## Descripción

Este proyecto implementa el **algoritmo A\*** para la búsqueda de rutas óptimas en una cuadrícula. El objetivo es completar la implementación del algoritmo A\* en los archivos faltantes y proporcionar una interfaz visual para experimentar con el algoritmo en diferentes escenarios de tableros.

### Características principales:
- Visualización interactiva del algoritmo A\*
- Construcción dinámica de tableros
- Búsqueda de rutas óptimas desde un punto de inicio hasta un punto final
- Soporte para obstáculos en el tablero

## Requisitos previos

- Python 3.8 o superior
- Git

## Instalación

### 1. Descargar el proyecto

```bash
https://github.com/fedemarod/A_Estrella_Programado
cd a_start_clase
```

O si tienes el repositorio como ZIP:

```bash
# Extrae el archivo ZIP y navega a la carpeta
cd a_start_clase
```

### 2. Crear ambiente virtual

En Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

En Windows (Command Prompt):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

En Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Dependencias

El proyecto utiliza las siguientes librerías:

- **numpy** (2.3.5): Para operaciones matemáticas y manejo de matrices
- **pygame** (2.6.1): Para la visualización gráfica del tablero y el algoritmo

## Estructura del proyecto

```
a_start_clase/
├── main.py              # Punto de entrada - Ejecuta la visualización
├── visualizer.py        # Interfaz gráfica con pygame
├── board.py            # Clase del tablero
├── a_star.py           # Implementación del algoritmo A* (a completar)
├── structures.py       # Estructuras de datos auxiliares
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## Uso

### Ejecutar la visualización

```bash
python main.py
```

Esto abrirá una ventana interactiva donde puedes:

**Controles:**
- **1** - Modo obstáculos (arrastra para dibujar)
- **2** - Modo punto inicial (click para establecer)
- **3** - Modo punto objetivo (click para establecer)
- **4** - Ejecutar algoritmo A\*
- **C** - Limpiar tablero
- **ESC** - Salir

## Implementación del Algoritmo A\*

La implementación del algoritmo A\* debe completarse en el archivo `a_star.py`. El algoritmo debe incluir:

1. **Cálculo de heurísticas**: Distancia Manhattan o Euclidiana
2. **Exploración de nodos**: Utilizando colas de prioridad
3. **Reconstrucción de ruta**: Trazabilidad del camino encontrado
4. **Manejo de obstáculos**: Evitar nodos no transitable

### Pseudocódigo de referencia

```
función A*(inicio, objetivo, heuristica):
    lista_abierta = [inicio]
    lista_cerrada = []
    
    mientras lista_abierta no esté vacía:
        nodo_actual = nodo con menor f = g + h
        
        si nodo_actual == objetivo:
            retornar reconstruir_ruta(nodo_actual)
        
        lista_abierta.remover(nodo_actual)
        lista_cerrada.agregar(nodo_actual)
        
        para cada vecino de nodo_actual:
            si vecino en lista_cerrada:
                continuar
            
            g_temporal = g(nodo_actual) + distancia(nodo_actual, vecino)
            
            si vecino no en lista_abierta o g_temporal < g(vecino):
                actualizar g, h, f del vecino
                agregar vecino a lista_abierta
    
    retornar ninguna_ruta_encontrada
```

## Desarrollo

Para desarrollar y contribuir al proyecto:

1. Asegúrate de que el ambiente virtual esté activado
2. Abre los archivos en tu editor favorito
3. Completa la implementación en `a_star.py`
4. Prueba ejecutando `python main.py`

## Notas importantes

- El tablero tiene dimensiones configurables (por defecto 30 filas × 40 columnas)
- La ventana es redimensionable y el tablero se adapta automáticamente
- El algoritmo debe manejar correctamente los obstáculos y las paredes

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver los detalles en el archivo [LICENSE](LICENSE).

## Autor

Desarrollado como parte del ejercicio de maestría.

