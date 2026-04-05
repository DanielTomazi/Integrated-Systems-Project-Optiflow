"""
OptiFlow Logística Inteligente
==============================
Script: grafico_heatmap_motoristas.py
Módulo: Visualização — Heatmap de Motoristas
Descrição: Gera heatmap de quantidade de pedidos por motorista e região,
           evidenciando sobrecarga e ociosidade na alocação da frota.

Gráfico gerado:
    1. Heatmap: Pedidos por motorista × região (anotado com contagens)

Uso:
    python grafico_heatmap_motoristas.py

Dependências:
    pip install pandas matplotlib seaborn numpy
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ─────────────────────────────────────────────
# CONFIGURAÇÕES VISUAIS
# ─────────────────────────────────────────────

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "font.size":        10,
    "axes.titlesize":   13,
    "axes.titleweight": "bold",
    "figure.dpi":       120,
})

try:
    _BASE      = os.path.dirname(os.path.abspath(__file__))
    CLEAN_PATH = os.path.join(_BASE, "..", "data", "dataset_logistica_limpo.csv")
    RAW_PATH   = os.path.join(_BASE, "..", "data", "dataset_logistica.csv")
    OUTPUT_DIR = os.path.join(_BASE, "..", "data")
except NameError:
    CLEAN_PATH = os.path.join(os.getcwd(), "data", "dataset_logistica_limpo.csv")
    RAW_PATH   = os.path.join(os.getcwd(), "data", "dataset_logistica.csv")
    OUTPUT_DIR = os.path.join(os.getcwd(), "data")


# ─────────────────────────────────────────────
# CARREGAMENTO DE DADOS
# ─────────────────────────────────────────────

def carregar_dados() -> pd.DataFrame:
    """Carrega o dataset e garante colunas necessárias."""
    caminho = CLEAN_PATH if os.path.exists(CLEAN_PATH) else RAW_PATH
    df = pd.read_csv(caminho, encoding="utf-8")
    print(f"[OK] {len(df)} registros carregados de: {os.path.basename(caminho)}")
    return df


# ─────────────────────────────────────────────
# HEATMAP — PEDIDOS POR MOTORISTA E REGIÃO
# ─────────────────────────────────────────────

def gerar_heatmap_motoristas(df: pd.DataFrame) -> None:
    """
    Gera e salva heatmap de pedidos por motorista × região.

    Identifica motoristas sobrecarregados (muitos pedidos em múltiplas
    regiões) e ociosos (poucas atribuições), subsidiando o problema de
    alocação da Pesquisa Operacional.
    """
    if "motorista_id" not in df.columns or "regiao" not in df.columns:
        print("[AVISO] Colunas 'motorista_id' e/ou 'regiao' não encontradas. "
              "Execute limpeza_dados.py antes.")
        return

    pivot = (
        df.groupby(["motorista_id", "regiao"])
        .size()
        .unstack(fill_value=0)
    )

    # Limitar aos 15 motoristas com mais pedidos para legibilidade
    top_motoristas = pivot.sum(axis=1).nlargest(15).index
    pivot = pivot.loc[top_motoristas]

    fig, ax = plt.subplots(figsize=(10, 7))

    sns.heatmap(
        pivot,
        annot=True,
        fmt="d",
        cmap="YlOrRd",
        linewidths=0.5,
        linecolor="#cccccc",
        cbar_kws={"label": "Nº de Pedidos", "shrink": 0.8},
        ax=ax,
    )

    ax.set_title("Distribuição de Pedidos por Motorista e Região\nOptiFlow — Análise de Carga de Trabalho")
    ax.set_xlabel("Região de Entrega", fontsize=11)
    ax.set_ylabel("ID do Motorista", fontsize=11)
    ax.tick_params(axis="x", rotation=0)
    ax.tick_params(axis="y", rotation=0)

    plt.tight_layout()

    saida = os.path.join(OUTPUT_DIR, "grafico_heatmap_motoristas.png")
    plt.savefig(saida, bbox_inches="tight")
    plt.close()
    print(f"[OK] Gráfico salvo em: {saida}")


# ─────────────────────────────────────────────
# EXECUÇÃO PRINCIPAL
# ─────────────────────────────────────────────

if __name__ == "__main__":
    df = carregar_dados()
    gerar_heatmap_motoristas(df)
    print("\n[CONCLUÍDO] Heatmap de motoristas gerado com sucesso.")
