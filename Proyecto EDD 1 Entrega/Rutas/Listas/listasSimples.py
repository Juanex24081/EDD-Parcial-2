class Ciudad:
    def __init__(self, nombreCiudad, distanciaOtraCiudad):
        self.nombreCiudad = nombreCiudad
        self.distanciaOtraCiudad = distanciaOtraCiudad
        self.siguienteCiudad = None

class ListaCiudades:
    def __init__(self):
        self.ciudadIncial = None #Cabeza

    def vacioLista(self):

        if self.ciudadIncial == None:
            print("Está vacia")

        else:
            
            print("Lista no vacia")

    def agregarCiudadInicial(self, nombreCiudad, distanciaOtraCiudad):
        ciudadNueva = Ciudad(nombreCiudad, distanciaOtraCiudad)

        if self.ciudadIncial == None:
            self.ciudadIncial = ciudadNueva

        else:
            ciudadNueva.siguienteCiudad = self.ciudadIncial
            self.ciudadIncial = ciudadNueva

    def agregarCiudadFinal(self, nombreCiudad, distanciaOtraCiudad):
        ciudadNueva = Ciudad(nombreCiudad, distanciaOtraCiudad)

        if self.ciudadIncial == None:
            self.ciudadIncial = ciudadNueva

        else:
            ciudadActual = self.ciudadIncial

            while not ciudadActual.siguienteCiudad == None:
                ciudadActual = ciudadActual.siguienteCiudad

            ciudadActual.siguienteCiudad = ciudadNueva

    def agregarCiudadAntesDe(self, nombreCiudad, distanciaOtraCiudad, ciudadBuscamos):
        ciudadNueva = Ciudad(nombreCiudad, distanciaOtraCiudad)

        if self.ciudadIncial is None:
            print("La lista está vacía.")
            return

        if self.ciudadIncial.nombreCiudad == ciudadBuscamos:
            ciudadNueva.siguienteCiudad = self.ciudadIncial
            self.ciudadIncial = ciudadNueva
            return

        ciudadActual = self.ciudadIncial
        ciudadAnterior = None

        while ciudadActual is not None:
            if ciudadActual.nombreCiudad == ciudadBuscamos:
                ciudadNueva.siguienteCiudad = ciudadActual
                ciudadAnterior.siguienteCiudad = ciudadNueva
                return 

            ciudadAnterior = ciudadActual
            ciudadActual = ciudadActual.siguienteCiudad

        print(f"No se encontró la ciudad {ciudadBuscamos}.")


    def agregarCiudadDespuesDe(self, nombreCiudad, distanciaOtraCiudad, ciudadBuscamos):
        ciudadNueva = Ciudad(nombreCiudad, distanciaOtraCiudad)

        if self.ciudadIncial is None:
            print("La lista está vacía.")
            return

        ciudadActual = self.ciudadIncial

        while ciudadActual is not None:
            if ciudadActual.nombreCiudad == ciudadBuscamos:
                ciudadNueva.siguienteCiudad = ciudadActual.siguienteCiudad
                ciudadActual.siguienteCiudad = ciudadNueva
                return 

            ciudadActual = ciudadActual.siguienteCiudad

        print(f"No se encontró la ciudad {ciudadBuscamos}.")


    def buscarCiudad(self, nombreCiudad):
        ciudadActual = self.ciudadIncial
        
        while ciudadActual is not None:  
            if ciudadActual.nombreCiudad == nombreCiudad:
                return ciudadActual  
            ciudadActual = ciudadActual.siguienteCiudad
        
        return None  



    def distanciaTotal(self, ciudadInicial, ciudadDestino):
        ciudadActual = self.buscarCiudad(ciudadInicial)
        if ciudadActual is None:
            return "Ciudad inicial no encontrada."

        distanciaCiudades = 0
        listaCiudades = []

        while ciudadActual is not None:
            listaCiudades.append(ciudadActual.nombreCiudad)  
             
            if ciudadActual.nombreCiudad == ciudadDestino:
                print(f"Ruta encontrada: {' -> '.join(listaCiudades)}")
                return distanciaCiudades  
            
            distanciaCiudades += ciudadActual.distanciaOtraCiudad 
            ciudadActual = ciudadActual.siguienteCiudad  

        return "Ciudad destino no encontrada."




    #Imprimir
    def imprimirLista(self):
        if self.ciudadIncial == None:
            print("Lista vacía")

        else:
            ciudad_actual = self.ciudadIncial

        while not ciudad_actual == None:
            print(ciudad_actual.nombreCiudad, end=" -> ")

            ciudad_actual = ciudad_actual.siguienteCiudad

        print("None")


lista = ListaCiudades()
lista.agregarCiudadInicial("Bucaramanga", 0) 
lista.agregarCiudadFinal("Floridablanca", 7)
lista.agregarCiudadFinal("Girón", 9)
lista.agregarCiudadFinal("Piedecuesta", 17)
lista.agregarCiudadFinal("San Gil", 96)
lista.agregarCiudadFinal("Barichara", 110)
lista.agregarCiudadFinal("Socorro", 120)
lista.agregarCiudadFinal("Barrancabermeja", 126)

lista.agregarCiudadDespuesDe("Lebrija", 20, "Bucaramanga")
lista.agregarCiudadAntesDe("Rionegro", 33, "Barrancabermeja")
lista.agregarCiudadDespuesDe("Zapatoca", 69, "Girón")
lista.agregarCiudadAntesDe("Vélez", 197, "Socorro")
lista.agregarCiudadDespuesDe("Málaga", 250, "Vélez")

lista.imprimirLista()

print("\n Rutas entre ciudades:")
print(lista.distanciaTotal("Girón", "Piedecuesta"), "\n")  
print(lista.distanciaTotal("Piedecuesta", "Vélez"), "\n")  
print(lista.distanciaTotal("Piedecuesta", "Piedecuesta"), "\n")  