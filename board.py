import numpy as np

class Board:
    """
    Clase que representa el tablero del algoritmo A*.
    Mantiene una matriz accesible para aplicar el algoritmo.
    """
    
    def __init__(self, cols, rows):
        """
        Inicializa el tablero.
        
        Args:
            cols: Número de columnas
            rows: Número de filas
        """
        self.cols = cols
        self.rows = rows
        
        # Matriz del tablero
        # 0 = celda vacía
        # 1 = obstáculo
        # 2 = punto inicial
        # 3 = punto objetivo
        self.matrix = np.zeros((rows, cols), dtype=int)
        
        # Estado de la interfaz
        self.start_point = None
        self.end_point = None
        self.mode = "obstacle"  # "obstacle", "start", "end"
        
    def get_cell_from_pos(self, pos, board_width, board_height):
        """Convierte coordenadas de píxeles a índices de celda."""
        x, y = pos
        
        # Calcular tamaño de celda dinámicamente
        cell_width = board_width / self.cols
        cell_height = board_height / self.rows
        
        col = int(x / cell_width)
        row = int(y / cell_height)
        
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return (row, col)
        return None
    
    def set_obstacle(self, row, col):
        """Coloca un obstáculo en la posición especificada."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.matrix[row, col] == 0:  # Solo si está vacío
                self.matrix[row, col] = 1
    
    def remove_obstacle(self, row, col):
        """Remueve un obstáculo."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.matrix[row, col] == 1:
                self.matrix[row, col] = 0
    
    def set_start(self, row, col):
        """Establece el punto inicial."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            # Limpiar punto inicial anterior
            if self.start_point:
                old_row, old_col = self.start_point
                self.matrix[old_row, old_col] = 0
            
            self.start_point = (row, col)
            self.matrix[row, col] = 2
    
    def set_end(self, row, col):
        """Establece el punto objetivo."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            # Limpiar punto objetivo anterior
            if self.end_point:
                old_row, old_col = self.end_point
                self.matrix[old_row, old_col] = 0
            
            self.end_point = (row, col)
            self.matrix[row, col] = 3
    
    def set_path(self, row, col):
        """Marca una celda como parte del camino encontrado."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.matrix[row, col] in [0, 5, 6]:  # Solo si está vacío o abierta
                self.matrix[row, col] = 4  # 4 = parte del camino

    def set_closed(self, row, col):
        """Marca una celda como cerrada (explorada)."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.matrix[row, col] in [0, 6]:  # Solo si está vacío o abierta
                self.matrix[row, col] = 5 # 5 = celda cerrada
    
    def set_open(self, row, col):
        """Marca una celda como abierta (en la frontera)."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.matrix[row, col] == 0:  # Solo si está vacío
                self.matrix[row, col] = 6  # 6 = celda abierta

    def clear_board(self):
        """Limpia el tablero."""
        self.matrix = np.zeros((self.rows, self.cols), dtype=int)
        self.start_point = None
        self.end_point = None
    
    def get_matrix(self):
        """Retorna la matriz para usar el algoritmo A*."""
        return self.matrix.copy()

    def neighbors(self, point: tuple[int, int]):
        """Retorna las celdas vecinas accesibles (no obstáculos)."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
        result = []
        row, col = point
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.matrix[r, c] != 1:  # No es un obstáculo
                    result.append((r, c))
        
        return result

    def neighbors_8(self, point: tuple[int, int]):
        """Retorna las celdas vecinas accesibles (no obstáculos), incluyendo diagonales."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Arriba, Abajo, Izquierda, Derecha
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales
        result = []
        row, col = point
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.matrix[r, c] != 1:  # No es un obstáculo
                    result.append((r, c))
        
        return result
       

if __name__ == "__main__":
    board = Board(10, 10)  # Ejemplo de uso de la clase Board
    board.set_start(0, 0)
    board.set_end(9, 9)
    board.set_obstacle(0, 1)    
    print("Vecinos de (0,0):", board.neighbors((0, 0)))
    print("Vecinos de (1,1):", board.neighbors((1, 1)))
    print("Vecinos de (9,9):", board.neighbors((9, 9)))
    print("Vecinos de (0,0):", board.neighbors_8((0, 0)))