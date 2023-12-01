# crawler-WebServices
Sistema de busca para a página de editais do Campus Barbacena: https://www.ifsudestemg.edu.br/editais/editais-de-barbacena

## Proposta da Atividade
<p> Atividade proposta na matéria de webServices tem por objetivo criar um código que pega todos os editais do IFET através do link https://www.ifsudestemg.edu.br/editais/editais-de-barbacena .</p>
<p>Depois de pegar todos os editais será extraído informações específicas de 
cada um e armazenados em um arquivo .csv.<br>Depois se criará um código de buscar esses editais de diversas formas diferentes.</p>
<p>A linguagem escolhida para desenvolver essa atividade foi o Python</p>
<p>Nos dois títulos abaixo será apresentado o passo a passo para a realização da atividade</p>

## Extrair Editais e persistir em arquivo .csv
- Criação do arquivo crawler que é responsável por todas as operações referentes aa extração de links e persistencia do arquivo.
- Extrair o link e o título de todos os editais do link : https://www.ifsudestemg.edu.br/editais/editais-de-barbacena.
    - No arquivo link criei um método static chamado <b>"obter_links_e_titulos"</b> que recebe o link acima e faz a busca pegando os link e titulo de todos os resultados retornando eles para o método initial.
- Em seguida com o auxílio da biblioteca concurrent.futures( presente na versão 3.12 do python que ajuda na execução assíncrona utilizando ThreadPoolExecutor para threads e  ProcessPoolExecutor para processos) chamaremos o método static <b>"coletar_dados_e_persistir"</b> que recebe a lista com todo o link e título dos editais coletados e agora irá acessar cada um dos links e pegar as seguintes informações de cada edital:
    - Título;
    - Modalidade;
    - Número;
    - Ano;
    - Situação;
    - Link direto para o PDF.
- Em seguida com os dados retornados do método acima em um dicionário, invocaremos o método static <b>"persistir_em_csv"</b> que vai receber os dados e o nome do arquivo e assim armazenar os dados nesse arquivo .csv.

##  busca (em modo texto)
- Criaçaõ de um arquivo chamado search_edital.py que irá realizar toda a busca em modo texto realizado pelo usuário;
- Primeiro será feita a manipulação das informações que o usuário poderá pesquisar, que são:
  - Termo de busca: a ser pesquisado nos títulos;
  - Filtro de modalidade;
  - Filtro de número;
  - Filtro de ano;
  - Filtro de situação.
- Por fim faremos algumas alterações para que a entrada e saída de dados seja como no exemplo abaixo:
  - <b>ENTRADA</b><br>
      #Busca editais com o termo "informática"<br>
      python3 busca_edital.py informática
  - <b>SAÍDA</b><br>
      Termo de busca: "informática"<br>
      Filtros:<br>
          ano: 2021<br>
          modalidade: extensão<br>
          Tempo de resposta: 400ms

        2 resultados
        ------------
            Edital 54/2023: Edital de chamada para submissão de resumos para a Semana Acadêmica do Curso de Licenciatura em Educação Física do IF Sudeste MG - Campus Barbacena
            Link: https://www.ifsudestemg.edu.br/editais/barbacena/ensino/edital-54-2023-edital-de-chamada-para-submissao-de-resumos-para-a-semana-academica-do-curso-de-licenciatura-em-             educacao-fisica-do-if-sudeste-mg-campus-barbacena/edital-54.pdf

            2023/52: 1° Festival de Música do IF Sudeste MG – IFestival 2023
            Link: https://www.ifsudestemg.edu.br/editais/barbacena/extensao/2023/edital-ndeg-52-1deg-festival-de-musica-do-if-sudeste-mg-2013-ifestival-2023/edital-inscricoes-                        ifestival.pdf



 

