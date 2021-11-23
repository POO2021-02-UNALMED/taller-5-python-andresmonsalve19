from zooAnimales.animal import Animal 

class Ave(Animal):
    
    _listado = []
    halcones =0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        Animal.__init__(self, nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        
    @classmethod   
    def cantidadAves(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._listado.append(halcon)
        cls.halcones += 1
        return halcon
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._listado.append(aguila)
        cls.aguilas += 1
        return aguila
    
    #Métodos Getters & Setters
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    
    @classmethod    
    def getListado(cls):
        return cls._listado
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
        
    def getColorPlumas(self):
        return self._colorPlumas
        
    