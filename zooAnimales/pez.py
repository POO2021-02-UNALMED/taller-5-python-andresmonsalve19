from zooAnimales.animal import Animal 

class Pez(Animal):
    
    _listado = []
    salmones =0
    bacalaos = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        Animal.__init__(self, nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        
    @classmethod   
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls._listado.append(salmon)
        cls.salmones += 1
        return salmon
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls._listado.append(bacalao)
        cls.bacalaos += 1
        return bacalao
    
    #Métodos Getters & Setters
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    
    @classmethod    
    def getListado(cls):
        return cls._listado
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
        
    def getCantidadAletas(self):
        return self._cantidadAletas
        
    