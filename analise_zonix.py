import matplotlib
matplotlib.use('Agg')  # Define o backend para evitar o uso do Tkinter
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime  # Import necessário para data e hora

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

def limpar_diretorio(caminho):
    """Remove todos os arquivos do diretório especificado."""
    if os.path.exists(caminho):
        for arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
    else:
        os.makedirs(caminho)

def gerar_nome_arquivo(base_nome):
    """Gera um nome de arquivo com data e hora."""
    data_hora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f"{base_nome}_{data_hora}.png"

def plotar_faturamento(df, config):
    """Analisa e plota o faturamento total por loja."""
    print("Analisando faturamento...")
    faturamento = df.groupby('Loja')['Preço'].sum()

    plt.figure(figsize=(10, 8))
    faturamento.plot(kind='pie', autopct=lambda p: f'{p:.1f}%', startangle=90, colors=config['paleta_cores'])
    plt.title('Faturamento Total por Loja (Alura Store)', fontsize=16)
    plt.ylabel('')  # Remove o rótulo do eixo Y
    plt.tight_layout()
    nome_arquivo = gerar_nome_arquivo('faturamento_alura_store')
    plt.savefig(os.path.join(config['caminho_graficos'], nome_arquivo))
    plt.close()

def plotar_categorias(df, config):
    """Analisa e plota as vendas por categoria."""
    print("Analisando vendas por categoria...")
    vendas_categoria = df.groupby(['Categoria do Produto', 'Loja']).size().unstack(fill_value=0)

    ax = vendas_categoria.plot(kind='bar', stacked=True, figsize=(14, 8), color=config['paleta_cores'])
    plt.title('Vendas por Categoria em Cada Loja (Alura Store)', fontsize=16)
    plt.xlabel('Categoria do Produto')
    plt.ylabel('Quantidade de Vendas')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Loja')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adiciona os valores nas barras empilhadas
    for p in ax.patches:
        if p.get_height() > 0:  # Apenas exibe valores maiores que zero
            ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_y() + p.get_height() / 2),
                        ha='center', va='center', fontsize=9, color='black')

    plt.tight_layout()
    nome_arquivo = gerar_nome_arquivo('categorias_alura_store')
    plt.savefig(os.path.join(config['caminho_graficos'], nome_arquivo))
    plt.close()

def plotar_avaliacoes(df, config):
    """Analisa e plota a média de avaliação por loja."""
    print("Analisando avaliações...")
    avaliacoes = df.groupby('Loja')['Avaliação da compra'].mean()

    plt.figure(figsize=(12, 7))

    # Gráfico de barras
    barras = avaliacoes.plot(kind='bar', color=config['paleta_cores'][1], alpha=0.7, label='Média de Avaliação (Barras)')

    # Adiciona os valores no topo das barras
    for i, valor in enumerate(avaliacoes):
        plt.text(i, valor + 0.1, f'{valor:.2f}', ha='center', fontsize=10)

    # Gráfico de linha sobreposto
    linha = avaliacoes.plot(kind='line', marker='o', color=config['paleta_cores'][0], linewidth=2, label='Média de Avaliação (Linha)')

    # Adiciona os valores nos pontos da linha
    for i, valor in enumerate(avaliacoes):
        plt.text(i, valor - 0.2, f'{valor:.2f}', ha='center', fontsize=10, color=config['paleta_cores'][0])

    plt.title('Média de Avaliação dos Clientes por Loja (Alura Store)', fontsize=16)
    plt.xlabel('Loja')
    plt.ylabel('Média da Avaliação (de 1 a 5)')
    plt.ylim(0, 5.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    nome_arquivo = gerar_nome_arquivo('avaliacoes_alura_store')
    plt.savefig(os.path.join(config['caminho_graficos'], nome_arquivo))
    plt.close()

def plotar_frete(df, config):
    """Analisa e plota o frete médio por loja."""
    print("Analisando frete médio...")
    frete = df.groupby('Loja')['Frete'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 7))
    barras = frete.plot(kind='barh', color=config['paleta_cores'])
    plt.title('Custo Médio de Frete por Loja (Alura Store)', fontsize=16)
    plt.xlabel('Custo Médio do Frete (R$)')
    plt.ylabel('Loja')
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.2f}'))
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Adiciona os valores ao lado das barras
    for i, valor in enumerate(frete):
        plt.text(valor + 0.1, i, f'R$ {valor:.2f}', va='center', fontsize=10)

    plt.tight_layout()
    nome_arquivo = gerar_nome_arquivo('frete_alura_store')
    plt.savefig(os.path.join(config['caminho_graficos'], nome_arquivo))
    plt.close()

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
        ax_top = axes_top[i]
        mais_vendidos.sort_values().plot(kind='barh', ax=ax_top, color=config['paleta_cores'])
        ax_top.set_title(loja)
        ax_top.set_xlabel('Quantidade Vendida')

        # Adiciona os valores nas barras (mais vendidos)
        for p in ax_top.patches:
            ax_top.annotate(f'{int(p.get_width())}', (p.get_width() + 0.1, p.get_y() + p.get_height() / 2),
                            ha='left', va='center', fontsize=9, color='black')

        # Plot menos vendidos
        menos_vendidos = produtos_loja.nsmallest(5)
        ax_bottom = axes_bottom[i]
        menos_vendidos.sort_values(ascending=False).plot(kind='barh', ax=ax_bottom, color=config['paleta_cores'])
        ax_bottom.set_title(loja)
        ax_bottom.set_xlabel('Quantidade Vendida')

        # Adiciona os valores nas barras (menos vendidos)
        for p in ax_bottom.patches:
            ax_bottom.annotate(f'{int(p.get_width())}', (p.get_width() + 0.1, p.get_y() + p.get_height() / 2),
                               ha='left', va='center', fontsize=9, color='black')

    fig_top.savefig(os.path.join(config['caminho_graficos'], gerar_nome_arquivo('top_5_produtos_alura_store')))
    fig_bottom.savefig(os.path.join(config['caminho_graficos'], gerar_nome_arquivo('bottom_5_produtos_alura_store')))
    plt.close(fig_top)
    plt.close(fig_bottom)

# ==============================================================================
# 3. FUNÇÃO PRINCIPAL (main)
# Orquestra a execução do script.
# ==============================================================================

def main():
    """Função principal que executa o fluxo completo da análise."""
    limpar_diretorio(CONFIG['caminho_graficos'])  # Limpa o diretório antes de gerar novos gráficos
    
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