44
4from collections import deque

def matriz_adj_para_lista_adj(matriz_adj):
    lista_adj = {}
    num_vertices = len(matriz_adj)
    for i in range(num_vertices):
        lista_adj[i] = []
        for j in range(num_vertices):
            if matriz_adj[i][j] != 0:
                for _ in range(matriz_adj[i][j]):
                    lista_adj[i].append(j)
    return lista_adj

def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n
    
    def bfs(start):
        queue = deque([start])
        colors[start] = 0
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 1 - current_color
            
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    return False
        return True
    
    for i in range(n):
        if colors[i] == -1:
            if not bfs(i):
                return False
                
    return True

def main():
    n = int(input("Digite o número de vértices: "))
    print("Digite a matriz de adjacência (linha por linha):")
    
    matriz_adj = []
    for i in range(n):
        linha = list(map(int, input().split()))
        if len(linha) != n:
            print(f"Erro: Cada linha deve conter exatamente {n} elementos.")
            return
        matriz_adj.append(linha)
    
    lista_adj = matriz_adj_para_lista_adj(matriz_adj)
    print("\nLista de Adjacência:")
    for key in lista_adj:
        print(f"{key}: {lista_adj[key]}")
    
    bipartido = is_bipartite(lista_adj)
    print(f"\nO grafo é bipartido? {'Sim' if bipartido else 'Não'}")

if __name__ == "__main__":
    main()
