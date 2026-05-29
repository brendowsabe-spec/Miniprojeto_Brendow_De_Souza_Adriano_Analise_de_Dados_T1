#Análise Exploratória da base Varejo
def linha(): #Feito função para criar linhas separados durante a analise
    print('-='*50)

import pandas as pd #Importando a biblioteca Pandas para análise dos dados do arquivo.csv
#Importando dados da Base_Varejo.csv do Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

df = pd.read_csv('Base_Varejo.csv',sep=';') #Importando csv base de dados com nome de data, utilizado "sep=';'" para determinar que o separador é ';' 

for n in range(1): #for para demonstrar o passo inicial da manipulação
    linha()
    print(f"OS 10 PRIMEIROS REGISTROS DE NOSSA BASE DE DADOS:\n\n{df.head(10)}") #para mostrar na tela apenas os 10 primeiros dados
    linha()

print(f'O dataset original possui {df.shape[0]} registros(linhas) e {df.shape[1]} colunas.') #número de registros #numero de colunas
linha()
print('Nome de todas as colunas:', end=' ')
for i in list(df.columns): #Demonstra todas as colunas
    print(i, end='. ') #Titulo de cada coluna
print()
linha()
#Contagem de todas as linhas #contagem de todas as colunas - #print(f'A Base_Varejo.csv tem inicialmente: {len(df.columns)} colunas e {len(df.index)} linhas.')
#print(df.shape) #Mostra numero de linhas(index) e colunas(columns) #print(df.fillna(0, inplace=True))) #troca o NaN por 0
print(2)
df.info() # informações de itens por cada titulo-coluna, tipos de dados.
linha()
print(4)
print(df.describe()) #Descreve quartis, estatiscas gerais matematicas do DataFrame
linha()
print(df.isnull().sum()) #Soma os locais que estão sem dados (NaN)
linha()
print(df.isnull()) #mostra como True os espaços sem dados (NaN)
linha()
Masculino = df[df['CL_GENERO'] == 'M'] #feito para manter apenas os que aparecem M (sendo masculino)
print(Masculino)
linha()
print(df.dtypes) #Mostra os tipos de dados de cada coluna
linha()
print(df.duplicated().sum()) #soma das linhas repetidas
linha()
#df.dropna() #remove linha que tenha 1 nulo (cuidado)
#df.dropna(how='all') #remove só onde todas colunas sao nula
#df.dropna(subset=['email']) #remove apenas onde 'email' é nula
#df.dropna(thresh=5) #mantem linhas que tem pelo menos 5 valores nao nulos.
print(df.dropna(axis=1, how='all')) #remove colunas que estejam com nulos NaN (axis=1 é coluna, how='all' é todas que contenham NaN)
print(len(df))
df_limpo = df.dropna(axis=1, how='all')
print(len(df))
print(df_limpo.head(10))

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



