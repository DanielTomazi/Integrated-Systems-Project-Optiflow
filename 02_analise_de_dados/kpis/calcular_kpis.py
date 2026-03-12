"""
OptiFlow Logística Inteligente
==============================
Script: calcular_kpis.py
Módulo: KPIs — Indicadores-Chave de Desempenho
Descrição: Carrega o dataset logístico e calcula os principais KPIs
           operacionais da OptiFlow, exibindo os resultados no console.

KPIs calculados:
    1. Faturamento mensal (R$)
    2. Tempo médio de entrega (min)
    3. Custo médio por entrega (R$)
    4. Ticket médio dos pedidos (R$)
    5. Custo médio por km (R$/km)
    6. Taxa de entregas no prazo (%)
    7. Performance por região
    8. Performance por motorista (Top 5)

Uso:
    python calcular_kpis.py

Dependências:
    pip install pandas numpy
"""

import os
import pandas as pd
import numpy as np


# ─────────────────────────────────────────────
# CONFIGURAÇÕES
# ─────────────────────────────────────────────

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
# Tenta carregar dados limpos; usa brutos se o limpo não existir
CLEAN_PATH  = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica_limpo.csv")
RAW_PATH    = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica.csv")

PRAZO_MAX_MINUTOS = 180  # Entrega "no prazo" se tempo_entrega <= 180 min


# ─────────────────────────────────────────────
# FUNÇÕES AUXILIARES
# ─────────────────────────────────────────────

def carregar_dados() -> pd.DataFrame:
    """Carrega o dataset (limpo ou bruto) e prepara as colunas."""
    if os.path.exists(CLEAN_PATH):
        caminho = CLEAN_PATH
    else:
        print("[AVISO] Dataset limpo não encontrado. Usando dataset bruto.")
        caminho = RAW_PATH

    df = pd.read_csv(caminho, encoding="utf-8")
    df["data_pedido"] = pd.to_datetime(df["data_pedido"], errors="coerce")
    df["ano_mes"] = df["data_pedido"].dt.to_period("M").astype(str)

    # Garantir presença da coluna entrega_no_prazo
    if "entrega_no_prazo" not in df.columns:
        df["entrega_no_prazo"] = df["tempo_entrega"] <= PRAZO_MAX_MINUTOS

    print(f"[OK] {len(df)} registros carregados de: {os.path.basename(caminho)}")
    return df


def formatar_brl(valor: float) -> str:
    """Formata um valor como moeda brasileira (R$ 1.234,56)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def separador(titulo: str, largura: int = 55) -> None:
    """Imprime um separador visual com título."""
    print("\n" + "─" * largura)
    print(f"  {titulo}")
    print("─" * largura)


# ─────────────────────────────────────────────
# FUNÇÕES DE KPI
# ─────────────────────────────────────────────

def kpi_faturamento_mensal(df: pd.DataFrame) -> pd.DataFrame:
    """
    KPI 1: Faturamento mensal total (soma dos valores dos pedidos por mês).
    """
    separador("KPI 1 — FATURAMENTO MENSAL")

    faturamento = (
        df.groupby("ano_mes")["valor_pedido"]
        .agg(total_pedidos="count", faturamento_total="sum", ticket_medio="mean")
        .reset_index()
    )
    faturamento["faturamento_total"] = faturamento["faturamento_total"].round(2)
    faturamento["ticket_medio"]      = faturamento["ticket_medio"].round(2)

    for _, row in faturamento.iterrows():
        print(f"  {row['ano_mes']} | {row['total_pedidos']:>3} pedidos | "
              f"Fat.: {formatar_brl(row['faturamento_total'])} | "
              f"Ticket Médio: {formatar_brl(row['ticket_medio'])}")

    total_geral = df["valor_pedido"].sum()
    media_mensal = faturamento["faturamento_total"].mean()

    print(f"\n  Faturamento Total Anual : {formatar_brl(total_geral)}")
    print(f"  Faturamento Médio Mensal: {formatar_brl(media_mensal)}")

    return faturamento


def kpi_tempo_medio_entrega(df: pd.DataFrame) -> dict:
    """
    KPI 2: Tempo médio de entrega global e por região (em minutos).
    """
    separador("KPI 2 — TEMPO MÉDIO DE ENTREGA")

    tempo_geral = df["tempo_entrega"].mean()
    tempo_mediano = df["tempo_entrega"].median()

    print(f"  Tempo Médio Global  : {tempo_geral:.1f} min")
    print(f"  Tempo Mediano Global: {tempo_mediano:.1f} min")

    print("\n  Por região:")
    tempo_por_regiao = (
        df.groupby("regiao_cliente")["tempo_entrega"]
        .agg(["mean", "median", "min", "max"])
        .round(1)
        .reset_index()
    )
    for _, row in tempo_por_regiao.iterrows():
        print(f"    {row['regiao_cliente']:<10} | Média: {row['mean']:>5.1f} min | "
              f"Mediana: {row['median']:>5.1f} min | "
              f"Min: {row['min']:>4.1f} | Max: {row['max']:>5.1f}")

    return {
        "tempo_medio_global": round(tempo_geral, 1),
        "tempo_mediano_global": round(tempo_mediano, 1),
    }


def kpi_custo_medio_entrega(df: pd.DataFrame) -> dict:
    """
    KPI 3: Custo médio por entrega (global e por região).
    """
    separador("KPI 3 — CUSTO MÉDIO POR ENTREGA")

    custo_medio = df["custo_entrega"].mean()
    custo_total = df["custo_entrega"].sum()

    print(f"  Custo Médio por Entrega: {formatar_brl(custo_medio)}")
    print(f"  Custo Total de Entregas: {formatar_brl(custo_total)}")

    print("\n  Custo médio por região:")
    custo_por_regiao = (
        df.groupby("regiao_cliente")["custo_entrega"]
        .agg(["mean", "sum", "count"])
        .round(2)
        .reset_index()
    )
    for _, row in custo_por_regiao.iterrows():
        print(f"    {row['regiao_cliente']:<10} | Média: {formatar_brl(row['mean'])} | "
              f"Total: {formatar_brl(row['sum'])} | Entregas: {int(row['count'])}")

    return {
        "custo_medio_global": round(custo_medio, 2),
        "custo_total": round(custo_total, 2),
    }


def kpi_taxa_no_prazo(df: pd.DataFrame) -> dict:
    """
    KPI 4: Taxa de entregas no prazo (tempo <= PRAZO_MAX_MINUTOS).
    """
    separador(f"KPI 4 — TAXA DE ENTREGAS NO PRAZO (≤ {PRAZO_MAX_MINUTOS} min)")

    total = len(df)
    no_prazo = df["entrega_no_prazo"].sum()
    atrasadas = total - no_prazo
    taxa = (no_prazo / total) * 100

    print(f"  Total de entregas  : {total}")
    print(f"  No prazo           : {no_prazo}  ({taxa:.1f}%)")
    print(f"  Atrasadas          : {atrasadas}  ({100 - taxa:.1f}%)")

    print("\n  Taxa no prazo por região:")
    taxa_regiao = (
        df.groupby("regiao_cliente")["entrega_no_prazo"]
        .agg(["sum", "count"])
        .reset_index()
    )
    taxa_regiao["taxa_pct"] = (taxa_regiao["sum"] / taxa_regiao["count"] * 100).round(1)
    for _, row in taxa_regiao.iterrows():
        print(f"    {row['regiao_cliente']:<10} | {row['taxa_pct']:>5.1f}% no prazo "
              f"({int(row['sum'])}/{int(row['count'])})")

    return {"taxa_no_prazo_pct": round(taxa, 1)}


def kpi_performance_motoristas(df: pd.DataFrame) -> pd.DataFrame:
    """
    KPI 5: Performance dos motoristas (Top 10 por valor entregue).
    """
    separador("KPI 5 — PERFORMANCE DE MOTORISTAS (Top 10)")

    perf = (
        df.groupby("id_motorista")
        .agg(
            total_entregas=("id_pedido", "count"),
            faturamento=("valor_pedido", "sum"),
            custo_total=("custo_entrega", "sum"),
            tempo_medio=("tempo_entrega", "mean"),
            entregas_no_prazo=("entrega_no_prazo", "sum"),
        )
        .reset_index()
    )
    perf["taxa_prazo_pct"]  = (perf["entregas_no_prazo"] / perf["total_entregas"] * 100).round(1)
    perf["faturamento"]     = perf["faturamento"].round(2)
    perf["custo_total"]     = perf["custo_total"].round(2)
    perf["tempo_medio"]     = perf["tempo_medio"].round(1)
    perf = perf.sort_values("faturamento", ascending=False).head(10)

    print(f"  {'Motorista':<12} | {'Entregas':>8} | {'Faturamento':>14} | "
          f"{'Custo Total':>12} | {'T.Médio':>8} | {'% Prazo':>8}")
    print("  " + "-" * 75)
    for _, row in perf.iterrows():
        print(f"  {row['id_motorista']:<12} | {int(row['total_entregas']):>8} | "
              f"{formatar_brl(row['faturamento']):>14} | "
              f"{formatar_brl(row['custo_total']):>12} | "
              f"{row['tempo_medio']:>6.1f}m | "
              f"{row['taxa_prazo_pct']:>6.1f}%")

    return perf


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    """Executa todos os KPIs e exibe o painel no console."""
    print("=" * 55)
    print("  OptiFlow — Painel de KPIs Logísticos")
    print("=" * 55)

    df = carregar_dados()

    # Calcular todos os KPIs
    faturamento_mensal  = kpi_faturamento_mensal(df)
    tempo_info          = kpi_tempo_medio_entrega(df)
    custo_info          = kpi_custo_medio_entrega(df)
    prazo_info          = kpi_taxa_no_prazo(df)
    perf_motoristas     = kpi_performance_motoristas(df)

    # Resumo Executivo
    separador("RESUMO EXECUTIVO — OPTIFLOW KPIs")
    print(f"  Faturamento Total       : {formatar_brl(df['valor_pedido'].sum())}")
    print(f"  Custo Total de Entregas : {formatar_brl(df['custo_entrega'].sum())}")
    print(f"  Tempo Médio de Entrega  : {tempo_info['tempo_medio_global']} min")
    print(f"  Custo Médio por Entrega : {formatar_brl(custo_info['custo_medio_global'])}")
    print(f"  Taxa de Entregas no Prazo: {prazo_info['taxa_no_prazo_pct']}%")
    print(f"  Total de Pedidos        : {len(df)}")
    print(f"  Período Analisado       : {df['data_pedido'].min().date()} a {df['data_pedido'].max().date()}")
    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()
