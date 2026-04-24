# 🔥 Análise de Focos de Incêndio em Minas Gerais e Brasil

Este repositório apresenta um projeto de análise de dados sobre focos de incêndio no Brasil, com foco principal no estado de **Minas Gerais**, seus municípios, biomas e unidades de conservação ambiental.

Foram utilizados dados do **INPE** e da **Fundação Chico Mendes** para a análise dos dados de incêndio em Minas Gerais entre os anos de **2015 e 2025**, além de dados relacionados às reservas ambientais do estado.

O objetivo do projeto é transformar dados brutos sobre focos de incêndio em **informações visuais, indicadores analíticos e insights relevantes**, permitindo compreender melhor a evolução dos incêndios ao longo dos anos, os períodos de maior ocorrência, as regiões mais afetadas e os impactos em áreas ambientais protegidas.

---

## 📌 Objetivo do Projeto

O projeto tem como objetivo principal analisar a incidência de focos de incêndio no estado de Minas Gerais, observando:

- A evolução anual dos focos de incêndio;
- A variação percentual anual dos focos;
- Os meses com maior ocorrência;
- Os biomas mais afetados;
- O posicionamento de Minas Gerais no ranking nacional;
- Os municípios mineiros com maior incidência;
- A distribuição espacial dos focos por meio de mapas;
- O impacto dos incêndios em áreas de conservação ambiental.

Além disso, o projeto busca apresentar essas informações de forma visual e acessível, utilizando gráficos, mapas e dashboards.

---

## 🧠 Principais Perguntas Respondidas

Durante a análise, o projeto buscou responder perguntas como:

- Em quais anos Minas Gerais teve mais focos de incêndio?
- Qual foi o ano com menor incidência?
- O número de focos está aumentando ou diminuindo ao longo do tempo?
- Quais meses concentram mais registros?
- Qual estação do ano apresenta maior risco?
- Qual bioma foi mais afetado?
- Minas Gerais está entre os estados mais afetados do Brasil?
- Quais municípios mineiros concentram mais focos?
- Como os incêndios se distribuem espacialmente no estado?
- Quais unidades de conservação foram mais impactadas pelo fogo?

---

## 📊 Análises Realizadas

### 1. Número de focos de incêndio por ano em Minas Gerais

Foi realizada uma análise temporal considerando o número de focos de incêndio registrados em Minas Gerais no período de **2015 a 2025**.

Essa análise permite entender a variação anual dos incêndios no estado e identificar anos críticos.

#### Principais resultados

- **Maior registro:** 2021, com **12.110 focos registrados**.
- **Menor registro:** 2018, com **4.627 focos registrados**.

Essa visualização ajuda a identificar períodos de maior intensidade e possíveis padrões de crescimento ou redução dos focos ao longo dos anos.

---

### 2. Taxa de Variação Anual dos Focos de Incêndio

Para complementar a análise, foi criado um indicador chamado **Taxa de Variação Anual dos Focos de Incêndio**.

Esse indicador permite observar se houve aumento ou redução no número de focos em relação ao ano anterior.

A fórmula utilizada foi:

```text
Taxa = ((F_atual - F_anterior) / F_anterior) * 100
```

Onde:

```text
F_atual = número de focos no ano atual
F_anterior = número de focos no ano anterior
```

A interpretação da taxa é feita da seguinte forma:

```text
Valor positivo  → aumento no número de focos de incêndio
Valor negativo  → redução no número de focos de incêndio
Valor próximo de zero → estabilidade
```

Esse indicador foi definido como um dos principais elementos analíticos do projeto, pois permite analisar não apenas o volume absoluto de incêndios, mas também a tendência de crescimento ou queda ao longo dos anos.

---

### 3. Bioma mais afetado em Minas Gerais

Também foi realizada uma análise dos focos de incêndio por bioma dentro do estado de Minas Gerais.

Essa etapa permite identificar quais formações naturais sofreram maior impacto ao longo do período analisado.

A análise é importante porque diferentes biomas apresentam diferentes níveis de vulnerabilidade ao fogo, além de características ambientais e climáticas próprias.

---

### 4. Ranking dos estados mais afetados no Brasil

O projeto também compara Minas Gerais com outros estados brasileiros, por meio de um ranking dos estados com maior número de focos de incêndio entre **2015 e 2025**.

#### Principal insight

Minas Gerais aparece como o **9º estado mais afetado do Brasil** no período analisado.

Essa informação permite compreender a gravidade da situação do estado em escala nacional.

---

### 5. Número de focos de incêndio por mês

Foi realizada uma análise mensal dos focos de incêndio, agrupando os registros pelos meses do ano.

Essa análise permite identificar em quais períodos do ano os incêndios são mais frequentes.

#### Principal insight

O mês com maior ocorrência de focos de incêndio em Minas Gerais foi **setembro**.

Além disso, a maior parte dos focos ocorreu durante o **inverno**, período mais seco do ano no estado.

Esse resultado reforça a influência das condições climáticas, como baixa umidade e estiagem, no aumento da ocorrência de incêndios.

---

### 6. Mapa de calor dos focos de incêndio

O projeto inclui mapas de calor para visualizar as regiões mais afetadas por incêndios no estado de Minas Gerais.

Esse tipo de visualização facilita a identificação de áreas com maior concentração de registros e auxilia na interpretação espacial do fenômeno.

Os mapas ajudam a responder perguntas como:

- Onde os focos estão mais concentrados?
- Existem regiões recorrentes de maior risco?
- Os focos se concentram em áreas urbanas, rurais ou ambientais?
- Há relação com biomas ou regiões específicas?

---

## 🏙️ Análises por Município

Além da análise estadual, o projeto também realiza análises específicas para municípios de Minas Gerais.

Foram aplicadas análises semelhantes às realizadas para o estado como um todo, permitindo observar o comportamento dos focos em escala municipal.

---

### 1. Ranking dos municípios mais afetados

Foi criado um ranking dos municípios mineiros com maior incidência de focos de incêndio.

Essa análise permite identificar quais cidades concentram os maiores volumes de registros e quais regiões demandam maior atenção.

---

### 2. Taxa de variação anual por município

Também foi calculada a taxa de variação anual dos focos de incêndio para os municípios.

Com isso, é possível observar se determinado município apresentou crescimento, queda ou estabilidade no número de focos ao longo dos anos.

Essa análise pode ser aplicada a qualquer município presente na base de dados.

---

### 3. Análise das maiores cidades de Minas Gerais

Foi dada atenção especial às 10 cidades mais populosas de Minas Gerais:

- Belo Horizonte;
- Uberlândia;
- Contagem;
- Juiz de Fora;
- Montes Claros;
- Betim;
- Uberaba;
- Ribeirão das Neves;
- Governador Valadares;
- Divinópolis.

Essa seleção permite observar como os focos de incêndio se comportam em municípios de grande relevância populacional e econômica.

---

### 4. Distribuição mensal por município

Para cada município, também foi feita uma análise da distribuição dos focos ao longo dos meses do ano.

Essa análise permite identificar se o padrão estadual, com maior ocorrência no período seco, também se repete em escala municipal.

---

### 5. Mapa interativo por município

O projeto também conta com mapas interativos que exibem os focos de incêndio do último ano disponível para cada município.

Esses mapas permitem uma visualização mais detalhada da distribuição geográfica dos registros.

---

## 🌱 Análises de Unidades de Conservação Ambiental

O projeto também contempla uma análise específica sobre áreas de conservação ambiental em Minas Gerais.

O objetivo dessa etapa foi avaliar o impacto dos incêndios em unidades de conservação e identificar quais áreas protegidas foram mais afetadas.

---

### Unidades de conservação consideradas

Foram consideradas unidades como:

- APA Cavernas do Peruaçu;
- APA da Serra da Mantiqueira;
- APA Morro da Pedreira;
- PARNA da Serra da Canastra;
- PARNA da Serra do Cipó;
- PARNA da Serra do Gandarela;
- PARNA das Sempre-Vivas;
- PARNA de Itatiaia;
- PARNA Grande Sertão Veredas;
- RDS Nascentes Geraizeiras;
- REBIO da Mata Escura.

---

### Área de conservação ambiental afetada

Foi analisada a área afetada pelo fogo em hectares ao longo dos anos.

#### Principais resultados

- **Maior registro:** 2020, com **94.372,1 hectares afetados**.
- **Menor registro:** 2021, com **30.681,74 hectares afetados**.

Essa análise mostra que, mesmo quando o número de focos varia, o impacto ambiental pode ser avaliado também pela extensão territorial atingida.

---

### Porcentagem média de área afetada

Também foi analisada a porcentagem média de área queimada por unidade de conservação entre **2015 e 2025**.

Essa métrica permite comparar unidades de tamanhos diferentes de forma mais justa, observando proporcionalmente quais áreas sofreram maior impacto.

---

## 🖼️ Exemplos de Visualizações

As imagens geradas pelo projeto podem ser encontradas na pasta `assets`.

> Caso algum nome de imagem esteja diferente no repositório, basta ajustar o caminho correspondente.

### Focos por ano em Minas Gerais

```md
![Focos por ano em Minas Gerais](assets/focosAnoMG.png)
```

Esse gráfico mostra a evolução anual dos focos de incêndio no estado entre 2015 e 2025.

---

### Biomas mais afetados

```md
![Focos por bioma](assets/fireBiomas.png)
```

Esse gráfico apresenta a distribuição dos focos de incêndio entre os biomas presentes em Minas Gerais.

---

### Taxa de variação anual

```md
![Taxa de variação anual](assets/taxaVariacaoAnual.png)
```

Esse gráfico mostra o crescimento ou queda percentual dos focos de incêndio em relação aos anos anteriores.

---

### Ranking nacional dos estados mais afetados

```md
![Ranking dos estados mais afetados](assets/rankingEstados.png)
```

Essa visualização compara Minas Gerais com outros estados brasileiros no número de focos registrados.

---

### Focos por mês

```md
![Focos por mês](assets/focosMeses.png)
```

Esse gráfico mostra os meses com maior concentração de focos de incêndio.

---

### Mapa de calor

```md
![Mapa de calor dos focos](assets/heatMap.png)
```

O mapa de calor permite visualizar espacialmente as regiões mais afetadas em Minas Gerais.

---

### Unidades de conservação

```md
![Áreas de conservação afetadas](assets/areasConservacao.png)
```

Esse gráfico apresenta o impacto dos incêndios em áreas de conservação ambiental.

---

## 🛠️ Tecnologias Utilizadas

O projeto utiliza ferramentas de análise de dados, visualização e desenvolvimento de dashboards.

### Linguagem principal

- **Python**

### Bibliotecas utilizadas

- **Pandas**  
  Utilizado para leitura, limpeza, filtragem, agrupamento e transformação dos dados.

- **NumPy**  
  Utilizado para operações numéricas auxiliares.

- **Matplotlib**  
  Utilizado para construção de gráficos estáticos.

- **Folium**  
  Utilizado para criação de mapas interativos e mapas de calor.

- **Streamlit**  
  Utilizado para criação de dashboards interativos.

- **Supabase**  
  Utilizado como banco de dados/backend para disponibilização e consulta dos dados.

- **PostgreSQL**  
  Banco relacional utilizado para armazenamento estruturado dos dados.

- **Python-dotenv**  
  Utilizado para carregar variáveis de ambiente a partir do arquivo `.env`.

---

## 📁 Estrutura Recomendada do Projeto

A estrutura do projeto pode seguir o seguinte padrão:

```text
analiseIncendioBR/
│
├── assets/
│   ├── focosAnoMG.png
│   ├── fireBiomas.png
│   ├── taxaVariacaoAnual.png
│   ├── rankingEstados.png
│   ├── focosMeses.png
│   ├── heatMap.png
│   └── areasConservacao.png
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboards/
│   └── app.py
│
├── maps/
│   └── heatMap.html
│
├── notebooks/
│   └── analises.ipynb
│
├── src/
│   ├── database.py
│   ├── processamento.py
│   ├── graficos.py
│   └── mapas.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Como Utilizar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/jvrezendem/analiseIncendioBR.git
```

Depois, entre na pasta do projeto:

```bash
cd analiseIncendioBR
```

---

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não exista, ele pode ser criado com dependências semelhantes a estas:

```txt
pandas
numpy
matplotlib
folium
streamlit
python-dotenv
supabase
psycopg2-binary
```

---

### 4. Configurar variáveis de ambiente

O projeto utiliza variáveis de ambiente para conexão com banco de dados e Supabase.

Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env.example`.

Exemplo:

```env
DATABASE_URL="postgresql://usuario:senha@localhost:5432/nome_do_banco"
SUPABASE_URL="https://sua-url-do-supabase.supabase.co"
SUPABASE_KEY="sua-chave-publica-ou-anon-key"
```

> Importante: o arquivo `.env` não deve ser enviado para o GitHub. Ele deve estar listado no `.gitignore`.

---

### 5. Visualizar notebooks e mapas

As visualizações podem ser acessadas na pasta:

```text
notebooks/
```

Os mapas interativos podem ser acessados na pasta:

```text
maps/
```

---

### 6. Executar o dashboard

Caso o projeto utilize Streamlit, execute:

```bash
streamlit run dashboards/app.py
```

Ou, se o arquivo principal estiver na raiz:

```bash
streamlit run app.py
```

---

## 🗃️ Dados Utilizados

O projeto trabalha com dados de focos de incêndio no Brasil, filtrando e analisando principalmente registros relacionados ao estado de Minas Gerais.

Os dados foram tratados para permitir análises por:

- Ano;
- Mês;
- Estado;
- Município;
- Bioma;
- Latitude e longitude;
- Unidade de conservação;
- Área afetada.

---

## 🔄 Etapas do Processamento

O fluxo geral do projeto segue as seguintes etapas:

```text
1. Coleta ou importação dos dados
2. Leitura dos arquivos CSV
3. Limpeza dos dados
4. Padronização de colunas
5. Filtro para Minas Gerais
6. Agrupamento por ano, mês, município e bioma
7. Cálculo de indicadores
8. Geração de gráficos
9. Geração de mapas
10. Construção do dashboard
```

---

## 📈 Indicadores Produzidos

O principal indicador criado no projeto foi a **Taxa de Variação Anual dos Focos de Incêndio**.

Além dele, também foram produzidos indicadores como:

- Total de focos por ano;
- Total de focos por mês;
- Total de focos por bioma;
- Ranking de estados mais afetados;
- Ranking de municípios mais afetados;
- Área ambiental afetada por ano;
- Porcentagem média de área queimada por unidade de conservação.

---

## 🔍 Principais Insights Produzidos

### Minas Gerais teve seu maior pico de focos em 2021

O ano de 2021 apresentou o maior número de focos registrados no período analisado, com **12.110 focos**.

---

### 2018 foi o ano com menor número de focos

O menor registro ocorreu em 2018, com **4.627 focos**.

---

### Setembro foi o mês mais crítico

O mês com maior número de focos foi setembro, indicando forte relação com o período seco.

---

### O inverno concentrou grande parte dos focos

A maioria dos focos ocorreu durante o inverno, estação marcada por baixa umidade, menor volume de chuvas e maior risco de queimadas.

---

### Minas Gerais aparece entre os 10 estados mais afetados

No ranking nacional, Minas Gerais aparece como o **9º estado mais afetado** por focos de incêndio entre 2015 e 2025.

---

### Unidades de conservação sofreram impactos relevantes

A análise das áreas protegidas mostrou que os incêndios também atingiram unidades de conservação ambiental, com destaque para o ano de 2020, que apresentou a maior área afetada.

---

## 🧭 Possíveis Aplicações

Este projeto pode ser utilizado para:

- Estudos ambientais;
- Monitoramento de queimadas;
- Apoio a políticas públicas;
- Planejamento de prevenção a incêndios;
- Educação ambiental;
- Visualização de dados geográficos;
- Construção de dashboards analíticos;
- Estudos acadêmicos sobre clima, vegetação e queimadas.

---

## 🚀 Melhorias Futuras

Algumas melhorias possíveis para o projeto:

- Adicionar filtros interativos por ano, município e bioma;
- Criar um dashboard online mais completo;
- Integrar dados climáticos, como chuva, temperatura e umidade;
- Adicionar modelos preditivos para estimar risco de incêndio;
- Criar alertas automáticos para regiões críticas;
- Melhorar os mapas interativos;
- Adicionar análise por estação do ano;
- Comparar os focos de incêndio com dados de desmatamento;
- Criar uma API para consulta dos dados processados.

---

## 👥 Autores

Projeto desenvolvido para análise de dados ambientais sobre focos de incêndio no Brasil, com foco em Minas Gerais.

Repositório:

```text
https://github.com/jvrezendem/analiseIncendioBR
```

---

## 📄 Licença

Este projeto pode ser utilizado para fins acadêmicos, educacionais e analíticos.

Caso deseje utilizar os dados, gráficos ou análises em outro projeto, recomenda-se citar este repositório como referência.

---

## ✅ Status do Projeto

```text
Em desenvolvimento
```

O projeto já conta com análises exploratórias, gráficos, mapas e indicadores produzidos, mas pode continuar evoluindo com novas visualizações, automações e modelos preditivos.
