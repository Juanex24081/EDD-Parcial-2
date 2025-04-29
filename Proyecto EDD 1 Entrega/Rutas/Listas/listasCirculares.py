class Ciudad:  
    def __init__(self, nombreCiudad, distanciaOtraCiudad):
        self.nombreCiudad = nombreCiudad
        self.distanciaOtraCiudad = distanciaOtraCiudad
        self.siguienteCiudad = None
        self.anteriorCiudad = None

class ListaCiudades:
    def __init__(self):
        self.ciudadInicial = None  
    
    def estaVacia(self): # Verifica si la lista esta vacia, por medio de reconocer si hay o no un elemento inicial
        return self.ciudadInicial is None

    def agregarCiudadInicial(self, nombreCiudad, distanciaOtraCiudad): # Agregamos una ciudad al inicio, en caso de que ya exista una en dicha posicion sencillamente le indicamos al apuntador del nuevo nodo que apunte a esta y se redefina la lista con este elemento como el elemento inicial
        ciudadNueva = Ciudad(nombreCiudad, distanciaOtraCiudad)
        if self.ciudadInicial is None:
            self.ciudadInicial = ciudadNueva
            self.ciudadInicial.siguienteCiudad = self.ciudadInicial
            self.ciudadInicial.anteriorCiudad = self.ciudadInicial
        else:
            ultimaCiudad = self.ciudadInicial.anteriorCiudad
            ciudadNueva.siguienteCiudad = self.ciudadInicial
            ciudadNueva.anteriorCiudad = ultimaCiudad
            self.ciudadInicial.anteriorCiudad = ciudadNueva
            ultimaCiudad.siguienteCiudad = ciudadNueva
            self.ciudadInicial = ciudadNueva

    def agregarCiudadFinal(self, nombreCiudad, distanciaOtraCiudad): #El ultimo elemento apunta a nuestro nuevo elemento en caso de que ya existan elementos en la lista
        ciudadNueva = Ciudad(nombreCiudad, distanciaOtraCiudad)
        if self.ciudadInicial is None:
            self.agregarCiudadInicial(nombreCiudad, distanciaOtraCiudad)
        else:
            ultimaCiudad = self.ciudadInicial.anteriorCiudad
            ultimaCiudad.siguienteCiudad = ciudadNueva
            ciudadNueva.anteriorCiudad = ultimaCiudad
            ciudadNueva.siguienteCiudad = self.ciudadInicial
            self.ciudadInicial.anteriorCiudad = ciudadNueva

    def buscarCiudad(self, nombreCiudad): # Recorremos nuestra lista de ciudades hasta encontrar la indicada
        if self.ciudadInicial is None:
            return None
        ciudadActual = self.ciudadInicial
        while True:
            if ciudadActual.nombreCiudad == nombreCiudad:
                return ciudadActual
            ciudadActual = ciudadActual.siguienteCiudad
            if ciudadActual == self.ciudadInicial:
                break
        return None

    def distanciaMasCorta(self, ciudadInicio, ciudadDestino): # Verifica las 2  maneras de llegar al mismo destino, normal o inversa, y retorna la mas corta de ellas 
        ciudadActual = self.buscarCiudad(ciudadInicio)
        if ciudadActual is None:
            return "Ciudad inicial no encontrada."
        ciudadDestinoNodo = self.buscarCiudad(ciudadDestino)
        if ciudadDestinoNodo is None:
            return "Ciudad destino no encontrada."

        distanciaNormal = 0
        recorridoNormal = []
        temp = ciudadActual
        while True:
            recorridoNormal.append(temp.nombreCiudad)
            if temp.nombreCiudad == ciudadDestino:
                break
            distanciaNormal += temp.distanciaOtraCiudad
            temp = temp.siguienteCiudad
        
        distanciaInversa = 0
        recorridoInverso = []
        temp = ciudadActual
        while True:
            recorridoInverso.append(temp.nombreCiudad)
            if temp.nombreCiudad == ciudadDestino:
                break
            distanciaInversa += temp.anteriorCiudad.distanciaOtraCiudad
            temp = temp.anteriorCiudad

        if distanciaNormal <= distanciaInversa:
            print(f"Ruta más corta: {' -> '.join(recorridoNormal)} (Distancia: {distanciaNormal} km) \n")
            return distanciaNormal
        else:
            print(f"Ruta más corta: {' -> '.join(recorridoInverso[::-1])} (Distancia: {distanciaInversa} km) \n")
            return distanciaInversa
        
    def buscarCiudadOrdenado(self, nombreCiudad):               #Busca la ciudada por medio del ordenamiento sort
        ciudades = []
        ciudadActual = self.ciudadInicial

        if ciudadActual is None:
         return None
    
        while True:
            ciudades.append(ciudadActual)
            ciudadActual = ciudadActual.siguienteCiudad
            if ciudadActual == self.ciudadInicial:
             break

        ciudades.sort(key=lambda ciudad: ciudad.nombreCiudad)

        for ciudad in ciudades:
            if ciudad.nombreCiudad == nombreCiudad:
              return ciudad

        return None

    def imprimirLista(self): # Similar al buscar recorre toda la lista imprimiendo las ciudades que contenga 
        if self.ciudadInicial is None:
            print("Lista vacía")
            return
        ciudadActual = self.ciudadInicial
        while True:
            print(f"{ciudadActual.nombreCiudad} -> ", end="")
            ciudadActual = ciudadActual.siguienteCiudad
            if ciudadActual == self.ciudadInicial:
                break
        print("Fin")


    def contarCiudades(self):                                   #Cuenta los elementos de la lista
        if self.ciudadInicial is None:
            return 0
        contador = 1
        ciudadActual = self.ciudadInicial.siguienteCiudad
        while ciudadActual != self.ciudadInicial:
            contador += 1
            ciudadActual = ciudadActual.siguienteCiudad
        return contador

lista = ListaCiudades()

if lista.estaVacia():                                           #Verifica si la lista esta vacia
    print("\n Estado de la Lista: La lista está vacía.")
else:
    print("\n Estado de la Lista: La lista tiene ciudades.")


lista.agregarCiudadInicial("Bucaramanga", 0) # Declaramos las ciudades 
lista.agregarCiudadFinal("Floridablanca", 7)
lista.agregarCiudadFinal("Girón", 9)
lista.agregarCiudadFinal("Piedecuesta", 17)
lista.agregarCiudadFinal("San Gil", 96)
lista.agregarCiudadFinal("Barichara", 110)
lista.agregarCiudadFinal("Socorro", 120)
lista.agregarCiudadFinal("Barrancabermeja", 126)
lista.agregarCiudadFinal("Zapatoca", 69)
lista.agregarCiudadFinal("Vélez", 197)
lista.agregarCiudadFinal("Málaga", 250)

nombre_ciudad = "San Gil"                                           # Buscar una ciudad en la lista
ciudad_buscada = lista.buscarCiudadOrdenado(nombre_ciudad)

if ciudad_buscada:
    print(f" Ciudad encontrada: {ciudad_buscada.nombreCiudad}.")
else:
    print(f" Ciudad '{nombre_ciudad}' no encontrada.")


print("\n Lista de Ciudades:")
lista.imprimirLista()

print(f"\n Número total de ciudades en la lista: {lista.contarCiudades()}")    # Contar el número total de ciudades

print("\n Rutas más cortas entre ciudades:")
print("-" * 50)
lista.distanciaMasCorta("Bucaramanga", "San Gil") #Probamos los metodos
lista.distanciaMasCorta("San Gil", "Zapatoca")
lista.distanciaMasCorta("Girón", "Barrancabermeja")
lista.distanciaMasCorta("Barrancabermeja", "Bucaramanga")
print("-" * 50)