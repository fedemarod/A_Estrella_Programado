from board import Board
from structures import Nodo, ListaAbierta, ListaCerrada

class AStar:

    def __init__(self, board:Board, heuristica_function:callable):
        self.board = board
        self.heuristica = heuristica_function
        self.lista_abierta = ListaAbierta()
        self.lista_cerrada = ListaCerrada()

    def execute(self):

        nodo = Nodo(self.board.start_point, 0, 
                    h = self.__calcular_h(self.board.start_point)
                    )
        self.lista_abierta.push(nodo)

        camino_encontrado = False
        while not self.lista_abierta.is_empty() and not camino_encontrado:

            current_node = self.lista_abierta.pop()

            if current_node.posicion == self.board.end_point:
                camino_encontrado = True

            else:
                self.lista_cerrada.push(current_node)
                self.board.set_closed(current_node.posicion[0], current_node.posicion[1])

                vecinos = self.board.neighbors_8(current_node.posicion)
                for vecino_punto in vecinos:
                    vecino_nodo = Nodo(
                        posicion=vecino_punto,
                        g = current_node.g+1,
                        h = self.__calcular_h(vecino_punto),
                        padre=current_node
                    )
                    if self.lista_cerrada.contains(vecino_nodo):
                        continue
                    
                    en_lista_abierta = self.lista_abierta.contains(vecino_nodo)
                    if en_lista_abierta is None:
                        self.lista_abierta.push(vecino_nodo)
                        self.board.set_open(vecino_nodo.posicion[0], vecino_nodo.posicion[1])
                    else:
                        if vecino_nodo < en_lista_abierta:
                            en_lista_abierta.g = vecino_nodo.g
                            en_lista_abierta.h = vecino_nodo.h
                            en_lista_abierta.f = vecino_nodo.f
                            en_lista_abierta.padre = vecino_nodo.padre
            yield

        if camino_encontrado:
            camino = self.reconstruct_path(current_node)
            for point in camino:
                self.board.set_path(point[0], point[1])
        yield

    def reconstruct_path(self, current_node:Nodo):
        print(current_node)
        path = []
        while current_node is not None:
            path.append(current_node.posicion)
            current_node = current_node.padre
        path.reverse()
        return path


    def __calcular_h(self, point:tuple[int, int])->float:
        return self.heuristica(point, self.board.end_point)

def manhatan_heuristic(point_a:tuple[int, int], point_b:tuple[int, int])->float:
    return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])

def euclidian_heuristic(point_a:tuple[int, int], point_b:tuple[int, int])->float:
    cateto1 = (point_a[0]-point_b[0])**2
    cateto2 = (point_a[1]-point_b[1])**2
    return (cateto1+cateto2)**0.5


if __name__ == '__main__':
    board = Board(5, 5)
    board.start_point = (0, 0)
    board.end_point = (4, 4)
    astar = AStar(board, manhatan_heuristic)
    print('Manhatan: ')
    astar.execute()
    astar.heuristica = euclidian_heuristic
    print('Euclidian: ')
    astar.execute()

