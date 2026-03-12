"""
==============================================================================
OptiFlow — Análise de Cenários: Otimização de Rotas de Entrega
Disciplina: Pesquisa Operacional
==============================================================================
Objetivo: Comparar o impacto de diferentes parâmetros operacionais na
          solução ótima do problema de otimização de rotas.

Cenários analisados:
  1. Baseline (parâmetros originais)
  2. Alta demanda (20 pedidos, +33%)
  3. Restrição severa de peso (15 kg por rota)
  4. Aumento de custos por km (+20%)
  5. Redução de rotas disponíveis (apenas 2 rotas)

Dependência: pip install pulp pandas numpy matplotlib seaborn
==============================================================================
"""

import pulp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import os
import sys

# Adicionar o diretório pai ao path para importar o módulo de otimização
sys.path.insert(0, os.path.dirname(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÃO BASE: resolver o modelo com parâmetros customizáveis
# ─────────────────────────────────────────────────────────────────────────────

def resolver_cenario(
    pedidos: dict,
    rotas: dict,
    custo_por_km: dict,
    peso_maximo: float,
    distancia_maxima: float,
    paradas_maximas: int,
    nome_cenario: str = "Cenário",
    seed: int = 10
) -> dict:
    """
    Resolve o modelo PLI de otimização de rotas para um dado cenário.

    Args:
        pedidos:          Dicionário {pedido_id: {peso_kg, regiao}}
        rotas:            Dicionário {rota_id: {custo_fixo, disponivel, motorista}}
        custo_por_km:     Dicionário {regiao: custo_R$/km}
        peso_maximo:      Capacidade máxima de peso por rota (kg)
        distancia_maxima: Distância máxima por rota (km)
        paradas_maximas:  Número máximo de pedidos por rota
        nome_cenario:     Nome descritivo para relatório
        seed:             Seed para reprodutibilidade das distâncias

    Returns:
        Dicionário com: status, custo_total, rotas_ativadas, pedidos_atendidos
    """
    nomes_pedidos = list(pedidos.keys())
    nomes_rotas   = list(rotas.keys())
    n_pedidos     = len(nomes_pedidos)
    n_rotas       = len(nomes_rotas)

    # Distâncias simuladas (reprodutíveis por seed)
    np.random.seed(seed)
    distancias = pd.DataFrame(
        np.random.uniform(5, 40, size=(n_pedidos, n_rotas)),
        index=nomes_pedidos, columns=nomes_rotas
    ).round(1)

    # Custos variáveis c_ij
    custos = distancias.copy()
    for ped in nomes_pedidos:
        reg = pedidos[ped]["regiao"]
        custos.loc[ped] = distancias.loc[ped] * custo_por_km.get(reg, 1.30)

    # Construir modelo
    prob = pulp.LpProblem(f"OptiFlow_{nome_cenario}", pulp.LpMinimize)

    x = pulp.LpVariable.dicts(
        "x", [(i, j) for i in nomes_pedidos for j in nomes_rotas], cat="Binary"
    )
    y = pulp.LpVariable.dicts("y", nomes_rotas, cat="Binary")

    # Função Objetivo
    prob += (
        pulp.lpSum(rotas[j]["custo_fixo"] * y[j] for j in nomes_rotas) +
        pulp.lpSum(custos.loc[i, j] * x[(i, j)] for i in nomes_pedidos for j in nomes_rotas)
    )

    # Restrições
    for i in nomes_pedidos:
        prob += pulp.lpSum(x[(i, j)] for j in nomes_rotas) == 1

    for j in nomes_rotas:
        prob += pulp.lpSum(pedidos[i]["peso_kg"] * x[(i, j)] for i in nomes_pedidos) <= peso_maximo
        prob += pulp.lpSum(distancias.loc[i, j] * x[(i, j)] for i in nomes_pedidos) <= distancia_maxima
        prob += pulp.lpSum(x[(i, j)] for i in nomes_pedidos) <= paradas_maximas

    for i in nomes_pedidos:
        for j in nomes_rotas:
            prob += x[(i, j)] <= y[j]

    for j in nomes_rotas:
        prob += y[j] <= (1 if rotas[j]["disponivel"] else 0)

    # Resolver
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    status = pulp.LpStatus[prob.status]
    custo  = pulp.value(prob.objective) if status == "Optimal" else float("inf")
    rotas_ativas   = sum(1 for j in nomes_rotas if pulp.value(y[j]) == 1) if status == "Optimal" else 0
    pedidos_alocados = sum(
        1 for i in nomes_pedidos for j in nomes_rotas
        if pulp.value(x[(i, j)]) == 1
    ) if status == "Optimal" else 0

    return {
        "cenario":           nome_cenario,
        "status":            status,
        "custo_total":       round(custo, 2) if custo != float("inf") else None,
        "rotas_ativadas":    rotas_ativas,
        "pedidos_atendidos": pedidos_alocados,
        "peso_maximo":       peso_maximo,
        "distancia_maxima":  distancia_maxima,
        "paradas_maximas":   paradas_maximas,
    }


# ─────────────────────────────────────────────────────────────────────────────
# DEFINIÇÃO DOS CENÁRIOS
# ─────────────────────────────────────────────────────────────────────────────

def definir_cenarios():
    """Retorna lista de configurações de cada cenário a analisar."""
    regioes = ["Centro", "Norte", "Sul", "Leste", "Oeste"]

    # Dataset base (15 pedidos)
    pedidos_base = {
        f"P{i:03d}": {
            "peso_kg": round(np.random.uniform(2, 10), 1),
            "regiao": regioes[i % 5]
        }
        for i in range(1, 16)
    }

    # Dataset alta demanda (20 pedidos)
    pedidos_alta_demanda = {
        f"P{i:03d}": {
            "peso_kg": round(np.random.uniform(2, 10), 1),
            "regiao": regioes[i % 5]
        }
        for i in range(1, 21)
    }

    rotas_base = {
        "R1": {"motorista": "M001", "disponivel": True,  "custo_fixo": 25.0},
        "R2": {"motorista": "M003", "disponivel": True,  "custo_fixo": 28.0},
        "R3": {"motorista": "M005", "disponivel": True,  "custo_fixo": 22.0},
        "R4": {"motorista": "M007", "disponivel": False, "custo_fixo": 30.0},
        "R5": {"motorista": "M009", "disponivel": True,  "custo_fixo": 26.0},
    }

    rotas_reduzidas = {
        "R1": {"motorista": "M001", "disponivel": True,  "custo_fixo": 25.0},
        "R2": {"motorista": "M003", "disponivel": True,  "custo_fixo": 28.0},
        "R3": {"motorista": "M005", "disponivel": False, "custo_fixo": 22.0},
        "R4": {"motorista": "M007", "disponivel": False, "custo_fixo": 30.0},
        "R5": {"motorista": "M009", "disponivel": False, "custo_fixo": 26.0},
    }

    custo_base  = {"Centro": 1.20, "Norte": 1.50, "Sul": 1.40, "Leste": 1.30, "Oeste": 1.35}
    custo_alto  = {k: round(v * 1.20, 3) for k, v in custo_base.items()}

    np.random.seed(99)  # Garantir pedidos reprodutíveis

    cenarios = [
        {
            "pedidos": pedidos_base, "rotas": rotas_base,
            "custo_por_km": custo_base, "peso_maximo": 20.0,
            "distancia_maxima": 60.0, "paradas_maximas": 5,
            "nome_cenario": "C1 - Baseline"
        },
        {
            "pedidos": pedidos_alta_demanda, "rotas": rotas_base,
            "custo_por_km": custo_base, "peso_maximo": 20.0,
            "distancia_maxima": 60.0, "paradas_maximas": 5,
            "nome_cenario": "C2 - Alta Demanda (+33%)"
        },
        {
            "pedidos": pedidos_base, "rotas": rotas_base,
            "custo_por_km": custo_base, "peso_maximo": 15.0,
            "distancia_maxima": 60.0, "paradas_maximas": 5,
            "nome_cenario": "C3 - Restrição de Peso (15 kg)"
        },
        {
            "pedidos": pedidos_base, "rotas": rotas_base,
            "custo_por_km": custo_alto, "peso_maximo": 20.0,
            "distancia_maxima": 60.0, "paradas_maximas": 5,
            "nome_cenario": "C4 - Aumento de Custos (+20%)"
        },
        {
            "pedidos": pedidos_base, "rotas": rotas_reduzidas,
            "custo_por_km": custo_base, "peso_maximo": 20.0,
            "distancia_maxima": 60.0, "paradas_maximas": 8,
            "nome_cenario": "C5 - Apenas 2 Rotas Disponíveis"
        },
    ]
    return cenarios


# ─────────────────────────────────────────────────────────────────────────────
# RELATÓRIO E VISUALIZAÇÃO
# ─────────────────────────────────────────────────────────────────────────────

def gerar_graficos(df_resultados: pd.DataFrame, pasta_saida: str):
    """Gera gráficos comparativos entre cenários."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Análise de Cenários — Otimização de Rotas (OptiFlow)", fontweight="bold")

    df_ok = df_resultados[df_resultados["status"] == "Optimal"].copy()
    cores = ["#2196F3", "#4CAF50", "#FF9800", "#F44336", "#9C27B0"]

    # Gráfico 1: Custo total por cenário
    ax1 = axes[0]
    barras = ax1.bar(range(len(df_ok)), df_ok["custo_total"], color=cores[:len(df_ok)])
    ax1.set_xticks(range(len(df_ok)))
    ax1.set_xticklabels([c.split(" - ")[0] for c in df_ok["cenario"]], fontsize=10)
    ax1.set_ylabel("Custo Total (R$)")
    ax1.set_title("Custo Total por Cenário")
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"R$ {x:,.0f}"))
    for bar, val in zip(barras, df_ok["custo_total"]):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                 f"R$ {val:,.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

    # Gráfico 2: Rotas ativadas por cenário
    ax2 = axes[1]
    ax2.bar(range(len(df_ok)), df_ok["rotas_ativadas"], color=cores[:len(df_ok)])
    ax2.set_xticks(range(len(df_ok)))
    ax2.set_xticklabels([c.split(" - ")[0] for c in df_ok["cenario"]], fontsize=10)
    ax2.set_ylabel("Número de Rotas Ativadas")
    ax2.set_title("Rotas Ativadas por Cenário")
    ax2.set_ylim(0, 6)

    plt.tight_layout()
    caminho = os.path.join(pasta_saida, "analise_cenarios_rotas.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✅ Gráfico salvo: {caminho}")


def imprimir_tabela_comparativa(resultados: list):
    """Imprime tabela comparativa de todos os cenários."""
    print("\n" + "=" * 80)
    print("  ANÁLISE COMPARATIVA DE CENÁRIOS — Otimização de Rotas")
    print("=" * 80)
    print(f"  {'Cenário':<35} {'Status':<10} {'Custo Total':>12} {'Rotas':>6} {'Pedidos':>8}")
    print("-" * 80)

    for r in resultados:
        custo_str = f"R$ {r['custo_total']:,.2f}" if r["custo_total"] else "N/A"
        print(
            f"  {r['cenario']:<35} {r['status']:<10} "
            f"{custo_str:>12} {r['rotas_ativadas']:>6} {r['pedidos_atendidos']:>8}"
        )

    # Variação em relação ao baseline
    baseline = next((r for r in resultados if "Baseline" in r["cenario"]), None)
    if baseline and baseline["custo_total"]:
        print("\n" + "-" * 80)
        print("  Variação em relação ao Baseline:")
        for r in resultados:
            if r["custo_total"] and "Baseline" not in r["cenario"]:
                variacao = ((r["custo_total"] - baseline["custo_total"]) / baseline["custo_total"]) * 100
                sinal = "▲" if variacao > 0 else "▼"
                print(f"  {r['cenario']:<35}: {sinal} {abs(variacao):.1f}%")

    print("=" * 80)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n  OptiFlow — Análise de Cenários: Otimização de Rotas")
    print("  " + "─" * 55)

    cenarios = definir_cenarios()
    resultados = []

    for cfg in cenarios:
        print(f"\n  Resolvendo: {cfg['nome_cenario']}...")
        resultado = resolver_cenario(**cfg)
        resultados.append(resultado)
        status = resultado["status"]
        custo  = f"R$ {resultado['custo_total']:,.2f}" if resultado["custo_total"] else "Inviável"
        print(f"    Status: {status} | Custo: {custo}")

    imprimir_tabela_comparativa(resultados)

    # Salvar resultados
    df = pd.DataFrame(resultados)
    pasta = os.path.dirname(__file__)
    caminho_csv = os.path.join(pasta, "resultado_cenarios.csv")
    df.to_csv(caminho_csv, index=False, encoding="utf-8-sig")
    print(f"\n  ✅ Resultados salvos em: {caminho_csv}")

    gerar_graficos(df, pasta)


if __name__ == "__main__":
    main()
