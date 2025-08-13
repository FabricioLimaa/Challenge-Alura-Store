# Análise Estratégica - Lojas Zonix

## 📖 Descrição do Projeto

Este projeto realiza uma análise de dados detalhada de quatro lojas da rede fictícia "Zonix", localizadas na Zona Oeste do Rio de Janeiro. O objetivo é avaliar o desempenho de cada unidade com base em métricas de faturamento, vendas, satisfação do cliente e custos operacionais (frete). A análise resulta em uma recomendação estratégica sobre qual loja deveria ser vendida para otimizar os negócios da rede.

O projeto simula um case de Business Intelligence, onde os dados são transformados em insights acionáveis para a tomada de decisão.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas:** Para carregamento, manipulação e análise dos dados.
* **Matplotlib:** Para a criação das visualizações gráficas.

## 📁 Estrutura do Projeto

O projeto é organizado com os dados de entrada, o script de análise e os relatórios visuais gerados.

/
|-- dados/
|   |-- loja_1.csv               # Dados brutos da Zonix Barra da Tijuca
|   |-- loja_2.csv               # Dados brutos da Zonix Campo Grande
|   |-- loja_3.csv               # Dados brutos da Zonix Recreio
|   |-- loja_4.csv               # Dados brutos da Zonix Jacarepaguá
|
|-- analise_zonix.py         # Script Python contendo todo o código da análise
|
|-- graficos_gerados/          # Diretório contendo as visualizações
|   |-- faturamento_zonix.png
|   |-- categorias_zonix.png
|   |-- avaliacoes_zonix.png
|   |-- top_5_produtos_zonix.png
|   |-- bottom_5_produtos_zonix.png
|   |-- frete_zonix.png
|
|-- README.md                # Este arquivo

## 🚀 Como Executar o Projeto

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado.

2.  **Instalação de Dependências:** Instale as bibliotecas necessárias.
    ```bash
    pip install pandas matplotlib
    ```

3.  **Execução:** Execute o script principal de análise.
    ```bash
    python analise_zonix.py
    ```
    Ao final da execução, os gráficos serão salvos no diretório `graficos_gerados/`.

## 📊 Análises Realizadas

Foram investigadas cinco métricas principais para cada loja da rede Zonix:

1.  **Faturamento Total:** Receita bruta total de cada unidade.
2.  **Vendas por Categoria:** Volume de vendas para cada categoria de produto.
3.  **Média de Avaliação dos Clientes:** Nível de satisfação do cliente (escala de 1 a 5).
4.  **Produtos Mais e Menos Vendidos:** Identificação dos produtos com maior e menor volume de vendas.
5.  **Custo Médio de Frete:** Eficiência logística e custo operacional por venda.

## 🏆 Conclusão e Recomendação

Com base na análise consolidada dos dados, a recomendação estratégica é a **venda da loja Zonix Barra da Tijuca**.

Embora apresente o maior faturamento, esta unidade demonstrou ser a menos eficiente, registrando a **pior avaliação média dos clientes** e o **maior custo médio de frete**. A decisão prioriza a saúde do negócio a longo prazo, focando em eficiência operacional e satisfação do cliente, áreas em que a **Zonix Jacarepaguá**, apesar do menor faturamento, mostrou ter mais força e potencial.

## ✒️ Autor

* **[Seu Nome Completo]**
* **[Link para seu LinkedIn ou GitHub]**
