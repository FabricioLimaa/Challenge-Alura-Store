import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================================================================
# 1. SEÇÃO DE CONFIGURAÇÃO
# Centraliza todas as variáveis que podem mudar, facilitando a manutenção.
# ==============================================================================
CONFIG = {
    'caminho_dados': './dados/',
    'caminho_graficos': './graficos_gerados/',
    'lojas': {
        'loja_1.csv': 'Alura Store Barra da Tijuca',
        'loja_2.csv': 'Alura Store Campo Grande',
        'loja_3.csv': 'Alura Store Recreio',
        'loja_4.csv': 'Alura Store Jacarepaguá'
    },
    'paleta_cores': ['#F2E205', '#A68C0A', '#F2CB05', '#F2EBC4', '#0D0D0D'],
    'mapa_colunas': {
        'Preço': 'preco',
        'Categoria do Produto': 'categoria_produto',
        'Avaliação da compra': 'avaliacao_compra',
        'Frete': 'frete',
        'Produto': 'produto',
        'Loja': 'loja'
    }
}

# ==============================================================================
# 2. FUNÇÕES DE ANÁLISE E PLOTAGEM
# Cada análise complexa é encapsulada em sua própria função.
# ==============================================================================

def carregar_dados(config):
    """
    Carrega os dados de múltiplos arquivos CSV, adiciona o nome da loja
    e concatena tudo em um único DataFrame.
    """
    dfs = []
    print("Carregando dados...")
    for arquivo, nome_loja in config['lojas'].items():
        caminho_completo = os.path.join(config['caminho_dados'], arquivo)
        try:
            df = pd.read_csv(caminho_completo)
            df['Loja'] = nome_loja
            dfs.append(df)
        except FileNotFoundError:
            print(f"AVISO: O arquivo '{caminho_completo}' não foi encontrado e será ignorado.")
    
    if not dfs:
        print("ERRO: Nenhum dado foi carregado. Verifique os caminhos dos arquivos.")
        return None
        
    print("Dados carregados com sucesso.")
    return pd.concat(dfs, ignore_index=True)

def plotar_faturamento(df, config):
    """Analisa e plota o faturamento total por loja."""
    print("Analisando faturamento...")
    faturamento = df.groupby('Loja')['Preço'].sum()
    
    plt.figure(figsize=(10, 8))
    faturamento.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=config['paleta_cores'])
    plt.title('Faturamento Total por Loja (Alura Store)', fontsize=16)
    plt.ylabel('')  # Remove o rótulo do eixo Y
    plt.tight_layout()
    plt.savefig(os.path.join(config['caminho_graficos'], 'faturamento_alura_store.png'))
    plt.close()

def plotar_categorias(df, config):
    """Analisa e plota as vendas por categoria."""
    print("Analisando vendas por categoria...")
    vendas_categoria = df.groupby(['Categoria do Produto', 'Loja']).size().unstack(fill_value=0)
    
    vendas_categoria.plot(kind='bar', stacked=True, figsize=(14, 8), color=config['paleta_cores'])
    plt.title('Vendas por Categoria em Cada Loja (Alura Store)', fontsize=16)
    plt.xlabel('Categoria do Produto')
    plt.ylabel('Quantidade de Vendas')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Loja')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(config['caminho_graficos'], 'categorias_alura_store.png'))
    plt.close()

def plotar_avaliacoes(df, config):
    """Analisa e plota a média de avaliação por loja."""
    print("Analisando avaliações...")
    avaliacoes = df.groupby('Loja')['Avaliação da compra'].mean()

    plt.figure(figsize=(12, 7))

    # Gráfico de barras
    avaliacoes.plot(kind='bar', color=config['paleta_cores'][1], alpha=0.7, label='Média de Avaliação (Barras)')

    # Gráfico de linha sobreposto
    avaliacoes.plot(kind='line', marker='o', color=config['paleta_cores'][0], linewidth=2, label='Média de Avaliação (Linha)')

    plt.title('Média de Avaliação dos Clientes por Loja (Alura Store)', fontsize=16)
    plt.xlabel('Loja')
    plt.ylabel('Média da Avaliação (de 1 a 5)')
    plt.ylim(0, 5.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(config['caminho_graficos'], 'avaliacoes_alura_store.png'))
    plt.close()

def plotar_frete(df, config):
    """Analisa e plota o frete médio por loja."""
    print("Analisando frete médio...")
    frete = df.groupby('Loja')['Frete'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 7))
    frete.plot(kind='barh', color=config['paleta_cores'])
    plt.title('Custo Médio de Frete por Loja (Alura Store)', fontsize=16)
    plt.xlabel('Custo Médio do Frete (R$)')
    plt.ylabel('Loja')
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.2f}'))
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(config['caminho_graficos'], 'frete_alura_store.png'))
    plt.close()  # Adicionado para evitar problemas de memória

def analisar_e_plotar_produtos(df, config):
    """Analisa e plota os produtos mais e menos vendidos."""
    print("Analisando produtos mais e menos vendidos...")
    contagem_produtos = df.groupby(['Loja', 'Produto']).size()
    lojas_ordenadas = sorted(df['Loja'].unique())

    # Mais Vendidos
    fig_top, axes_top = plt.subplots(2, 2, figsize=(15, 12), constrained_layout=True)
    fig_top.suptitle('Top 5 Produtos Mais Vendidos por Loja (Alura Store)', fontsize=18)
    axes_top = axes_top.flatten()

    # Menos Vendidos
    fig_bottom, axes_bottom = plt.subplots(2, 2, figsize=(15, 12), constrained_layout=True)
    fig_bottom.suptitle('Top 5 Produtos Menos Vendidos por Loja (Alura Store)', fontsize=18)
    axes_bottom = axes_bottom.flatten()
    
    for i, loja in enumerate(lojas_ordenadas):
        produtos_loja = contagem_produtos.loc[loja]
        
        # Plot mais vendidos
        mais_vendidos = produtos_loja.nlargest(5)
        mais_vendidos.sort_values().plot(kind='barh', ax=axes_top[i], color=config['paleta_cores'])
        axes_top[i].set_title(loja)
        axes_top[i].set_xlabel('Quantidade Vendida')

        # Plot menos vendidos
        menos_vendidos = produtos_loja.nsmallest(5)
        menos_vendidos.sort_values(ascending=False).plot(kind='barh', ax=axes_bottom[i], color=config['paleta_cores'])
        axes_bottom[i].set_title(loja)
        axes_bottom[i].set_xlabel('Quantidade Vendida')

    fig_top.savefig(os.path.join(config['caminho_graficos'], 'top_5_produtos_alura_store.png'))
    fig_bottom.savefig(os.path.join(config['caminho_graficos'], 'bottom_5_produtos_alura_store.png'))
    plt.close(fig_top)
    plt.close(fig_bottom)

# ==============================================================================
# 3. FUNÇÃO PRINCIPAL (main)
# Orquestra a execução do script.
# ==============================================================================

def main():
    """Função principal que executa o fluxo completo da análise."""
    os.makedirs(CONFIG['caminho_graficos'], exist_ok=True)
    
    df_completo = carregar_dados(CONFIG)
    
    if df_completo is not None:
        plotar_faturamento(df_completo, CONFIG)
        plotar_categorias(df_completo, CONFIG)
        plotar_avaliacoes(df_completo, CONFIG)
        plotar_frete(df_completo, CONFIG)
        analisar_e_plotar_produtos(df_completo, CONFIG)
        
        print(f"\nAnálise completa! Gráficos salvos em: {CONFIG['caminho_graficos']}")

# ==============================================================================
# Ponto de Entrada do Script
# ==============================================================================
if __name__ == "__main__":
    main()