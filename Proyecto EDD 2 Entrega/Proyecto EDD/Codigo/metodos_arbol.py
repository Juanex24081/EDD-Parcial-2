# Metodos
from bigtree import Node

# Crear la raíz del árbol
raiz = Node("UIS")

# Crear nodos y establecer relaciones jerárquicas
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
 
# Mostrar el árbol
print(raiz.show())