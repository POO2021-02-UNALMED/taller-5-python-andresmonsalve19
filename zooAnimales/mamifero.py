from zooAnimales.animal import Animal 

class Mamifero(Animal):
    
    _listado = []
    caballos =0
    leones = 0
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        Animal.__init__(self, nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        
    @classmethod   
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls._listado.append(caballo)
        cls.caballos += 1
        return caballo
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls._listado.append(leon)
        cls.leones += 1
        return leon
    
    #Métodos Getters & Setters
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    
    @classmethod    
    def getListado(cls):
        return cls._listado
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
        
    def isPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
        
    def getPatas(self):
        return self._patas
        
    