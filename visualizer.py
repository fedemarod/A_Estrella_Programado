import pygame
import sys
from a_star import AStar, manhatan_heuristic
from board import Board

class Visualizer:
    """
    Visualizador del tablero del algoritmo A* usando Pygame.
    Permite crear y modificar el tablero de forma interactiva.
    """
    
    def __init__(self, width=800, height=600, rows=30, cols=40):
        """
        Inicializa el visualizador.
        
        Args:
            width: Ancho inicial de la ventana
            height: Alto inicial de la ventana
            rows: Número de filas del tablero
            cols: Número de columnas del tablero
        """
        pygame.init()
        
        # Dimensiones del tablero (filas x columnas)
        self.board_rows = rows
        self.board_cols = cols
        
        # Panel de instrucciones
        self.panel_width = 200
        
        # Dimensiones iniciales de la ventana
        self.width = width
        self.height = height
        self.board_width = width - self.panel_width
        self.board_height = height
        
        # Crear pantalla redimensionable
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Algoritmo A* - Visualizador")
        
        # Crear tablero - solo necesita saber filas y columnas
        self.board = Board(self.board_cols, self.board_rows)
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        
        # Estado del mouse
        self.mouse_pressed = False
        self.mouse_button = None
        
        # Fuente para el texto
        self.font_small = pygame.font.Font(None, 20)
        self.font_tiny = pygame.font.Font(None, 16)
        
        # Colores
        self.COLORS = {
            "background": (255, 255, 255),
            "grid": (200, 200, 200),
            "obstacle": (0, 0, 0),
            "start": (0, 255, 0),
            "end": (255, 0, 0),
            "path": (0, 0, 255),
            "closed": "#BB8528",
            "open": "#EAFF02",
            "empty": (255, 255, 255),
            "panel_bg": (240, 240, 240),
            "panel_border": (100, 100, 100),
            "text": (0, 0, 0),
            "text_light": (100, 100, 100)
        }
        
        # Configurar el algoritmo A*
        self.astar = AStar(
            board=self.board,
            heuristica_function=manhatan_heuristic
        )
        self.execute_pathfinding = False
        self.pathfinding_generator = None  # Guardar la instancia del generador
    
    def handle_events(self):
        """Maneja los eventos del teclado y mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.VIDEORESIZE:
                # Manejar redimensionamiento de ventana
                new_width, new_height = event.size
                # Asegurar dimensiones mínimas
                min_width = self.panel_width + 100
                min_height = 100
                new_width = max(new_width, min_width)
                new_height = max(new_height, min_height)
                
                self.width = new_width
                self.height = new_height
                self.board_width = new_width - self.panel_width
                self.board_height = new_height
                
                # Recrear pantalla
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.board.mode = "obstacle"
                    print("Modo: Agregar obstáculos (arrastra para dibujar)")
                elif event.key == pygame.K_2:
                    self.board.mode = "start"
                    print("Modo: Establecer punto inicial")
                elif event.key == pygame.K_3:
                    self.board.mode = "end"
                    print("Modo: Establecer punto objetivo")
                elif event.key == pygame.K_4:
                    self.execute_pathfinding = True
                    # Crear una nueva instancia del generador
                    self.pathfinding_generator = self.astar.execute()
                    print("Ejecutando algoritmo A*")                    
                elif event.key == pygame.K_c:
                    self.board.clear_board()
                    # self.astar = AStar(
                    #     board=self.board,
                    #     heuristic=Heuristic.MANHATTAN,  # Usar Manhattan
                    #     neighbors_type=4  # Vecinos 4-direccionales
                    # )                    
                    print("Tablero limpiado")
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.board.mode == "obstacle":
                    pos = pygame.mouse.get_pos()
                    # Solo procesar si estamos en el área del tablero (no en el panel)
                    if pos[0] < self.board_width:
                        self.mouse_pressed = True
                        self.mouse_button = event.button
                else:
                    # Para start y end, un simple click
                    pos = pygame.mouse.get_pos()
                    # Solo procesar si estamos en el área del tablero
                    if pos[0] < self.board_width:
                        cell = self.board.get_cell_from_pos(pos, self.board_width, self.board_height)
                        
                        if cell:
                            row, col = cell
                            
                            if self.board.mode == "start":
                                self.board.set_start(row, col)
                                print(f"Punto inicial establecido en ({row}, {col})")
                            
                            elif self.board.mode == "end":
                                self.board.set_end(row, col)
                                print(f"Punto objetivo establecido en ({row}, {col})")
            
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_pressed = False
                self.mouse_button = None
        
        # Procesar arrastre del mouse en modo obstáculos
        if self.mouse_pressed and self.board.mode == "obstacle":
            pos = pygame.mouse.get_pos()
            cell = self.board.get_cell_from_pos(pos, self.board_width, self.board_height)
            
            if cell:
                row, col = cell
                
                if self.mouse_button == 1:  # Click izquierdo
                    self.board.set_obstacle(row, col)
                elif self.mouse_button == 3:  # Click derecho
                    self.board.remove_obstacle(row, col)
    
    def draw(self):
        """Dibuja el tablero y la retícula."""
        self.screen.fill(self.COLORS["background"])
        # Calcular tamaño de cada celda dinámicamente
        cell_width = self.board_width / self.board_cols
        cell_height = self.board_height / self.board_rows
        
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                x = int(col * cell_width)
                y = int(row * cell_height)
                w = int(cell_width)
                h = int(cell_height)
                
                cell_value = self.board.matrix[row, col]
                
                # Determinar color según el tipo de celda
                if cell_value == 1:  # Obstáculo
                    color = self.COLORS["obstacle"]
                elif cell_value == 2:  # Punto inicial
                    color = self.COLORS["start"]
                elif cell_value == 3:  # Punto objetivo
                    color = self.COLORS["end"]
                elif cell_value == 4:  # Parte del camino
                    color = self.COLORS["path"]  # Azul para el camino
                elif cell_value == 5:  # Cerrado
                    color = self.COLORS["closed"]  # Rojo para cerrado
                elif cell_value == 6:  # Abierto
                    color = self.COLORS["open"]  # Verde para abierto
                else:  # Vacío
                    color = self.COLORS["empty"]
                
                # Dibujar celda
                pygame.draw.rect(self.screen, color, (x, y, w, h))
        
        # Dibujar retícula
        for row in range(self.board.rows + 1):
            y = int(row * cell_height)
            pygame.draw.line(self.screen, self.COLORS["grid"], 
                           (0, y), (self.board_width, y), 1)
        
        for col in range(self.board.cols + 1):
            x = int(col * cell_width)
            pygame.draw.line(self.screen, self.COLORS["grid"], 
                           (x, 0), (x, self.board_width), 1)
        
        # Dibujar panel de instrucciones
        self.draw_instructions_panel()
        
        pygame.display.flip()
    
    def draw_instructions_panel(self):
        """Dibuja el panel con las instrucciones en el lado derecho."""
        panel_x = self.board_width
        
        # Fondo del panel
        pygame.draw.rect(self.screen, self.COLORS["panel_bg"],
                        (panel_x, 0, self.panel_width, self.height))
        
        # Borde del panel
        pygame.draw.line(self.screen, self.COLORS["panel_border"],
                        (panel_x, 0), (panel_x, self.height), 2)
        
        # Texto de instrucciones
        instructions = [
            ("CONTROLES:", self.font_small, self.COLORS["text"]),
            ("", self.font_tiny, self.COLORS["text"]),
            ("1 - Obstáculos", self.font_tiny, self.COLORS["text"]),
            ("   Arrastra", self.font_tiny, self.COLORS["text_light"]),
            ("", self.font_tiny, self.COLORS["text"]),
            ("2 - Punto Inicio", self.font_tiny, self.COLORS["text"]),
            ("   Click", self.font_tiny, self.COLORS["text_light"]),
            ("", self.font_tiny, self.COLORS["text"]),
            ("3 - Punto Objetivo", self.font_tiny, self.COLORS["text"]),
            ("   Click", self.font_tiny, self.COLORS["text_light"]),
            ("", self.font_tiny, self.COLORS["text"]),
            ("C - Limpiar", self.font_tiny, self.COLORS["text"]),
            ("", self.font_tiny, self.COLORS["text"]),
            ("ESC - Salir", self.font_tiny, self.COLORS["text"]),
        ]
        
        y = 15
        for text, font, color in instructions:
            if text:
                surface = font.render(text, True, color)
                self.screen.blit(surface, (panel_x + 10, y))
            y += 22
    
    def print_instructions(self):
        """Imprime las instrucciones en consola."""
        print("\n" + "="*50)
        print("ALGORITMO A* - VISUALIZADOR")

        print("="*50)
        print("Controles:")
        print("  1 - Modo obstáculos (arrastra para dibujar)")
        print("  2 - Modo punto inicial")
        print("  3 - Modo punto objetivo")
        print("  C - Limpiar tablero")
        print("  ESC - Salir")
        print("="*50 + "\n")
    
    def run(self):
        """Ejecuta el visualizador."""
        self.print_instructions()
        
        while self.running:
            self.handle_events()
            #Aplicar logica
            if self.execute_pathfinding and self.board.start_point and self.board.end_point:
                try:
                    next(self.pathfinding_generator)
                except StopIteration:
                    self.execute_pathfinding = False
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()
    
    def get_board_matrix(self):
        """Retorna la matriz del tablero para usar el algoritmo A*."""
        return self.board.get_matrix()
    
    def get_board_state(self):
        """Retorna el estado actual del tablero."""
        return {
            "matrix": self.board.get_matrix(),
            "start": self.board.start_point,
            "end": self.board.end_point
        }
