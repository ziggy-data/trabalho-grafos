def print_grafo(grafo):
    for vertice in grafo:
        print(f"{vertice}: {grafo[vertice]}")

def main():
    vertices = input("Digite os vértices do grafo separados por espaço: ").split()
    direcionado = input("É um grafo direcionado? (s/n) ") in "sS"
    ponderado = input("É um grafo ponderado? (s/n) ") in "sS"

    grafo = {vertice: [] for vertice in vertices}
    for vertice in vertices:
        print(f"grafo:")
        print_grafo(grafo)
        arestas = int(input(f"Digite a quantidade de arestas que o vertice '{vertice}' tem: "))
        while len(grafo[vertice]) < arestas:
            print(f"vertice {vertice}: {grafo[vertice] if ponderado else f"[{", ".join(grafo[vertice])}]"}")
            vizinho = input(f"Insira o vertice vizinho ao '{vertice}': ")
            assert vizinho in vertices, "Vertice vizinho não existente!"
            if ponderado:
                peso = input(f"digite o peso da aresta entre '{vertice}' e '{vizinho}': ")
            grafo[vertice].append((vizinho, peso) if ponderado else vizinho)
            if not direcionado and not vizinho == vertice:
                grafo[vizinho].append((vertice, peso) if ponderado else vertice)
    
    print_grafo(grafo)

if __name__ == "__main__":
    main()
