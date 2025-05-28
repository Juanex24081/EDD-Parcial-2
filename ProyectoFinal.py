import networkx as nx
import matplotlib.pyplot as plt
import random
import pandas as pd
from networkx.algorithms.shortest_paths.dense import floyd_warshall_predecessor_and_distance

# Creamos el grafo vacío
Graph = nx.Graph()

# Lista con los barrios iniciales del mapa
nodos = [
    'Cabecera', 'Provenza', 'La Aurora', 'Real de Minas',
    'Mutis', 'UIS', 'San Alonso', 'Sotomayor',
    'San Francisco', 'Antonia Santos', 'Girardot', 'Diamante II',
    'La Victoria', 'La Joya', 'El Rocío', 'Morrorico'
]
Graph.add_nodes_from(nodos)

# Posiciones para que se vea como una cuadrícula 4x4
pos = {}
index = 0
for y in range(4):
    for x in range(4):
        pos[nodos[index]] = (x, 3 - y)
        index += 1

# Conectamos los nodos vecinos (derecha y abajo) con pesos aleatorios
for y in range(4):
    for x in range(4):
        idx = y * 4 + x
        current = nodos[idx]
        if x < 3:
            right = nodos[y * 4 + (x + 1)]
            peso = random.randint(2, 15)
            Graph.add_edge(current, right, weight=peso)
        if y < 3:
            down = nodos[(y + 1) * 4 + x]
            peso = random.randint(2, 15)
            Graph.add_edge(current, down, weight=peso)

# Función para mostrar el mapa completo de barrios
def mostrar_grafo():
    plt.figure(figsize=(8, 8))
    plt.gca().set_facecolor('#f5f5f5')
    nx.draw(Graph, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=8)
    labels = nx.get_edge_attributes(Graph, 'weight')
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels, font_size=6)
    plt.title('Mapa de barrios conectados')
    plt.grid(True)
    plt.show()

# Muestra el camino más corto entre dos barrios y lo resalta
def mostrar_camino(G, origen, destino):
    try:
        path = nx.dijkstra_path(G, origen, destino, weight='weight')
        distancia = nx.dijkstra_path_length(G, origen, destino, weight='weight')

        print("\nCamino más corto:")
        print(" -> ".join(path))
        print(f"Distancia total: {distancia} unidades\n")

        edge_list = list(zip(path[:-1], path[1:]))
        plt.figure(figsize=(8, 8))
        plt.gca().set_facecolor('#f5f5f5')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=8)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=1100)
        plt.title(f'Ruta más corta de {origen} a {destino}')
        plt.grid(True)
        plt.show()

    except nx.NetworkXNoPath:
        print("No hay un camino entre esos dos barrios.")
    except Exception as e:
        print("Error:", e)

# Muestra la matriz de distancias usando Floyd-Warshall
def floyd_warshall_con_tablas(G):
    pred, dist = floyd_warshall_predecessor_and_distance(G)
    nodos_ordenados = sorted(G.nodes())
    dist_matrix = []

    for u in nodos_ordenados:
        fila = []
        for v in nodos_ordenados:
            if u == v:
                fila.append(0)
            else:
                fila.append(dist[u][v] if v in dist[u] else float('inf'))
        dist_matrix.append(fila)

    df = pd.DataFrame(dist_matrix, index=nodos_ordenados, columns=nodos_ordenados)
    print("\nMatriz de distancias mínimas (Floyd-Warshall):\n")
    print(df)

# Agregamos un barrio nuevo al grafo
def agregar_barrio():
    nuevo = input("Nombre del nuevo barrio: ").strip()
    if nuevo in Graph.nodes:
        print("Ese barrio ya existe.")
    else:
        Graph.add_node(nuevo)
        print(f"Barrio '{nuevo}' agregado.")

# Creamos una conexión entre dos barrios existentes
def conectar_barrios():
    origen = input("Barrio de origen: ").strip()
    destino = input("Barrio de destino: ").strip()
    if origen in Graph.nodes and destino in Graph.nodes:
        try:
            peso = int(input("Distancia entre los barrios: "))
            Graph.add_edge(origen, destino, weight=peso)
            print(f"Conexión creada entre {origen} y {destino} con peso {peso}.")
        except:
            print("Error: el peso debe ser un número.")
    else:
        print("Uno o ambos barrios no existen.")

# Eliminamos un barrio del grafo
def eliminar_barrio():
    barrio = input("Nombre del barrio a eliminar: ").strip()
    if barrio in Graph.nodes:
        Graph.remove_node(barrio)
        print(f"Barrio '{barrio}' eliminado.")
    else:
        print("Ese barrio no existe.")

# Eliminamos una conexión entre dos barrios
def eliminar_conexion():
    u = input("Barrio 1: ").strip()
    v = input("Barrio 2: ").strip()
    if Graph.has_edge(u, v):
        Graph.remove_edge(u, v)
        print(f"Conexión entre '{u}' y '{v}' eliminada.")
    else:
        print("No existe esa conexión.")

# Buscamos si un barrio existe y muestro sus conexiones
def buscar_barrio():
    barrio = input("Ingrese el barrio a buscar: ").strip()
    if barrio in Graph.nodes:
        vecinos = list(Graph.neighbors(barrio))
        print(f"Barrio '{barrio}' encontrado. Conectado con: {', '.join(vecinos) if vecinos else 'ninguno.'}")
    else:
        print("Ese barrio no está en el grafo.")

# Menú de opciones principal
def menu():
    while True:
        print("\n========= MENÚ GRAFO DE BARRIOS =========")
        print("1. Ver mapa de barrios")
        print("2. Calcular camino más corto (Dijkstra)")
        print("3. Ver matriz de distancias (Floyd-Warshall)")
        print("4. Salir")
        print("5. Agregar barrio")
        print("6. Conectar barrios")
        print("7. Eliminar barrio")
        print("8. Eliminar conexión")
        print("9. Buscar barrio")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_grafo()
        elif opcion == '2':
            print("\nBarrios disponibles:", ", ".join(Graph.nodes))
            origen = input("Ingrese el barrio de origen: ").strip()
            destino = input("Ingrese el barrio de destino: ").strip()
            if origen in Graph.nodes and destino in Graph.nodes:
                mostrar_camino(Graph, origen, destino)
            else:
                print("Uno o ambos barrios no existen.")
        elif opcion == '3':
            floyd_warshall_con_tablas(Graph)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        elif opcion == '5':
            agregar_barrio()
        elif opcion == '6':
            conectar_barrios()
        elif opcion == '7':
            eliminar_barrio()
        elif opcion == '8':
            eliminar_conexion()
        elif opcion == '9':
            buscar_barrio()
        else:
            print("Opción inválida. Intente de nuevo.")

# Inicio del programa
if __name__ == "__main__":
    menu()
