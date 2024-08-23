from sequences import ADN
key_limpias = []
secuencias_limpias = []

def eliminar_duplicados(secuencia):
    for elemento in secuencia:
        # Separamos el identificador de la secuencia
        identificador, sec = str(elemento).split(": ")

        # Si la key ya está en la lista, ignoramos esta secuencia
        if identificador in key_limpias:
            continue
            
        key_limpias.append(identificador)
        secuencias_limpias.append(elemento)
    return secuencias_limpias

def renombrar_duplicados(secuencia):
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


if __name__ == '__main__':
    secuencia = ["S1: ACTG", "S1: CCTT", "S2: ATTT", "S3: TAAA", "S4: GGGA", "S4: AGGG"]
    secuencia_recortada = eliminar_duplicados(secuencia)
    print(secuencia_recortada)
    secuencias_actualizadas = renombrar_duplicados(secuencia)
    print(secuencias_actualizadas)
