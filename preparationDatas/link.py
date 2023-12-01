import requests
from bs4 import BeautifulSoup
import concurrent.futures
from constants import Constants

class Link:
    @staticmethod
    def titulo,modalidade,numero,ano,situacao,link_pdf(url_base):
        links_titulos = []

        # Loop para percorrer todas as páginas
        for i in range(0, 181, 15):
            # Constrói a URL com o parâmetro b_start
            url = f'{url_base}?b_start:int={i}'

            # Baixa a página
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encontra as células da tabela (td) que contêm links e títulos
            for td in soup.find_all('td'):
                # Procura por links dentro da célula
                link = td.find('a', href=True)
                if link:
                    href = link['href']
                    if '/editais/' in href and 'b_start:int=' not in href:
                        titulo = link.text.strip()
                        links_titulos.append({'titulo': titulo, 'link': href})

        return links_titulos
    
    @staticmethod
    def obter_detalhes_edital(link_edital):
        response_edital = requests.get(link_edital)
        soup_edital = BeautifulSoup(response_edital.text, 'html.parser')

        # Modifique as próximas linhas de acordo com a estrutura da página do edital
        modalidade_element = soup_edital.find('span', {'id': 'form-widgets-modalidade_edital'})
        numero_element = soup_edital.find('span', {'id': 'form-widgets-numero_edital'})
        ano_element = soup_edital.find('span', {'id': 'form-widgets-ano_edital'})
        situacao_element = soup_edital.find('span', {'id': 'form-widgets-situacao_edital'})
        link_pdf_element = soup_edital.find('a', {'class': 'state-missing-value contenttype-file'})

        # Verifica se os elementos foram encontrados antes de acessar os atributos
        modalidade = modalidade_element.text.strip() if modalidade_element else ''
        numero = numero_element.text.strip() if numero_element else ''
        ano = ano_element.text.strip() if ano_element else ''
        situacao = situacao_element.text.strip() if situacao_element else ''
        link_pdf = link_pdf_element['href'] if link_pdf_element else ''

        return {'modalidade': modalidade, 'numero': numero, 'ano': ano, 'situacao': situacao, 'link_pdf': link_pdf}

    @staticmethod
    def coletar_dados_e_persistir(resultado):
        print(f'Coletando dados para o edital {resultado["titulo"]}...')
        link_edital = resultado["link"]

        # Verifica se o link já contém "https://"
        if not link_edital.startswith("https://"):
            link_edital = f'{Constants.INITIAL_LINK}{link_edital}'

        # Coleta detalhes do edital em uma função assíncrona
        detalhes_edital = Link.obter_detalhes_edital(link_edital)

        # Combina informações do resultado e detalhes do edital
        dados_edital = {'titulo': resultado["titulo"], **detalhes_edital}

        return dados_edital
