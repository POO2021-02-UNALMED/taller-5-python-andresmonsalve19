class Zona:
    
    def __init__(self, nombre, zoo = None, animales = None):
        self._nombre = nombre
        self._zoo = zoo
        
        if (animales == None):
            animales = []
            
        self._animales = animales
        
    def agregarAnimales(self, animal):
        self._animales += [animal]
        
    def  cantidadAnimales(self):
        return len(self._animales)
    
    #Métodos Getters & Setters
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre
    
    def setZoo(self, zoo):
        self._zoo = zoo
        
    def getZoo(self):
        return self._zoo
    
    def setAnimales(self, animales):
        self._animales = animales
        
    def getAnimales(self):
        return self._animales