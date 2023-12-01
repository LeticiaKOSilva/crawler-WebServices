import csv
from constants import Constants

class File_CSV:
    @staticmethod
    def persistir_em_csv(dados, arquivo_csv=Constants.FILE_NAME):
        with open(arquivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
            # Especifica as colunas do CSV
            colunas = ['titulo', 'modalidade', 'numero', 'ano', 'situacao', 'link_pdf']
            writer = csv.DictWriter(csvfile, fieldnames=colunas)

            # Escreve o cabeçalho
            writer.writeheader()

            # Escreve os dados
            writer.writerows(dados)
