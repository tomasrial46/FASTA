class ADN:
    def __init__(self, id, secuencia):
        self.id=id
        self.secuencia=secuencia

    def __repr__(self):
        return "{}: {}".format(self.id,self.secuencia)

    def __str__(self):
        return "{}: {}".format(self.id,self.secuencia)
    
    #Esta función modifica la cadena de ADN ajustando a preferencia del usuario los saltos de linea y si las letras son
    #mayúsculas o minúsculas.

    def formatter(self, case=0, maxLength=0):
        
        if case == 1 or case=="1" or case=="upper":
            secuencia_formateada = self.secuencia.upper()
        elif case == 2 or case=="2" or case=="lower":
            secuencia_formateada = self.secuencia.lower()
        else:
            
            secuencia_formateada = self.secuencia

        maxLength= int(maxLength)
        if maxLength > 0:        
            fragmentos = [""]   #Pongo "" para que al empezar a poner las secuencias en función de maxLength la primera este en la siguiente linea y no al lado del id
            i = 0
            while i < len(secuencia_formateada):
                fragmentos.append(secuencia_formateada[i:i+maxLength])
                i += maxLength

            secuencia_formateada2 = "\n".join(fragmentos)
        else:
             secuencia_formateada2 = "\n{}".format(secuencia_formateada)
             

        return ADN(self.id, secuencia_formateada2)
        
#Esta función sirve para eliminar el último carácter de un string. Se usa en la función loadfile() para eliminar 
#el salto de línea al final de cada línea leída desde el archivo FASTA.

def eliminar(elemento):
    return elemento[:-1]

#La función loadfile lee linea por linea el fichero FASTA y crea una lista de listas con el identificador y la cadena,
#depués llama a la clase ADN para crear otra lista, pero esta vez, no hay listas dentro, sino objetos(el identificador y la cadena).

def loadfile(File):
    with open(File, "r") as file:
        lineas = file.readlines()
        lineas_final = list(map(eliminar, lineas))
        lineas_final[-1]=lineas[-1]
        n = 0
        for elemento in lineas_final:
            n+=elemento.count(">")
        lista_grande = []
        for i in range(n):
            lista_grande.append(list())

        i = 0
        primera_vez= True
        for elemento in lineas_final:
            if primera_vez:
                primera_vez = False    
            elif ">" in lista_grande[i][0] and ">" in elemento:
                i+=1
            lista_grande[i].append(elemento)

        for i in range(len(lista_grande)):
            lista_grande[i][1]="".join(lista_grande[i][1:])

        for i in range(len(lista_grande)):
            for j in range(len(lista_grande[i])-1, 0, -1):
                if j>1:
                    del lista_grande[i][j]
        lista_final=[]
        for i in range(len(lista_grande)):
            adn=ADN(lista_grande[i][0].replace(">","",1),lista_grande[i][1])                          
            lista_final.append(adn)

    return lista_final

def fasta_writer(ruta_archivo_salida,adns,case=0,maxLength=0):
    with open(ruta_archivo_salida, "w") as file:
        for adn in adns:
            adn_formateado = adn.formatter(case, maxLength)
            file.write(">{} {}\n".format(adn_formateado.id, adn_formateado.secuencia))
            


#En el apartado de código principal se especifícan las rutas de entrada y salida para el archivo sin formatear y
#formateado, se añaden a una lista las cadenas convertidas a objetos con su identificador correspondiente y después 
# se pasan por la función formatter una a una con un bucle for a la vez que son escritas en el fichero de salida.

if __name__  == "__main__":
    ruta_archivo = "test_data/test_3.fasta"
    ruta_archivo_salida = "fichero.txt"
    adns = loadfile(ruta_archivo)
    fasta_writer(ruta_archivo_salida,adns)
    
   

   

    
    

