class Zoologico:
    
    def __init__(self, nombre, ubicacion, zonas = None) :
        self._nombre = nombre
        self._ubicacion = ubicacion
        
        if (zonas == None):
            zonas = []
            
        self._zonas = zonas
        
    def agregarZonas(self, zona):
        self._zonas += [zona]
        
    def cantidadTotalAnimales(self):
        totalAnimales = 0
        
        for i in range(len(self._zonas)):
            totalAnimales += self._zonas[i].cantidadAnimales()
            
        return totalAnimales
    
    #Métodos Getters & Setters
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre;
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getUbicacion(self):
        return self._ubicacion;
    
    def setZona(self, zonas):
        self._zonas = zonas
        
    def getZona(self):
        return self._zonas