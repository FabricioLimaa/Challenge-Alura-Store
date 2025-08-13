import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================================================================
# 1. SEÇÃO DE CONFIGURAÇÃO
# Centraliza todas as variáveis que podem mudar, facilitando a manutenção.
# ==============================================================================
CONFIG = {
    'caminho_dados': './',
    'caminho_graficos': './graficos_gerados/',
    'lojas': {
        'loja_1.csv': 'Zonix Barra da Tijuca',
        'loja_2.csv': 'Zonix Campo Grande',
        'loja_3.csv': 'Zonix Recreio',
        'loja_4.csv': 'Zonix Jacarepaguá'
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
        
    return pd.concat(dfs, ignore_index=True)

def plotar_faturamento(df, caminho_saida):
    """Analisa e plota o faturamento total por loja."""
    print("Analisando faturamento...")
    faturamento = df.groupby('Loja')['Preço'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 7))
    faturamento.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title('Faturamento Total por Loja (Zonix)', fontsize=16)
    plt.ylabel('Faturamento (R$)')
    plt.xlabel('')
    plt.xticks(rotation=25, ha='right')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.2f}'))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_saida, 'faturamento_zonix.png'))
    plt.close()

def plotar_avaliacoes(df, caminho_saida):
    """Analisa e plota a média de avaliação por loja."""
    print("Analisando avaliações...")
    avaliacoes = df.groupby('Loja')['Avaliação da compra'].mean().sort_values()

    plt.figure(figsize=(12, 7))
    bars = plt.barh(avaliacoes.index, avaliacoes.values, color=['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4'])
    plt.title('Média de Avaliação dos Clientes por Loja (Zonix)', fontsize=16)
    plt.xlabel('Média da Avaliação (de 1 a 5)')
    plt.ylabel('Loja')
    plt.xlim(0, 5.5)
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}', va='center')
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_saida, 'avaliacoes_zonix.png'))
    plt.close()

# (Aqui iriam as outras funções de plotagem: categorias, frete, produtos...)

# ==============================================================================
# 3. FUNÇÃO PRINCIPAL (main)
# Orquestra a execução do script.
# ==============================================================================

def main():
    """Função principal que executa o fluxo completo da análise."""
    # Garante que o diretório de saída para os gráficos exista
    os.makedirs(CONFIG['caminho_graficos'], exist_ok=True)
    
    df_completo = carregar_dados(CONFIG)
    
    if df_completo is not None:
        # Executa cada etapa da análise
        plotar_faturamento(df_completo, CONFIG['caminho_graficos'])
        plotar_avaliacoes(df_completo, CONFIG['caminho_graficos'])
        # (Chamadas para as outras funções de análise aqui)
        
        print(f"\nAnálise concluída! Gráficos salvos em: {CONFIG['caminho_graficos']}")

# ==============================================================================
# Ponto de Entrada do Script
# A construção `if __name__ == "__main__"` é uma boa prática em Python.
# ==============================================================================
if __name__ == "__main__":
    main()