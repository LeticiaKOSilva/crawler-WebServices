from link import Link
from constants import Constants
from file_csv import File_CSV
import concurrent.futures

def initial() :
    # Obtém os links e títulos
    resultados = Link.obter_links_e_titulos(Constants.URL_INITIAL)

    # Coleta detalhes e persiste em CSV de forma paralela
    with concurrent.futures.ThreadPoolExecutor() as executor:
        dados_coletados = list(executor.map(Link.coletar_dados_e_persistir, resultados))

    # Persiste os dados em CSV
    File_CSV.persistir_em_csv(dados_coletados)

    print('Coleta e persistência concluídas.')

'''
i=0
Imprime os resultados
for resultado in resultados:
    i = i + 1
    print(i)
    print(f'Título: {resultado["titulo"]}')
    print(f'Link: {resultado["link"]}')
    print('-' * 50)
'''

initial()