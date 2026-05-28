#Análise Exploratória da base Varejo

#Importando a biblioteca Pandas para análise dos dados do arquivo.csv
import pandas as pd
#importando dados da Base_Varejo.csv do Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data
pd.read_csv('Base_Varejo.csv')

print(pd.read_csv('Base_Varejo.csv'))

#Carregar a base Varejo.csv com pandas e mostrar:
#número de registros


#colunas


#tipos de dados


#dois problemas básicos: valores nulos por coluna, duplicatas e possíveis inconsistências (ex.: datas inválidas ou categorias vazias)

#três etapas de limpeza mínima necessária: remover ou imputar nulos (explique a escolha), eliminar duplicatas relevantes e ajustar tipos de dados (ex.: converter coluna DATA para datetime)

# Gerar estatísticas descritivas básicas para coluna de número de filhos do cliente (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem, quartis)

# Explorar padrões de agrupamento com pelo menos dois agrupamentos (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().

# Produzir um pequeno bloco de conclusões (3–6 tópicos) com os principais insights obtidos e possíveis problemas remanescentes na base. Notebook Python, MD ou um “print”


# 01 - (Transformação de Strings, Integer e Float e Datetime): Desenvolvimento das funções de limpeza de texto, inteiros e decimais usando métodos e expressões regulares.
# 02 - (Limpeza de Nulos e Duplicatas): Aplicação das condicionais e funções  para identificação e substituição de valores vazios e  de str para valores de data tipo datetime, na tabela de varejo. 
# 03 - (Estatística Descritiva): Aplicação das funções estatísticas para coletar parâmetros da coluna de Número de filhos do cliente.
# 04 - (Relatório e Documentação): Construção dos contadores do relatório final exibido no terminal, finalização do README.md com a reflexão teórica e submissão do link no AVA.


# Versionamento 01 - Entregou o repositório no GitHub contendo os arquivos organizados e um README.md explicativo com a reflexão teórica obrigatória sobre ETL e qualidade de dados.
# Documentação 02 - Desenvolveu Arquivo README.md contendo de 3-6 tópicos com insights obtidos da análise dos dados.
# Manipulação de Arquivos CSV 03 - Realizou a leitura e extração dos arquivos de dados de forma estruturada e nativa (csv.DictReader).
# Tratamento de Nulos e Condicionais 04 - # Implementou a lógica (if/else) para preencher categorias vazias com "Sem Categoria" e tratou corretamente os nulos das dimensões físicas, justificando a escolha.
# Regras de Negócio e Datas 05 - Validou a regra do identificador de número de compra, e converteu com sucesso a string de data da compra utilizando o módulo datetime.
# Padrões de Agrupamento 06 - Explorou padrões de agrupamento com pelo menos duas combinações.
# Geração de Estatísticas Básicas 07 - Gerou as estatísticas básicas de acordo com a coluna Número de filhos dos clientes, contemplando todos os parâmetros elencados



