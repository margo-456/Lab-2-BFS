
'''se importa la libreria Queue'''
from queue import Queue

class Grafo:
    '''Constructor con parametros numero de nodos'''
    def __init__(self, numero_nodos, dirigido=True):
        '''especifica el atributo de la instancia'''
        self.m_numero_nodos = numero_nodos
        ''''especifica el rango de retornos'''
        self.m_nodos = range(self.m_numero_nodos)
		
        '''atributo de  la instancia de la clase especifica grafo dirigido o no dirigido'''
        self.m_dirigido = dirigido
		
        '''genera el diccionario de lista '''
        self.m_adj_list = {nodo: set() for nodo in self.m_nodos}      
	
    '''Agregar los nodos al grafo '''
    def add_arista(self, nodo1, nodo2, peso=1):

        '''accede al diccionario de lista para agregar nodos 1 y 2'''
        self.m_adj_list[nodo1].add((nodo2, peso))
        '''condicion para un nodo no dirigo'''
        if not self.m_dirigido:
            self.m_adj_list[nodo2].add((nodo1, peso))
 
    '''contiene el parametro y va imprimir los valores'''
    def print_adj_list(self):
        '''Recorre cada uno de los elementos'''
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

  
    ''' Este es el docstring de la función bfs_traversal
      Los parámetros de la funcion  son: self y nodo_inicio
    '''



    
    def bfs_traversal(self, nodo_inicio):
        ''' Conjunto de nodos visitados '''
        visitado = set()
        cola = Queue()

        ''' se agrega el nodo inicio a la cola y la lista visitada'''
        cola.put(nodo_inicio)
        visitado.add(nodo_inicio)

        '''Se ejecuta la instrucion mientras tenga valores'''
        while not cola.empty():
            '''especifica el nodo actual y se imprime el nodo actual'''
            nodo_actual = cola.get()
            print(nodo_actual, end = " ")

           

            ''' Obtener todos los vértices adyacentes '''
            for (next_node, weight) in self.m_adj_list[nodo_actual]:
                ''' si el nodo no es visitado'''
                if next_node not in visitado:
                    cola.put(next_node)

                    ''' visitar el nodo  y ponerlo en cola'''
                    visitado.add(next_node)










'''metodo main para la ejecucion del programa'''
if __name__ == "__main__":
    '''se crea la instancia del
     objeto tipo grafo especifica como parametro el numero de nodos y el tipo de grafo'''
    g = Grafo(8, dirigido=False)
    '''Se agrega el numero de nodos para recorrer'''
    g.add_arista(0, 1)
    g.add_arista(0, 2)
    g.add_arista(0, 3)
    g.add_arista(0, 4)
    g.add_arista(1, 2)
    g.add_arista(2, 3)
    g.add_arista(2, 5)
    g.add_arista(3, 4)
    g.add_arista(3, 5)
    g.add_arista(4 ,5)
    g.add_arista(6 ,5)
    g.add_arista(6 ,4)
    g.add_arista(7 ,4)
    g.add_arista(7 ,5)


    '''imprime el recorrido realizado ,se refiere a la lista de adyacencia'''
    g.print_adj_list()
    '''Imprimir el mensaje especifica el recorrido'''

    print ("Recorrido por amplitud" " (inicializa en el vertice 0)")
    g.bfs_traversal(0)
    print()

    #import doctest
    #doctest.testmod()