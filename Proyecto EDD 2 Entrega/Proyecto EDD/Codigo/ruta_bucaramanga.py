# Importamos las librerías para trabajar con imágenes y para crear el árbol de rutas
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from bigtree import Node

# =================== CREACIÓN DEL ÁRBOL ===================

# Creamos el nodo raíz, o sea, el punto principal de partida
raiz = Node("UIS")

# De aquí para abajo vamos armando el árbol, conectando los lugares como si fueran las rutas reales
node_santoto = Node("SanToto", parent=raiz)
node_estadio = Node("Estadio", parent=raiz)
node_cronos = Node("Cronos Express", parent=node_santoto)
node_escuela = Node("Escuela la malaña", parent=node_santoto)
node_parque_morrorico = Node("Parque Morrorico", parent=node_estadio)
node_fitbella = Node("Fitbella", parent=node_estadio)
node_tatami = Node("Tatami Hostel", parent=node_cronos)
node_duvautos = Node("Duvautos", parent=node_cronos)
node_parque_agua = Node("Parque del agua", parent=node_parque_morrorico)
node_parque_ninos = Node("Parque de los niños", parent=node_parque_agua)
node_parque_centenario = Node("Parque centenario", parent=node_parque_ninos)
node_homecenter = Node("Homecenter", parent=node_parque_centenario)
node_megamall = Node("Megamall", parent=node_parque_centenario)
node_parque_sanpio = Node("Parque San Pio", parent=node_megamall)
node_villas_girardot = Node("Villas de Girardot", parent=node_fitbella)
node_barrio_feria = Node("Barrio la Feria", parent=node_fitbella)
node_libro_total = Node("Libro Total", parent=node_parque_sanpio)
node_parque_palmas = Node("Parque las palmas", parent=node_parque_sanpio)

# =================== COORDENADAS DE CADA LUGAR ===================

# Diccionario que asocia cada lugar con su ubicación (x, y) en el mapa
lugares_mapa = {
    'UIS': (729, 34),
    'SanToto': (511, 140),
    'Estadio': (270, 296),
    'Cronos Express': (270, 90),
    'Escuela la malaña': (1250, 47),
    'Parque Morrorico': (1090, 266),
    'Fitbella': (288, 230),
    'Tatami Hostel': (1030, 152),
    'Duvautos': (290, 335),
    'Parque del agua': (1010, 330),
    'Parque de los niños': (760, 480),
    'Parque centenario': (603, 575),
    'Homecenter': (714, 724),
    'Megamall': (945, 330),
    'Parque San Pio': (995, 662),
    'Villas de Girardot': (259, 228),
    'Barrio la Feria': (145, 616),
    'Libro Total': (436, 685),
    'Parque las palmas': (941, 621)
}

# =================== FUNCIONES PARA EL PROGRAMA ===================

# Buscamos un nodo específico a partir de su nombre (tipo 'UIS', 'Megamall', etc.)
def buscar_nodo(raiz, nombre):
    if raiz.name == nombre:
        return raiz
    for hijo in raiz.children:
        resultado = buscar_nodo(hijo, nombre)
        if resultado:
            return resultado
    return None

# Búsqueda BFS (Breadth-First Search) para encontrar la ruta más corta entre dos lugares
def bfs(origen, destino):
    queue = [(origen, [origen])]
    while queue:
        (nodo, path) = queue.pop(0)
        if nodo.name == destino.name:
            return path
        for child in nodo.children:
            queue.append((child, path + [child]))
    return None

# =================== INTERACCIÓN CON EL USUARIO ===================

# Mostramos los lugares disponibles para que el usuario no se pierda
print("\n--- Lugares disponibles para viajar ---")
for lugar in lugares_mapa.keys():
    print(f"- {lugar}")
print("---------------------------------------\n")

# Pedimos al usuario el origen y el destino, o sea de dónde a dónde quiere ir
origen_nombre = input("Ingrese el lugar de ORIGEN (escríbalo igual que arriba): ").strip()
destino_nombre = input("Ingrese el lugar de DESTINO (escríbalo igual que arriba): ").strip()

# Buscamos los nodos correspondientes
nodo_origen = buscar_nodo(raiz, origen_nombre)
nodo_destino = buscar_nodo(raiz, destino_nombre)

# =================== LÓGICA PRINCIPAL ===================

# Verificamos que el origen y destino existan
if not nodo_origen or not nodo_destino:
    print(" El origen o el destino que escribió no existen. Vuelva a intentarlo.")
else:
    # Buscamos la ruta más corta con BFS
    ruta = bfs(nodo_origen, nodo_destino)

    # Cargamos el mapa de Bucaramanga
    img = mpimg.imread('Mapa_Bucaramanga.jpg') 
    fig, ax = plt.subplots()
    ax.imshow(img)

    # Dibujamos la ruta si se encontró
    if ruta:
        ruta_nombres = [n.name for n in ruta]
        print("\n Ruta encontrada:")
        print(" -> ".join(ruta_nombres))
        
        for i in range(len(ruta_nombres) - 1):
            x_values = [lugares_mapa[ruta_nombres[i]][0], lugares_mapa[ruta_nombres[i+1]][0]]
            y_values = [lugares_mapa[ruta_nombres[i]][1], lugares_mapa[ruta_nombres[i+1]][1]]
            ax.plot(x_values, y_values, marker='o', color='red')
    else:
        print(" No se encontró ruta, algo salió mal.")

    plt.axis('off')  # Quitamos los numeritos del eje
    plt.show()
