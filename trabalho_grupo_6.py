import heapq


def print_grafo(grafo):
    for vertice in grafo:
        print(f"{vertice}: {grafo[vertice]}")


def grafo_para_matriz_adj(grafo, ponderado=False, direcionado=False):
    vertices = list(grafo.keys())
    n = len(vertices)
    indice_vertice = {vertices[i]: i for i in range(n)}

    matriz_adj = [[0] * n for _ in range(n)]

    if ponderado:
        for vertice in grafo:
            for vizinho, peso in grafo[vertice]:
                i, j = indice_vertice[vertice], indice_vertice[vizinho]
                matriz_adj[i][j] = int(peso)
                if not direcionado:
                    matriz_adj[j][i] = int(peso)
    else:
        for vertice in grafo:
            for vizinho in grafo[vertice]:
                i, j = indice_vertice[vertice], indice_vertice[vizinho]
                matriz_adj[i][j] = 1
                if not direcionado:
                    matriz_adj[j][i] = 1

    return matriz_adj, vertices


def verificar_arestas_negativas(grafo):
    for vertice in grafo:
        for vizinho, peso in grafo[vertice]:
            if int(peso) < 0:
                return True
    return False


def dfs_todos_caminhos(grafo, start, end, path, all_paths):
    path.append(start)
    if start == end:
        all_paths.append(list(path))
    else:
        for neighbor, weight in grafo[start]:
            if neighbor not in path:
                dfs_todos_caminhos(grafo, neighbor, end, path, all_paths)
    path.pop()


def calcular_custo(grafo, caminho):
    custo = 0
    for i in range(len(caminho) - 1):
        for vizinho, peso in grafo[caminho[i]]:
            if vizinho == caminho[i + 1]:
                custo += int(peso)
                break
    return custo


def main():
    vertices = input("Digite os vértices do grafo separados por espaço: ").split()
    direcionado = input("É um grafo direcionado? (s/n) ") in "sS"
    ponderado = input("É um grafo ponderado? (s/n) ") in "sS"

    grafo = {vertice: [] for vertice in vertices}
    for vertice in vertices:
        print("grafo:")
        print_grafo(grafo)
        arestas = int(input(f"Digite a quantidade de arestas que o vertice '{vertice}' tem: "))
        while len(grafo[vertice]) < arestas:
            if ponderado:
                print(f"vertice {vertice}: {grafo[vertice]}")
            else:
                vizinhos_str = ", ".join(grafo[vertice])
                print(f"vertice {vertice}: [{vizinhos_str}]")
            vizinho = input(f"Insira o vertice vizinho ao '{vertice}': ")
            assert vizinho in vertices, "Vertice vizinho não existente!"
            if ponderado:
                peso = input(f"Digite o peso da aresta entre '{vertice}' e '{vizinho}': ")
                grafo[vertice].append((vizinho, peso))
                if not direcionado and vertice != vizinho:
                    grafo[vizinho].append((vertice, peso))
            else:
                grafo[vertice].append(vizinho)
                if not direcionado and vertice != vizinho:
                    grafo[vizinho].append(vertice)

    print_grafo(grafo)

    if verificar_arestas_negativas(grafo):
        print("O grafo possui arestas negativas. O algoritmo de Dijkstra não pode ser aplicado.")
    else:
        start_vertex = input("Digite o vértice de origem para o algoritmo de Dijkstra: ")
        end_vertex = input("Digite o vértice de chegada para o algoritmo de Dijkstra: ")
        all_paths = []
        dfs_todos_caminhos(grafo, start_vertex, end_vertex, [], all_paths)

        if not all_paths:
            print(f"Não há caminho entre '{start_vertex}' e '{end_vertex}'.")
        else:
            print("Todos os caminhos e seus custos:")
            custos_caminhos = [(caminho, calcular_custo(grafo, caminho)) for caminho in all_paths]
            for caminho, custo in custos_caminhos:
                print(f"Caminho: {' -> '.join(caminho)}, Custo: {custo}")

            melhor_caminho = min(custos_caminhos, key=lambda x: x[1])
            print(
                f"\nMelhor caminho de '{start_vertex}' a '{end_vertex}': {' -> '.join(melhor_caminho[0])}, Custo: {melhor_caminho[1]}")


if __name__ == "__main__":
    main()
