import heapq

class Nodo:
    def __init__(self, posicion:tuple[int,int],
                 g:float, h:float, padre:"Nodo"=None):
        self.posicion = posicion
        self.g = g
        self.h = h
        self.f = g+h
        self.padre = padre
    
    def __lt__(self, other:"Nodo"):
        return self.f < other.f
    
    def __eq__(self, other:"Nodo"):
        return self.posicion == other.posicion

class ListaAbierta:

    def __init__(self):
        self.heap = []
    
    def push(self, nodo:Nodo):
        heapq.heappush(self.heap, nodo)

    def pop(self)->Nodo:
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0

    def contains(self, nodo_buscar:Nodo)->Nodo|None:
        for nodo in self.heap:
            if nodo == nodo_buscar:
                return nodo
        return None

class ListaCerrada:
    def __init__(self):
        self.lista = []

    def push(self, nodo:Nodo):
        self.lista.append(nodo)
    
    def contains(self, nodo_buscar:Nodo)->Nodo|None:
        for nodo in self.lista:
            if nodo == nodo_buscar:
                return nodo
        return None

if __name__ == "__main__":
    nodo1 = Nodo((0,0), 0, 100)
    print(nodo1)
    nodo2 = Nodo((0,0), 10, 10)
    print(nodo2)
    print( nodo1 > nodo2 )
    print( nodo1 < nodo2 )
    print("Son el mismo: ", nodo1 == nodo2)

    lista_abierta = ListaAbierta()
    lista_abierta.push(nodo1)
    lista_abierta.push(nodo2)
    print(lista_abierta.heap)
    nodo_salida = lista_abierta.pop()
    print(nodo_salida)
    print(lista_abierta.heap)

    nodo_contenido = lista_abierta.contains(Nodo((0,1), 0, 0))
    print(nodo_contenido)
