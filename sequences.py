class ADN:
    def __init__(self, id, secuencia):
        self.id=id
        self.secuencia=secuencia

    def __repr__(self):
        return "{}: {}".format(self.id,self.secuencia)

    def __str__(self):
        return "{}: {}".format(self.id,self.secuencia)
    
