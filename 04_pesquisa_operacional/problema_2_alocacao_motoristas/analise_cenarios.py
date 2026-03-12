"""
==============================================================================
OptiFlow — Análise de Cenários: Alocação de Motoristas por Região
Disciplina: Pesquisa Operacional
==============================================================================
Objetivo: Avaliar como diferentes configurações operacionais impactam
          a eficiência da alocação de motoristas às regiões de entrega.

Cenários analisados:
  1. Baseline (parâmetros originais)
  2. Redução de 30% nas horas disponíveis (alta ausência)
  3. Aumento de 40% na demanda mínima por região
  4. Restrição de experiência elevada (apenas motoristas nível 3)
  5. Frota reduzida (apenas 6 motoristas disponíveis)

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

# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÃO BASE: resolver alocação com parâmetros customizáveis
# ─────────────────────────────────────────────────────────────────────────────

def resolver_alocacao(
    motoristas: dict,
    regioes: dict,
    eficiencia_df: pd.DataFrame,
    horas_necessarias_df: pd.DataFrame,
    regioes_max_por_motorista: int,
    nome_cenario: str = "Cenário"
) -> dict:
    """
    Resolve o modelo PLI de alocação de motoristas por região.

    Returns:
        Dicionário com: status, eficiencia_total, motoristas_alocados,
                        demanda_atendida, detalhes por região
    """
    nomes_mot = list(motoristas.keys())
    nomes_reg = list(regioes.keys())

    # Garantir que DataFrames contenham apenas os motoristas/regiões do cenário
    eff  = eficiencia_df.loc[nomes_mot, nomes_reg]
    hora = horas_necessarias_df.loc[nomes_mot, nomes_reg]

    prob = pulp.LpProblem(f"Alocacao_{nome_cenario}", pulp.LpMaximize)

    x = pulp.LpVariable.dicts(
        "x", [(m, r) for m in nomes_mot for r in nomes_reg], cat="Binary"
    )

    # Objetivo
    prob += pulp.lpSum(
        eff.loc[m, r] * motoristas[m]["horas_disponiveis"] * x[(m, r)]
        for m in nomes_mot for r in nomes_reg
    )

    # Restrições
    for m in nomes_mot:
        prob += pulp.lpSum(hora.loc[m, r] * x[(m, r)] for r in nomes_reg) <= motoristas[m]["horas_disponiveis"]

    for r in nomes_reg:
        prob += pulp.lpSum(
            eff.loc[m, r] * motoristas[m]["horas_disponiveis"] * x[(m, r)] for m in nomes_mot
        ) >= regioes[r]["demanda_minima"]

    for r in nomes_reg:
        prob += pulp.lpSum(x[(m, r)] for m in nomes_mot) <= regioes[r]["max_motoristas"]

    for m in nomes_mot:
        for r in nomes_reg:
            hab = 1 if motoristas[m]["nivel_experiencia"] >= regioes[r]["nivel_experiencia_min"] else 0
            prob += x[(m, r)] <= hab

    for m in nomes_mot:
        prob += pulp.lpSum(x[(m, r)] for r in nomes_reg) <= regioes_max_por_motorista

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    status = pulp.LpStatus[prob.status]
    eff_total = pulp.value(prob.objective) if status == "Optimal" else None

    mot_alocados = 0
    demanda_por_regiao = {}

    if status == "Optimal":
        mot_alocados = sum(
            1 for m in nomes_mot
            if any(pulp.value(x[(m, r)]) == 1 for r in nomes_reg)
        )
        for r in nomes_reg:
            d = sum(
                eff.loc[m, r] * motoristas[m]["horas_disponiveis"] * (pulp.value(x[(m, r)]) or 0)
                for m in nomes_mot
            )
            demanda_por_regiao[r] = round(d, 1)

    return {
        "cenario":            nome_cenario,
        "status":             status,
        "eficiencia_total":   round(eff_total, 1) if eff_total else None,
        "motoristas_alocados": mot_alocados,
        "demanda_por_regiao": demanda_por_regiao,
        "total_motoristas":   len(nomes_mot),
    }


# ─────────────────────────────────────────────────────────────────────────────
# DADOS BASE
# ─────────────────────────────────────────────────────────────────────────────

def dados_base():
    np.random.seed(42)

    motoristas = {
        "M001": {"horas_disponiveis": 8.0, "nivel_experiencia": 3},
        "M002": {"horas_disponiveis": 6.0, "nivel_experiencia": 2},
        "M003": {"horas_disponiveis": 7.0, "nivel_experiencia": 3},
        "M004": {"horas_disponiveis": 5.0, "nivel_experiencia": 1},
        "M005": {"horas_disponiveis": 8.0, "nivel_experiencia": 2},
        "M006": {"horas_disponiveis": 4.0, "nivel_experiencia": 1},
        "M007": {"horas_disponiveis": 7.0, "nivel_experiencia": 3},
        "M008": {"horas_disponiveis": 6.0, "nivel_experiencia": 2},
        "M009": {"horas_disponiveis": 8.0, "nivel_experiencia": 2},
        "M010": {"horas_disponiveis": 5.0, "nivel_experiencia": 1},
    }

    regioes = {
        "Centro": {"demanda_minima": 12, "max_motoristas": 3, "nivel_experiencia_min": 2},
        "Norte":  {"demanda_minima": 10, "max_motoristas": 2, "nivel_experiencia_min": 1},
        "Sul":    {"demanda_minima": 11, "max_motoristas": 2, "nivel_experiencia_min": 2},
        "Leste":  {"demanda_minima":  9, "max_motoristas": 2, "nivel_experiencia_min": 1},
        "Oeste":  {"demanda_minima": 10, "max_motoristas": 2, "nivel_experiencia_min": 1},
    }

    nomes_mot = list(motoristas.keys())
    nomes_reg = list(regioes.keys())

    np.random.seed(7)
    eficiencia = pd.DataFrame(
        np.random.uniform(2.0, 5.0, size=(len(nomes_mot), len(nomes_reg))),
        index=nomes_mot, columns=nomes_reg
    ).round(2)

    np.random.seed(3)
    horas_nec = pd.DataFrame(
        np.random.uniform(2.0, 5.0, size=(len(nomes_mot), len(nomes_reg))),
        index=nomes_mot, columns=nomes_reg
    ).round(1)

    return motoristas, regioes, eficiencia, horas_nec


# ─────────────────────────────────────────────────────────────────────────────
# DEFINIÇÃO DOS CENÁRIOS
# ─────────────────────────────────────────────────────────────────────────────

def definir_cenarios():
    import copy
    motoristas_base, regioes_base, eff, horas = dados_base()

    cenarios = []

    # C1 — Baseline
    cenarios.append({
        "motoristas":   copy.deepcopy(motoristas_base),
        "regioes":      copy.deepcopy(regioes_base),
        "eficiencia_df": eff, "horas_necessarias_df": horas,
        "regioes_max_por_motorista": 2,
        "nome_cenario": "C1 - Baseline"
    })

    # C2 — Redução de 30% nas horas disponíveis
    mot_c2 = copy.deepcopy(motoristas_base)
    for m in mot_c2:
        mot_c2[m]["horas_disponiveis"] = round(mot_c2[m]["horas_disponiveis"] * 0.70, 1)
    cenarios.append({
        "motoristas": mot_c2, "regioes": copy.deepcopy(regioes_base),
        "eficiencia_df": eff, "horas_necessarias_df": horas,
        "regioes_max_por_motorista": 2, "nome_cenario": "C2 - Redução de Horas (-30%)"
    })

    # C3 — Aumento de 40% na demanda
    reg_c3 = copy.deepcopy(regioes_base)
    for r in reg_c3:
        reg_c3[r]["demanda_minima"] = int(reg_c3[r]["demanda_minima"] * 1.40)
    cenarios.append({
        "motoristas": copy.deepcopy(motoristas_base), "regioes": reg_c3,
        "eficiencia_df": eff, "horas_necessarias_df": horas,
        "regioes_max_por_motorista": 2, "nome_cenario": "C3 - Alta Demanda (+40%)"
    })

    # C4 — Apenas motoristas nível 3
    mot_c4 = {m: v for m, v in motoristas_base.items() if v["nivel_experiencia"] == 3}
    cenarios.append({
        "motoristas": mot_c4, "regioes": copy.deepcopy(regioes_base),
        "eficiencia_df": eff.loc[list(mot_c4.keys())],
        "horas_necessarias_df": horas.loc[list(mot_c4.keys())],
        "regioes_max_por_motorista": 2, "nome_cenario": "C4 - Somente Nível 3"
    })

    # C5 — Frota reduzida (6 motoristas, excluir M004, M006, M010, M008)
    mot_c5 = {m: v for m, v in motoristas_base.items() if m not in ["M004", "M006", "M008", "M010"]}
    cenarios.append({
        "motoristas": mot_c5, "regioes": copy.deepcopy(regioes_base),
        "eficiencia_df": eff.loc[list(mot_c5.keys())],
        "horas_necessarias_df": horas.loc[list(mot_c5.keys())],
        "regioes_max_por_motorista": 3, "nome_cenario": "C5 - Frota Reduzida (6 mot.)"
    })

    return cenarios


# ─────────────────────────────────────────────────────────────────────────────
# VISUALIZAÇÃO
# ─────────────────────────────────────────────────────────────────────────────

def gerar_graficos(resultados: list, pasta_saida: str):
    df = pd.DataFrame([
        {"cenario": r["cenario"], "eficiencia_total": r["eficiencia_total"],
         "motoristas_alocados": r["motoristas_alocados"], "status": r["status"]}
        for r in resultados
    ])
    df_ok = df[df["status"] == "Optimal"].copy()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Análise de Cenários — Alocação de Motoristas (OptiFlow)", fontweight="bold")

    cores = ["#1565C0", "#2E7D32", "#E65100", "#6A1B9A", "#00838F"]
    labels = [c.split(" - ")[0] for c in df_ok["cenario"]]

    # Eficiência total por cenário
    bars1 = ax1.bar(labels, df_ok["eficiencia_total"], color=cores[:len(df_ok)])
    ax1.set_title("Eficiência Total (Pedidos Estimados)")
    ax1.set_ylabel("Pedidos estimados")
    for bar, val in zip(bars1, df_ok["eficiencia_total"]):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                 f"{val:.0f}", ha="center", fontweight="bold")

    # Motoristas alocados por cenário
    bars2 = ax2.bar(labels, df_ok["motoristas_alocados"], color=cores[:len(df_ok)])
    ax2.set_title("Motoristas Alocados por Cenário")
    ax2.set_ylabel("Motoristas alocados")
    ax2.set_ylim(0, 12)
    for bar, val in zip(bars2, df_ok["motoristas_alocados"]):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                 str(int(val)), ha="center", fontweight="bold")

    plt.tight_layout()
    caminho = os.path.join(pasta_saida, "analise_cenarios_motoristas.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✅ Gráfico salvo: {caminho}")


# ─────────────────────────────────────────────────────────────────────────────
# RELATÓRIO
# ─────────────────────────────────────────────────────────────────────────────

def imprimir_comparativo(resultados: list):
    print("\n" + "=" * 80)
    print("  ANÁLISE COMPARATIVA DE CENÁRIOS — Alocação de Motoristas")
    print("=" * 80)
    print(f"  {'Cenário':<35} {'Status':<10} {'Efic. Total':>12} {'Mot. Alocados':>14}")
    print("-" * 80)

    for r in resultados:
        eff_str = f"{r['eficiencia_total']:.1f} ped" if r["eficiencia_total"] else "N/A"
        print(f"  {r['cenario']:<35} {r['status']:<10} {eff_str:>12} {r['motoristas_alocados']:>14}")

    baseline = next((r for r in resultados if "Baseline" in r["cenario"]), None)
    if baseline and baseline["eficiencia_total"]:
        print("\n  Variação em relação ao Baseline:")
        for r in resultados:
            if r["eficiencia_total"] and "Baseline" not in r["cenario"]:
                var = ((r["eficiencia_total"] - baseline["eficiencia_total"]) / baseline["eficiencia_total"]) * 100
                sinal = "▲" if var > 0 else "▼"
                print(f"  {r['cenario']:<35}: {sinal} {abs(var):.1f}% em eficiência")

    print("=" * 80)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n  OptiFlow — Análise de Cenários: Alocação de Motoristas")
    print("  " + "─" * 55)

    cenarios = definir_cenarios()
    resultados = []

    for cfg in cenarios:
        print(f"\n  Resolvendo: {cfg['nome_cenario']}...")
        resultado = resolver_alocacao(**cfg)
        resultados.append(resultado)
        eff_str = f"{resultado['eficiencia_total']:.1f} ped" if resultado["eficiencia_total"] else "Inviável"
        print(f"    Status: {resultado['status']} | Eficiência: {eff_str}")

    imprimir_comparativo(resultados)

    # Salvar CSV
    pasta = os.path.dirname(__file__)
    df = pd.DataFrame([
        {k: v for k, v in r.items() if k != "demanda_por_regiao"}
        for r in resultados
    ])
    caminho_csv = os.path.join(pasta, "resultado_cenarios_motoristas.csv")
    df.to_csv(caminho_csv, index=False, encoding="utf-8-sig")
    print(f"\n  ✅ Resultados salvos em: {caminho_csv}")

    gerar_graficos(resultados, pasta)


if __name__ == "__main__":
    main()
