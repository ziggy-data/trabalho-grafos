import numpy as np

def adj_para_incidencia(matriz_adj):
    num_vertices = len(matriz_adj)
    arestas = []
    for i in range(num_vertices):
        for j in range(i, num_vertices):
            if matriz_adj[i][j] != 0:
                for _ in range(matriz_adj[i][j]):
                    arestas.append((i, j))
    
    num_arestas = len(arestas)
    matriz_incidencia = np.zeros((num_vertices, num_arestas), dtype=int)
    
    for idx_aresta, (i, j) in enumerate(arestas):
        matriz_incidencia[i][idx_aresta] = 1
        if i != j:  # Não contar duas vezes se i == j (loops)
            matriz_incidencia[j][idx_aresta] = 1
    
    return matriz_incidencia, num_vertices, num_arestas

def calcular_graus(matriz_adj):
    graus = np.sum(matriz_adj, axis=1)
    return graus

def main():
    # Exemplo de uma matriz de adjacências
    matriz_adj = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    matriz_incidencia, num_vertices, num_arestas = adj_para_incidencia(matriz_adj)
    graus = calcular_graus(matriz_adj)
    
    print("Matriz de Adjacência:")
    print(np.array(matriz_adj))
    print("\nMatriz de Incidência:")
    print(matriz_incidencia)
    print(f"\nNúmero de Vértices: {num_vertices}")
    print(f"Número de Arestas: {num_arestas}")
    print(f"Grau de cada Vértice: {graus}")

if __name__ == "__main__":
    main()
