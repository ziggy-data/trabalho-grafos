import numpy as np
from trabalho_grupo_2 import grafo_para_matriz_adj
from main import main

def bellman_ford(matriz_adj, vertice_fonte, vertice_destino, ponderado):
    num_vertices = len(matriz_adj)
    distancia = [float('inf')] * num_vertices
    predecessor = [-1] * num_vertices
    distancia[vertice_fonte] = 0
    
    if not ponderado:
        matriz_adj = np.where(matriz_adj != 0, 1, 0)
    
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                if matriz_adj[u][v] != 0:
                    if distancia[u] + matriz_adj[u][v] < distancia[v]:
                        distancia[v] = distancia[u] + matriz_adj[u][v]
                        predecessor[v] = u
    
    for u in range(num_vertices):
        for v in range(num_vertices):
            if matriz_adj[u][v] != 0:
                if distancia[u] + matriz_adj[u][v] < distancia[v]:
                    print("Grafo contém ciclo de peso negativo")
                    return None, None
    
    caminho = []
    atual = vertice_destino
    while atual != -1:
        caminho.append(atual)
        atual = predecessor[atual]
    caminho.reverse()
    
    if caminho[0] == vertice_fonte:
        return distancia[vertice_destino], caminho
    else:
        return float('inf'), []

def main_bellmanford():
    grafo, direcionado, ponderado = main()
    matriz_adj, rotulos = grafo_para_matriz_adj(grafo, ponderado, direcionado)
    
    vertice_fonte = int(input(f"Digite o índice do vértice de origem (0 a {len(rotulos)-1}): "))
    vertice_destino = int(input(f"Digite o índice do vértice de destino (0 a {len(rotulos)-1}): "))
    distancia, caminho = bellman_ford(matriz_adj, vertice_fonte, vertice_destino, ponderado)
    
    if distancia is not None:
        caminho_rotulado = [rotulos[v] for v in caminho]
        print(f"\nDistância do vértice {rotulos[vertice_fonte]} ao vértice {rotulos[vertice_destino]}: {distancia}")
        print(f"Caminho de menor custo do vértice {rotulos[vertice_fonte]} ao vértice {rotulos[vertice_destino]}: {caminho_rotulado}")
    else:
        print("Não foi possível encontrar um caminho.")

if __name__ == "__main__":
    main_bellmanford()