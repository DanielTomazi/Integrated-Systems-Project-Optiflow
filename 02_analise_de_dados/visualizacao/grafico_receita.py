"""
OptiFlow Logística Inteligente
==============================
Script: grafico_receita.py
Módulo: Visualização — Análise de Faturamento
Descrição: Gera gráficos de análise do faturamento ao longo do tempo
           e por região para a OptiFlow.

Gráficos gerados:
    1. Linha: Faturamento mensal total (série temporal)
    2. Barras agrupadas: Faturamento e custo mensal comparativo
    3. Pizza: Distribuição do faturamento por região
    4. Linha com anotações: Ticket médio mensal

Uso:
    python grafico_receita.py

Dependências:
    pip install pandas matplotlib seaborn
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


# ─────────────────────────────────────────────
# CONFIGURAÇÕES VISUAIS
# ─────────────────────────────────────────────

# Paleta de cores OptiFlow
COR_PRINCIPAL   = "#1A73E8"   # Azul OptiFlow
COR_SECUNDARIA  = "#EA4335"   # Vermelho alerta
COR_SUCESSO     = "#34A853"   # Verde positivo
COR_AVISO       = "#FBBC05"   # Amarelo atenção
PALETTE_REGIOES = ["#1A73E8", "#34A853", "#EA4335", "#FBBC05", "#9334E6"]

# Estilo global dos gráficos
plt.rcParams.update({
    "font.family":    "DejaVu Sans",
    "font.size":      11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "figure.dpi":     120,
})

# Caminhos
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
CLEAN_PATH   = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica_limpo.csv")
RAW_PATH     = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica.csv")
OUTPUT_DIR   = os.path.join(SCRIPT_DIR, "..", "data")


# ─────────────────────────────────────────────
# FUNÇÕES AUXILIARES
# ─────────────────────────────────────────────

def carregar_dados() -> pd.DataFrame:
    """Carrega e prepara o dataset para visualização."""
    caminho = CLEAN_PATH if os.path.exists(CLEAN_PATH) else RAW_PATH
    df = pd.read_csv(caminho, encoding="utf-8")
    df["data_pedido"] = pd.to_datetime(df["data_pedido"], errors="coerce")
    df["ano_mes"]     = df["data_pedido"].dt.to_period("M").astype(str)
    df["mes_abrev"]   = df["data_pedido"].dt.strftime("%b/%y")
    print(f"[OK] {len(df)} registros carregados.")
    return df


def formatar_eixo_brl(valor, pos):
    """Formata valores do eixo Y como R$ mil."""
    if valor >= 1000:
        return f"R${valor/1000:.1f}k"
    return f"R${valor:.0f}"


# ─────────────────────────────────────────────
# GRÁFICOS
# ─────────────────────────────────────────────

def grafico_faturamento_linha(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 1: Linha do faturamento mensal total ao longo do tempo.
    """
    mensal = df.groupby("mes_abrev")["valor_pedido"].sum().reset_index()
    # Ordenar cronologicamente
    mensal["data_aux"] = pd.to_datetime(
        df.groupby("mes_abrev")["data_pedido"].min().values
    )
    mensal = mensal.sort_values("data_aux")

    ax.plot(
        mensal["mes_abrev"], mensal["valor_pedido"],
        color=COR_PRINCIPAL, linewidth=2.5, marker="o", markersize=7,
        label="Faturamento Mensal"
    )

    # Preencher área sob a curva
    ax.fill_between(
        mensal["mes_abrev"], mensal["valor_pedido"],
        alpha=0.15, color=COR_PRINCIPAL
    )

    # Anotações nos picos e vales
    max_idx = mensal["valor_pedido"].idxmax()
    min_idx = mensal["valor_pedido"].idxmin()
    for idx, label, cor in [(max_idx, "Pico", COR_SUCESSO), (min_idx, "Mínimo", COR_SECUNDARIA)]:
        row = mensal.loc[idx]
        ax.annotate(
            f"{label}\nR${row['valor_pedido']/1000:.1f}k",
            xy=(row["mes_abrev"], row["valor_pedido"]),
            xytext=(0, 18), textcoords="offset points",
            ha="center", fontsize=9, color=cor,
            arrowprops=dict(arrowstyle="->", color=cor, lw=1.5)
        )

    ax.set_title("Faturamento Mensal — OptiFlow 2025")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Faturamento (R$)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(formatar_eixo_brl))
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)


def grafico_faturamento_vs_custo(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 2: Barras agrupadas comparando faturamento e custo mensal.
    """
    mensal = df.groupby("mes_abrev").agg(
        faturamento=("valor_pedido", "sum"),
        custo=("custo_entrega", "sum")
    ).reset_index()
    mensal["data_aux"] = pd.to_datetime(
        df.groupby("mes_abrev")["data_pedido"].min().values
    )
    mensal = mensal.sort_values("data_aux")

    x = range(len(mensal))
    largura = 0.38

    barras1 = ax.bar(
        [i - largura / 2 for i in x], mensal["faturamento"],
        width=largura, color=COR_PRINCIPAL, alpha=0.85, label="Faturamento"
    )
    barras2 = ax.bar(
        [i + largura / 2 for i in x], mensal["custo"],
        width=largura, color=COR_SECUNDARIA, alpha=0.85, label="Custo Logístico"
    )

    ax.set_title("Faturamento vs. Custo Logístico Mensal")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Valor (R$)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(mensal["mes_abrev"], rotation=45, ha="right")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(formatar_eixo_brl))
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)


def grafico_pizza_regiao(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 3: Pizza com distribuição percentual do faturamento por região.
    """
    fat_regiao = df.groupby("regiao_cliente")["valor_pedido"].sum().sort_values(ascending=False)

    wedges, texts, autotexts = ax.pie(
        fat_regiao.values,
        labels=fat_regiao.index,
        autopct="%1.1f%%",
        colors=PALETTE_REGIOES,
        startangle=90,
        pctdistance=0.82,
        wedgeprops={"linewidth": 1.5, "edgecolor": "white"}
    )
    for text in autotexts:
        text.set_fontsize(10)
        text.set_fontweight("bold")

    ax.set_title("Distribuição do Faturamento por Região")


def grafico_ticket_medio(df: pd.DataFrame, ax: plt.Axes) -> None:
    """
    Gráfico 4: Linha do ticket médio mensal com linha de referência.
    """
    ticket = df.groupby("mes_abrev")["valor_pedido"].mean().reset_index()
    ticket["data_aux"] = pd.to_datetime(
        df.groupby("mes_abrev")["data_pedido"].min().values
    )
    ticket = ticket.sort_values("data_aux")

    ticket_global = df["valor_pedido"].mean()

    ax.plot(
        ticket["mes_abrev"], ticket["valor_pedido"],
        color=COR_AVISO, linewidth=2.5, marker="s", markersize=7,
        label="Ticket Médio Mensal"
    )
    ax.axhline(
        ticket_global, color=COR_SUCESSO, linestyle="--",
        linewidth=1.5, label=f"Ticket Médio Global: R${ticket_global:.2f}"
    )

    ax.set_title("Ticket Médio Mensal dos Pedidos")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Ticket Médio (R$)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(formatar_eixo_brl))
    ax.tick_params(axis="x", rotation=45)
    ax.legend(fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.4)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    """Gera o painel completo de gráficos de receita."""
    print("=" * 55)
    print("  OptiFlow — Gráficos de Receita e Faturamento")
    print("=" * 55)

    df = carregar_dados()

    # Criar figura com 4 subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(
        "OptiFlow Logística Inteligente — Análise de Receita 2025",
        fontsize=16, fontweight="bold", y=1.01
    )

    grafico_faturamento_linha(df, axes[0, 0])
    grafico_faturamento_vs_custo(df, axes[0, 1])
    grafico_pizza_regiao(df, axes[1, 0])
    grafico_ticket_medio(df, axes[1, 1])

    plt.tight_layout()

    # Salvar
    output_path = os.path.join(OUTPUT_DIR, "grafico_receita.png")
    plt.savefig(output_path, bbox_inches="tight", dpi=150)
    print(f"\n[OK] Gráfico salvo em: {os.path.abspath(output_path)}")

    plt.show()
    print("[OK] Gráficos exibidos com sucesso.")


if __name__ == "__main__":
    main()
