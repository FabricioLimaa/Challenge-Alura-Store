# 📊 Análise Estratégica - Alura Store

## 📖 Propósito da Análise

Este projeto tem como objetivo realizar uma análise detalhada de dados de quatro lojas da rede fictícia **Alura Store**, localizadas na Zona Oeste do Rio de Janeiro. A análise busca identificar o desempenho de cada unidade com base em métricas como faturamento, vendas por categoria, satisfação do cliente e custos operacionais (frete). 

O resultado final é uma recomendação estratégica sobre qual loja deve ser vendida para otimizar os negócios da rede, simulando um case de **Business Intelligence**.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas:** Para carregamento, manipulação e análise dos dados.
* **Matplotlib:** Para a criação de visualizações gráficas.

---

## 📁 Estrutura do Projeto

O projeto é organizado com os dados de entrada, o script de análise e os relatórios visuais gerados.

/
*|-- dados/
*|   |-- loja_1.csv               # Dados brutos da Alura Store Barra da Tijuca
|   |-- loja_2.csv               # Dados brutos da Alura Store Campo Grande
|   |-- loja_3.csv               # Dados brutos da Alura Store Recreio
|   |-- loja_4.csv               # Dados brutos da Alura Store Jacarepaguá
|
|-- analise_alura.py             # Script Python contendo todo o código da análise
|
|-- graficos_gerados/            # Diretório contendo os gráficos gerados pela análise
|   |-- faturamento_alura.png        # Gráfico de faturamento total por loja
|   |-- categorias_alura.png         # Gráfico de vendas por categoria
|   |-- avaliacoes_alura.png         # Gráfico de média de avaliações por loja
|   |-- top_5_produtos_alura.png     # Gráfico dos 5 produtos mais vendidos por loja
|   |-- bottom_5_produtos_alura.png  # Gráfico dos 5 produtos menos vendidos por loja
|   |-- frete_alura.png              # Gráfico de custo médio de frete por loja
|
|-- README.md                    # Este arquivo com a documentação do projeto

## 🚀 Como Executar o Projeto

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado.

2.  **Instalação de Dependências:** Instale as bibliotecas necessárias.
    ```bash
    pip install pandas matplotlib
    ```

3.  **Execução:** Execute o script principal de análise.
    ```bash
    python analise_alura.py
    ```
    Ao final da execução, os gráficos serão salvos no diretório [graficos_gerados](http://_vscodecontentref_/2).

## 📊 Análises Realizadas

Foram investigadas cinco métricas principais para cada loja da rede Alura Store:

1.  **Faturamento Total:** Receita bruta total de cada unidade.
2.  **Vendas por Categoria:** Volume de vendas para cada categoria de produto.
3.  **Média de Avaliação dos Clientes:** Nível de satisfação do cliente (escala de 1 a 5).
4.  **Produtos Mais e Menos Vendidos:** Identificação dos produtos com maior e menor volume de vendas.
5.  **Custo Médio de Frete:** Eficiência logística e custo operacional por venda.

---

## 📊 Exemplos de Gráficos e Insights Obtidos

### 1. **Faturamento Total por Loja**
![Faturamento Total](graficos_gerados/faturamento_alura.png)

- A **Alura Store Barra da Tijuca** apresentou o maior faturamento, mas também os maiores custos operacionais.

### 2. **Vendas por Categoria**
![Vendas por Categoria](graficos_gerados/categorias_alura.png)

- As categorias mais vendidas variam entre as lojas, destacando a importância de estratégias locais.

### 3. **Média de Avaliação dos Clientes**
![Média de Avaliação](graficos_gerados/avaliacoes_alura.png)

- A **Alura Store Jacarepaguá** obteve a melhor avaliação média dos clientes, indicando maior satisfação.

### 4. **Produtos Mais e Menos Vendidos**
![Top 5 Produtos](graficos_gerados/top_5_produtos_alura.png)
![Bottom 5 Produtos](graficos_gerados/bottom_5_produtos_alura.png)

- Produtos mais vendidos são consistentes entre as lojas, mas os menos vendidos variam significativamente.

### 5. **Custo Médio de Frete**
![Custo Médio de Frete](graficos_gerados/frete_alura.png)

- A **Alura Store Barra da Tijuca** apresentou o maior custo médio de frete, impactando sua eficiência operacional.

---

## 🚀 Como Executar o Projeto

1. **Pré-requisitos:** Certifique-se de ter o Python 3 instalado em sua máquina.

2. **Instalação de Dependências:** Instale as bibliotecas necessárias.
    ```bash
    pip install pandas matplotlib
    ```

3. **Execução do Script:** Execute o script principal de análise.
    ```bash
    python analise_alura.py
    ```
    Após a execução, os gráficos serão salvos no diretório [graficos_gerados](http://_vscodecontentref_/3).

4. **Execução no Notebook (Opcional):** Caso prefira uma análise interativa, utilize o notebook no Google Colab ou Jupyter Notebook.

---

## 🏆 Conclusão e Recomendação

Com base na análise consolidada dos dados, a recomendação estratégica é a **venda da loja Alura Store Barra da Tijuca**.

Embora apresente o maior faturamento, esta unidade demonstrou ser a menos eficiente, registrando a **pior avaliação média dos clientes** e o **maior custo médio de frete**. A decisão prioriza a saúde do negócio a longo prazo, focando em eficiência operacional e satisfação do cliente, áreas em que a **Alura Store Jacarepaguá**, apesar do menor faturamento, mostrou ter mais força e potencial.

---

## ✒️ Autor

* **Fabricio Lima**
* **[GitHub](https://github.com/FabricioLimaa)**
