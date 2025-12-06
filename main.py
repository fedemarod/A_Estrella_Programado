"""
Punto de entrada para el visualizador del algoritmo A*.
Ejecuta la interfaz para construir el tablero.
"""

from visualizer import Visualizer

if __name__ == "__main__":
    # Configurar dimensiones del tablero
    # rows: número de filas del tablero
    # cols: número de columnas del tablero
    # La ventana se puede redimensionar y el tablero se adapta automáticamente
    
    visualizer = Visualizer(
        width=800,      # Ancho inicial de la ventana
        height=600,     # Alto inicial de la ventana
        rows=30,        # 30 filas
        cols=40         # 40 columnas
    )
    
    # Ejecutar la interfaz
    visualizer.run()
    
    # Después de cerrar, puedes acceder al estado del tablero:
    board_state = visualizer.get_board_state()
    start = board_state["start"]
    end = board_state["end"]
    matrix = board_state["matrix"]
    print("Punto inicial:", start)


    print("Punto objetivo:", end)
    print("Matriz del tablero:\n", matrix)
