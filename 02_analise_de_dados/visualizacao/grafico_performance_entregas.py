"""
OptiFlow Logística Inteligente
==============================
Script: grafico_performance_entregas.py
Módulo: Visualização — Performance de Entregas
Descrição: Gera gráficos de análise de performance operacional das
           entregas, por região, motorista e dimensão temporal.

Gráficos gerados:
    1. Barras horizontais: Número de entregas por região
    2. Barras empilhadas: Entregas no prazo vs. atrasadas por região
    3. Boxplot: Distribuição do tempo de entrega por região
    4. Heatmap: Quantidade de pedidos por motorista e região
    5. Barras: Custo médio de entrega por região
    6. Linha: Volume de pedidos ao longo do tempo

Uso:
    python grafico_performance_entregas.py

Dependências:
    pip install pandas matplotlib seaborn numpy
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


# ─────────────────────────────────────────────
# CONFIGURAÇÕES VISUAIS
# ─────────────────────────────────────────────

PALETTE = {
    "Centro": "#1A73E8",
    "Norte":  "#34A853",
    "Sul":    "#EA4335",
    "Leste":  "#FBBC05",
    "Oeste":  "#9334E6",
}
COR_NO_PRAZO  = "#34A853"
COR_ATRASADA  = "#EA4335"
COR_PRINCIPAL = "#1A73E8"

plt.rcParams.update({
    "font.family":   "DejaVu Sans",
    "font.size":     10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "figure.dpi":    120,
})

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
CLEAN_PATH  = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica_limpo.csv")
RAW_PATH    = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica.csv")
OUTPUT_DIR  = os.path.join(SCRIPT_DIR, "..", "data")


# ─────────────────────────────────────────────
# CARREGAMENTO DE DADOS
# ─────────────────────────────────────────────

def carregar_dados() -> pd.DataFrame:
    """Carrega o dataset e prepara colunas auxiliares."""
    caminho = CLEAN_PATH if os.path.exists(CLEAN_PATH) else RAW_PATH
    df = pd.read_csv(caminho, encoding="utf-8")
    df["data_pedido"]     = pd.to_datetime(df["data_pedido"], errors="coerce")
    df["ano_mes"]         = df["data_pedido"].dt.to_period("M").astype(str)
    df["mes_abrev"]       = df["data_pedido"].dt.strftime("%b/%y")

    if "entrega_no_prazo" not in df.columns:
        df["entrega_no_prazo"] = df["tempo_entrega"] <= 180

    df["status_entrega"] = df["entrega_no_prazo"].map(
        {True: "No Prazo", False: "Atrasada"}
    )

    print(f"[OK] {len(df)} registros carregados.")
    return df


# ─────────────────────────────────────────────
# GRÁFICOS
# ─────────────────────────────────────────────

def grafico_entregas_por_regiao(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 1: Barras horizontais — volume de entregas por região.
    """
    contagem = df["regiao_cliente"].value_counts().sort_values()
    cores    = [PALETTE.get(r, COR_PRINCIPAL) for r in contagem.index]

    barras = ax.barh(contagem.index, contagem.values, color=cores, alpha=0.85, edgecolor="white")

    # Rótulos de valor ao final de cada barra
    for barra in barras:
        ax.text(
            barra.get_width() + 0.5, barra.get_y() + barra.get_height() / 2,
            f"{int(barra.get_width())}",
            va="center", ha="left", fontsize=10, fontweight="bold"
        )

    ax.set_title("Volume de Entregas por Região")
    ax.set_xlabel("Número de Entregas")
    ax.set_ylabel("Região")
    ax.grid(axis="x", linestyle="--", alpha=0.4)


def grafico_prazo_por_regiao(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 2: Barras empilhadas — entregas no prazo vs. atrasadas por região.
    """
    pivot = df.groupby(["regiao_cliente", "status_entrega"]).size().unstack(fill_value=0)

    # Garantir as colunas
    for col in ["No Prazo", "Atrasada"]:
        if col not in pivot.columns:
            pivot[col] = 0

    regioes = pivot.index.tolist()
    x = range(len(regioes))

    ax.bar(x, pivot["No Prazo"], color=COR_NO_PRAZO, alpha=0.85, label="No Prazo")
    ax.bar(x, pivot["Atrasada"], bottom=pivot["No Prazo"],
           color=COR_ATRASADA, alpha=0.85, label="Atrasada")

    # Percentual no prazo no topo
    for i, regiao in enumerate(regioes):
        total = pivot.loc[regiao, "No Prazo"] + pivot.loc[regiao, "Atrasada"]
        pct   = pivot.loc[regiao, "No Prazo"] / total * 100 if total > 0 else 0
        ax.text(i, total + 0.5, f"{pct:.0f}%", ha="center", fontsize=9,
                color=COR_NO_PRAZO, fontweight="bold")

    ax.set_title("Entregas: No Prazo vs. Atrasadas por Região")
    ax.set_xticks(list(x))
    ax.set_xticklabels(regioes)
    ax.set_ylabel("Quantidade")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)


def grafico_boxplot_tempo(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 3: Boxplot da distribuição do tempo de entrega por região.
    """
    regioes_ordenadas = df.groupby("regiao_cliente")["tempo_entrega"].median().sort_values().index.tolist()

    sns.boxplot(
        data=df, x="regiao_cliente", y="tempo_entrega",
        order=regioes_ordenadas, ax=ax,
        palette=PALETTE, width=0.5,
        linewidth=1.5, flierprops={"marker": "o", "markersize": 4, "alpha": 0.5}
    )

    # Linha de referência: prazo máximo
    ax.axhline(180, color=COR_ATRASADA, linestyle="--",
               linewidth=1.5, label="Limite de Prazo (180 min)")

    ax.set_title("Distribuição do Tempo de Entrega por Região")
    ax.set_xlabel("Região")
    ax.set_ylabel("Tempo de Entrega (min)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.4)


def grafico_custo_medio_regiao(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 4: Barras — custo médio de entrega por região com linha de meta.
    """
    custo = df.groupby("regiao_cliente")["custo_entrega"].mean().sort_values(ascending=False)
    cores = [PALETTE.get(r, COR_PRINCIPAL) for r in custo.index]
    meta  = df["custo_entrega"].mean()

    barras = ax.bar(custo.index, custo.values, color=cores, alpha=0.85, edgecolor="white")
    ax.axhline(meta, color="black", linestyle="--", linewidth=1.5,
               label=f"Média Global: R${meta:.2f}")

    for barra in barras:
        ax.text(
            barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.3,
            f"R${barra.get_height():.2f}",
            ha="center", va="bottom", fontsize=9, fontweight="bold"
        )

    ax.set_title("Custo Médio de Entrega por Região")
    ax.set_xlabel("Região")
    ax.set_ylabel("Custo Médio (R$)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.4)


def grafico_volume_temporal(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 5: Linha do volume de pedidos ao longo do tempo.
    """
    volume = df.groupby("mes_abrev").size().reset_index(name="total")
    volume["data_aux"] = pd.to_datetime(
        df.groupby("mes_abrev")["data_pedido"].min().values
    )
    volume = volume.sort_values("data_aux")

    ax.plot(
        volume["mes_abrev"], volume["total"],
        color=COR_PRINCIPAL, linewidth=2.5, marker="^", markersize=8
    )
    ax.fill_between(volume["mes_abrev"], volume["total"], alpha=0.12, color=COR_PRINCIPAL)

    media = volume["total"].mean()
    ax.axhline(media, color="gray", linestyle="--", linewidth=1.2,
               label=f"Média: {media:.1f} pedidos/mês")

    ax.set_title("Volume de Pedidos ao Longo do Tempo")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Número de Pedidos")
    ax.tick_params(axis="x", rotation=45)
    ax.legend(fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.4)


def grafico_heatmap_motorista_regiao(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 6: Heatmap — número de entregas por motorista e região.
    """
    pivot = df.pivot_table(
        index="id_motorista", columns="regiao_cliente",
        values="id_pedido", aggfunc="count", fill_value=0
    )
    # Ordenar motoristas por total de entregas
    pivot["_total"] = pivot.sum(axis=1)
    pivot = pivot.sort_values("_total", ascending=False).drop(columns="_total")

    sns.heatmap(
        pivot, ax=ax, annot=True, fmt="d", cmap="Blues",
        linewidths=0.5, cbar_kws={"label": "Qtd. Entregas"},
        linecolor="white"
    )
    ax.set_title("Entregas por Motorista e Região (Heatmap)")
    ax.set_xlabel("Região")
    ax.set_ylabel("Motorista")
    ax.tick_params(axis="x", rotation=0)
    ax.tick_params(axis="y", rotation=0)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    """Gera e salva o painel de performance de entregas."""
    print("=" * 55)
    print("  OptiFlow — Gráficos de Performance de Entregas")
    print("=" * 55)

    df = carregar_dados()

    # Painel 1: 2×2 (Regiões e Prazo)
    fig1, axes1 = plt.subplots(2, 2, figsize=(16, 12))
    fig1.suptitle(
        "OptiFlow — Performance de Entregas por Região 2025",
        fontsize=15, fontweight="bold"
    )
    grafico_entregas_por_regiao(df, axes1[0, 0])
    grafico_prazo_por_regiao(df, axes1[0, 1])
    grafico_boxplot_tempo(df, axes1[1, 0])
    grafico_custo_medio_regiao(df, axes1[1, 1])
    plt.tight_layout()
    output1 = os.path.join(OUTPUT_DIR, "grafico_performance_entregas.png")
    fig1.savefig(output1, bbox_inches="tight", dpi=150)
    print(f"[OK] Painel 1 salvo em: {os.path.abspath(output1)}")

    # Painel 2: 1×2 (Temporal e Heatmap)
    fig2, axes2 = plt.subplots(1, 2, figsize=(18, 7))
    fig2.suptitle(
        "OptiFlow — Volume Temporal e Distribuição por Motorista",
        fontsize=15, fontweight="bold"
    )
    grafico_volume_temporal(df, axes2[0])
    grafico_heatmap_motorista_regiao(df, axes2[1])
    plt.tight_layout()
    output2 = os.path.join(OUTPUT_DIR, "grafico_heatmap_motoristas.png")
    fig2.savefig(output2, bbox_inches="tight", dpi=150)
    print(f"[OK] Painel 2 salvo em: {os.path.abspath(output2)}")

    plt.show()
    print("[OK] Todos os gráficos exibidos.")


if __name__ == "__main__":
    main()
