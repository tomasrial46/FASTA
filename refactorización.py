from sequences import ADN
from abc import ABC, abstractmethod
from fasta import *

class AbstractTransformer(ABC):
    @abstractmethod
    def transform(self, secuencia):
        pass

class DuplicatedIdentifiersRenamer(AbstractTransformer):
    def transform(self, secuencia):
        titulos = {}
        nuevas_cadenas = []
        
        for cadena in secuencia:
            titulo, sec = str(cadena).split(": ")
            if titulo in titulos:
                titulos[titulo] += 1
                nuevo_titulo = f"{titulo}.{titulos[titulo]}"
            else:
                titulos[titulo] = 1
                nuevo_titulo = titulo
            nuevas_cadenas.append(ADN(nuevo_titulo, sec))  # Crear objeto ADN directamente

        titulos_repetidos = set(titulo for titulo in titulos if titulos[titulo] > 1)
        titulos_actualizados = {}

        for i, cadena in enumerate(nuevas_cadenas):
            titulo, sec = cadena.id, cadena.secuencia
            if titulo in titulos_repetidos:
                if titulo not in titulos_actualizados:
                    titulos_actualizados[titulo] = 1
                else:
                    titulos_actualizados[titulo] += 1
                nuevo_titulo = f"{titulo}.{titulos_actualizados[titulo]}"
                nuevas_cadenas[i].id = nuevo_titulo

        return nuevas_cadenas


class DuplicatedIdentifiersRemover(AbstractTransformer):
    def transform(self, secuencia):
        key_limpias = []
        secuencias_limpias = []
        for elemento in secuencia:
            # Separamos el identificador de la secuencia
            identificador, sec = str(elemento).split(": ")

            # Si la key ya está en la lista, ignoramos esta secuencia
            if identificador in key_limpias:
                continue
                
            key_limpias.append(identificador)
            secuencias_limpias.append(elemento)
        return secuencias_limpias


class Reverse(AbstractTransformer):
    def transform(self, secuencia):
        new_self = []
        for adn in secuencia:
            inverted_adn = ADN(adn.id, adn.secuencia[::-1])
            new_self.append(inverted_adn)
        return new_self

class Complement(AbstractTransformer):
    def transform(self, secuencia):
        new_self = []
        for adn in secuencia:
            secuencia = adn.secuencia
            nueva_secuencia = ""
            for base in secuencia:
                if base == 'A':
                    nueva_secuencia += 'T'
                elif base == 'T':
                    nueva_secuencia += 'A'
                elif base == 'C':
                    nueva_secuencia += 'G'
                elif base == 'G':
                    nueva_secuencia += 'C'
            complemented_adn = ADN(adn.id, nueva_secuencia)
            new_self.append(complemented_adn)
        return new_self


class SequenceListTransformer:
    def __init__(self, secuencia, transformers):
        self.secuencia = secuencia
        self.transformers = transformers

    def transform(self):
        transformed_sequences = self.secuencia
        for transformer in self.transformers:
            transformed_sequences = transformer.transform(transformed_sequences)
        return transformed_sequences
    

if __name__ == "__main__":
    ruta_archivo = "test_data/test_3.fasta"
    adns = loadfile(ruta_archivo)
    resultado = DuplicatedIdentifiersRenamer()
    print(resultado.transform(adns))
    resultado = DuplicatedIdentifiersRemover()
    print(resultado.transform(adns))
    resultado = Complement()
    print(resultado.transform(adns))
    resultado = Reverse()
    print(resultado.transform(adns))
    transformadores = [Complement(), Reverse(), DuplicatedIdentifiersRemover(), DuplicatedIdentifiersRenamer()]
    transformador = SequenceListTransformer(adns, transformadores)

    resultado = transformador.transform()
    print(resultado)