import csv
from fasta import *

class SequenceStats:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_length(self):
        return len(self.sequence)

    def count_letters(self):
        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0, '-': 0}
        for letter in self.sequence:
            if letter in counts:
                counts[letter] += 1
        return counts


class SequenceStatsMatrix:
    def __init__(self, sequences):
        self.sequences = sequences
        self.stats_matrix = []

    def generate_stats_matrix(self):
        header = ['id', 'len', 'A', 'C', 'T', 'G', '-']
        self.stats_matrix.append(header)

        for sequence_id, sequence in self.sequences:
            stats = SequenceStats(sequence)
            length = stats.get_length()
            letter_counts = stats.count_letters()
            row = [sequence_id, length, letter_counts['A'], letter_counts['C'], letter_counts['T'], letter_counts['G'], letter_counts['-']]
            self.stats_matrix.append(row)

    def save_as_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.stats_matrix)


def fasta_summary(input_file, output_file):
    sequences = loadfile(input_file)
    stats_matrix = SequenceStatsMatrix(sequences)
    stats_matrix.generate_stats_matrix()
    stats_matrix.save_as_csv(output_file)



if __name__ == "__main__":
    ruta_archivo = "test_data/test_1.fasta"
    adns = loadfile(ruta_archivo)


    # Obtener estadísticas de una sola secuencia
    secuencia = adns[0].secuencia  # Obtener la secuencia de interés
    stats = SequenceStats(secuencia)
    length = stats.get_length()
    letter_counts = stats.count_letters()
    print("Longitud:", length)
    print("Recuento de letras:", letter_counts)

    # Obtener matriz de estadísticas de varias secuencias
    sequences = [(adn.id, adn.secuencia) for adn in adns]  # Convertir la lista de ADN a una lista de tuplas (id, secuencia)
    stats_matrix = SequenceStatsMatrix(sequences)
    stats_matrix.generate_stats_matrix()
    matrix = stats_matrix.stats_matrix
    for row in matrix:
        print(row)

    ruta_archivo_salida = "matriz.csv"
    stats_matrix.save_as_csv(ruta_archivo_salida)