import argparse
import csv
import time

def carregar_dados_csv(nome_arquivo='preparationDatas/dados_editais.csv'):
    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        dados = list(reader)
    return dados

def aplicar_filtros(resultado, filtros):
    for chave, valor in filtros.items():
        if valor and chave in resultado:
            if chave == "ano":
                # Formatação especial para o filtro "ano"
                if valor.isdigit() and len(valor) == 4:
                    valor = f"{int(valor):,}".replace(",", ".")
                else:
                    # Ignora valores não numéricos ou com mais de 4 dígitos
                    continue
            
            if valor.lower() not in resultado[chave].lower():
                return False
    return True

def buscar_editais(dados, termo_busca, **kwargs):
    # Aplica filtros com base nos argumentos
    resultados_filtrados = dados

    if termo_busca:
        resultados_filtrados = [resultado for resultado in resultados_filtrados if termo_busca.lower() in resultado["titulo"].lower()]

    resultados_filtrados = [resultado for resultado in resultados_filtrados if aplicar_filtros(resultado, kwargs)]

    return resultados_filtrados

def formatar_saida(resultados, termo_busca, filtros, tempo_resposta):
    print(f'Termo de busca: "{termo_busca}"')
    print('Filtros:')
    for chave, valor in filtros.items():
        if not valor == None:
            print(f'  {chave.capitalize()}: {valor}')

    print(f'\nTempo de resposta: {tempo_resposta}')
    print(f'\nResultados: {len(resultados)}\n------------')

    for resultado in resultados:
        print(f'\n{resultado["titulo"]}')
        print(f'Link: {resultado["link_pdf"]}')

if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="Buscar editais")
    parser.add_argument("termo_busca", type=str, help="Termo de busca")
    parser.add_argument("-modalidade", type=str, help="Modalidade")
    parser.add_argument("-numero", type=str, help="Número")
    parser.add_argument("-ano", type=str, help="Ano")
    parser.add_argument("-situacao", type=str, help="Situação")
    args = parser.parse_args()

    # Cria um dicionário com os filtros fornecidos
    filtros = {"modalidade": args.modalidade, "numero": args.numero, "ano": args.ano, "situacao": args.situacao}

    dados = carregar_dados_csv()
    resultados = buscar_editais(dados, args.termo_busca, **filtros)

    tempo_resposta = f"{(time.time() - start_time) * 1000:.0f}ms"
    formatar_saida(resultados, args.termo_busca, filtros, tempo_resposta)
