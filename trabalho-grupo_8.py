import numpy as np

def adj_para_incidencia(matriz_adj, direcionado=False):
    num_vertices = len(matriz_adj)
    arestas = []
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if matriz_adj[i][j] != 0:
                for _ in range(matriz_adj[i][j]):
                    if direcionado or (i <= j):
                        arestas.append((i, j))
    
    num_arestas = len(arestas)
    matriz_incidencia = np.zeros((num_vertices, num_arestas), dtype=int)
    
    for idx_aresta, (i, j) in enumerate(arestas):
        matriz_incidencia[i][idx_aresta] = 1
        if not direcionado:
            matriz_incidencia[j][idx_aresta] = 1
        else:
            matriz_incidencia[j][idx_aresta] = -1
    
    return matriz_incidencia, num_vertices, num_arestas


def calcular_graus(matriz_adj, direcionado=False):
    if direcionado:
        graus_saida = np.sum(matriz_adj, axis=1)
        graus_entrada = np.sum(matriz_adj, axis=0)
        return graus_saida, graus_entrada
    else:
        graus = np.sum(matriz_adj, axis=1)
        return graus

#Função pra implmentar o algoritmo de prim
def prim(matriz_adj):
    num_vertices = len(matriz_adj)
    selected = np.zeros(num_vertices, dtype=bool)
    selected[0] = True
    mst_edges = []
    
    while len(mst_edges) < num_vertices - 1:
        min_edge = float('inf')
        u, v = -1, -1
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and matriz_adj[i][j] != 0:
                        if matriz_adj[i][j] < min_edge:
                            min_edge = matriz_adj[i][j]
                            u, v = i, j
        if u != -1 and v != -1:
            mst_edges.append((u, v, min_edge))
            selected[v] = True
    
    return mst_edges

def main():
    # Exemplo de uma matriz de adjacências
    #         A  B  C  D
    matriz_adj = [[0, 1, 2, 0],  # A
                  [1, 0, 0, 1],  # B
                  [2, 0, 0, 3],  # C
                  [0, 1, 3, 0]]  # D
    
    direcionado = False  # Defina como False porque Prim requer um grafo não direcionado

    matriz_incidencia, num_vertices, num_arestas = adj_para_incidencia(matriz_adj, direcionado)
    graus = calcular_graus(matriz_adj, direcionado)
    
    print("Matriz de Adjacência:")
    print(np.array(matriz_adj))
    print("\nMatriz de Incidência:")
    print(matriz_incidencia)
    print(f"\nNúmero de Vértices: {num_vertices}")
    print(f"Número de Arestas: {num_arestas}")
    
    if direcionado:
        graus_saida, graus_entrada = graus
        print(f"Grau de Saída de cada Vértice: {graus_saida}")
        print(f"Grau de Entrada de cada Vértice: {graus_entrada}")
    else:
        print(f"Grau de cada Vértice: {graus}")

    mst_edges = prim(matriz_adj)
    print("\nÁrvore Geradora Mínima (AGM) - Algoritmo de Prim:")
    for u, v, weight in mst_edges:
        print(f"Aresta {u} - {v} com peso {weight}")

if __name__ == "__main__":
    main()
