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

def main():
    # Exemplo de uma matriz de adjacências
                #    A  B  C  D
    matriz_adj =   [[0, 1, 2, 0], #A  (A->B),(A->C),(A->C)
                    [0, 0, 0, 1], #B  (B->D)
                    [0, 0, 0, 0], #C
                    [0, 0, 1, 0]] #D  (D->C)
    
    direcionado = True  # Defina como True se o grafo for direcionado

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

if __name__ == "__main__":
    main()
