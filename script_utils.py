from fasta import *
from transformations import *


def apply_transformation(input_file, output_file, transformation):
    load = loadfile(input_file)

    if transformation == 'invertida':
        load = invertida(load)
    elif transformation == 'complementaria':
        load = complementaria(load)
    elif transformation == 'ambas':
        load = invertida(load)
        load = complementaria(load)
    elif transformation == 'rename':
        load=renombrar_duplicados(load)
    elif transformation == 'remove':
        load=eliminar_duplicados(load)

    else:
        print("Usted se ha equivocado en la expresión de trans")
        return

    fasta_writer(output_file, load)