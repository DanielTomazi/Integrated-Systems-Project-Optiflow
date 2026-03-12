"""
==============================================================================
OptiFlow — Problema 2: Alocação Ótima de Motoristas por Região
Disciplina: Pesquisa Operacional
Método: Programação Linear Inteira (PLI) — PuLP + CBC Solver
==============================================================================
Objetivo: Maximizar a eficiência operacional total alocando motoristas
          às regiões de entrega, respeitando restrições de disponibilidade,
          demanda mínima e nível de experiência.

Dependência: pip install pulp pandas numpy
==============================================================================
"""

import pulp
import pandas as pd
import numpy as np
import os

# ─────────────────────────────────────────────────────────────────────────────
# 1. DADOS DO PROBLEMA
# ─────────────────────────────────────────────────────────────────────────────

np.random.seed(42)

# Motoristas disponíveis
# nivel_experiencia: 1=baixo, 2=medio, 3=alto
MOTORISTAS = {
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

# Regiões de entrega
# nivel_experiencia_min: nível mínimo exigido do motorista
REGIOES = {
    "Centro": {"demanda_minima": 12, "max_motoristas": 3, "nivel_experiencia_min": 2},
    "Norte":  {"demanda_minima": 10, "max_motoristas": 2, "nivel_experiencia_min": 1},
    "Sul":    {"demanda_minima": 11, "max_motoristas": 2, "nivel_experiencia_min": 2},
    "Leste":  {"demanda_minima":  9, "max_motoristas": 2, "nivel_experiencia_min": 1},
    "Oeste":  {"demanda_minima": 10, "max_motoristas": 2, "nivel_experiencia_min": 1},
}

# Parâmetros globais
REGIOES_MAXIMAS_POR_MOTORISTA = 2  # Cada motorista cobre no máximo 2 regiões

# Eficiência e_mr: pedidos entregues por hora (baseado em histórico simulado)
nomes_motoristas = list(MOTORISTAS.keys())
nomes_regioes    = list(REGIOES.keys())

np.random.seed(7)
eficiencia = pd.DataFrame(
    np.random.uniform(2.0, 5.0, size=(len(nomes_motoristas), len(nomes_regioes))),
    index=nomes_motoristas,
    columns=nomes_regioes
).round(2)

# Horas necessárias t_mr: tempo médio para atender a região (baseado em distância)
np.random.seed(3)
horas_necessarias = pd.DataFrame(
    np.random.uniform(2.0, 5.0, size=(len(nomes_motoristas), len(nomes_regioes))),
    index=nomes_motoristas,
    columns=nomes_regioes
).round(1)


# ─────────────────────────────────────────────────────────────────────────────
# 2. CONSTRUÇÃO DO MODELO PLI (PuLP)
# ─────────────────────────────────────────────────────────────────────────────

def construir_modelo():
    """
    Constrói o modelo PLI de alocação de motoristas por região.

    Variável:
        x[m][r] = 1 se o motorista m é alocado à região r

    Objetivo:
        Maximizar a eficiência total (pedidos entregues / horas totais)

    Returns:
        prob: Problema PuLP configurado
        x:    Dicionário de variáveis de decisão
    """
    # Maximização → converter para minimização (PuLP default)
    prob = pulp.LpProblem("OptiFlow_Alocacao_Motoristas", pulp.LpMaximize)

    # ── Variáveis de decisão ──────────────────────────────────────────────
    x = pulp.LpVariable.dicts(
        "alocar",
        [(m, r) for m in nomes_motoristas for r in nomes_regioes],
        cat="Binary"
    )

    # ── Função Objetivo: Maximizar pedidos entregues totais ───────────────
    prob += pulp.lpSum(
        eficiencia.loc[m, r] * MOTORISTAS[m]["horas_disponiveis"] * x[(m, r)]
        for m in nomes_motoristas
        for r in nomes_regioes
    ), "Eficiencia_Total"

    # ── Restrições ────────────────────────────────────────────────────────

    # R1: Horas alocadas ≤ horas disponíveis do motorista
    for m in nomes_motoristas:
        prob += (
            pulp.lpSum(horas_necessarias.loc[m, r] * x[(m, r)] for r in nomes_regioes)
            <= MOTORISTAS[m]["horas_disponiveis"],
            f"R1_horas_{m}"
        )

    # R2: Demanda mínima atendida por região
    for r in nomes_regioes:
        prob += (
            pulp.lpSum(
                eficiencia.loc[m, r] * MOTORISTAS[m]["horas_disponiveis"] * x[(m, r)]
                for m in nomes_motoristas
            ) >= REGIOES[r]["demanda_minima"],
            f"R2_demanda_{r}"
        )

    # R3: Máximo de motoristas por região
    for r in nomes_regioes:
        prob += (
            pulp.lpSum(x[(m, r)] for m in nomes_motoristas) <= REGIOES[r]["max_motoristas"],
            f"R3_max_motoristas_{r}"
        )

    # R4: Restrição de nível de experiência
    for m in nomes_motoristas:
        for r in nomes_regioes:
            nivel_m = MOTORISTAS[m]["nivel_experiencia"]
            nivel_min_r = REGIOES[r]["nivel_experiencia_min"]
            habilitado = 1 if nivel_m >= nivel_min_r else 0
            prob += x[(m, r)] <= habilitado, f"R4_exp_{m}_{r}"

    # R5: Máximo de regiões por motorista
    for m in nomes_motoristas:
        prob += (
            pulp.lpSum(x[(m, r)] for r in nomes_regioes) <= REGIOES_MAXIMAS_POR_MOTORISTA,
            f"R5_regioes_{m}"
        )

    return prob, x


# ─────────────────────────────────────────────────────────────────────────────
# 3. EXECUÇÃO E RELATÓRIO
# ─────────────────────────────────────────────────────────────────────────────

def exibir_relatorio(prob, x):
    """Exibe o resultado da alocação de forma estruturada."""
    status = pulp.LpStatus[prob.status]
    print("=" * 65)
    print("  OPTIFLOW — RESULTADO DA ALOCAÇÃO DE MOTORISTAS")
    print("=" * 65)
    print(f"\n  Status do solver: {status}")

    if status != "Optimal":
        print("  ❌ Solução ótima não encontrada.")
        return

    eficiencia_total = pulp.value(prob.objective)
    print(f"  📦 Pedidos estimados (eficiência total): {eficiencia_total:.1f} pedidos")

    print("\n" + "-" * 65)
    print("  ALOCAÇÃO POR REGIÃO")
    print("-" * 65)

    for r in nomes_regioes:
        mot_alocados = [m for m in nomes_motoristas if pulp.value(x[(m, r)]) == 1]
        if mot_alocados:
            ped_regiao = sum(
                eficiencia.loc[m, r] * MOTORISTAS[m]["horas_disponiveis"]
                for m in mot_alocados
            )
            print(f"\n  Região: {r}")
            print(f"  Demanda mínima: {REGIOES[r]['demanda_minima']} pedidos")
            print(f"  Motoristas: {', '.join(mot_alocados)}")
            print(f"  Pedidos estimados: {ped_regiao:.1f}")
        else:
            print(f"\n  Região: {r} — ⚠️  Nenhum motorista alocado!")

    print("\n" + "-" * 65)
    print("  UTILIZAÇÃO DE MOTORISTAS")
    print("-" * 65)
    for m in nomes_motoristas:
        regioes_alocadas = [r for r in nomes_regioes if pulp.value(x[(m, r)]) == 1]
        if regioes_alocadas:
            horas_usadas = sum(horas_necessarias.loc[m, r] for r in regioes_alocadas)
            print(
                f"  {m}: Regiões: {', '.join(regioes_alocadas)} | "
                f"Horas: {horas_usadas:.1f}/{MOTORISTAS[m]['horas_disponiveis']:.0f}h"
            )

    print("\n" + "=" * 65)


def salvar_resultado(x, caminho_saida: str = None):
    """Salva o resultado da alocação em CSV."""
    if caminho_saida is None:
        base = os.path.dirname(__file__)
        caminho_saida = os.path.join(base, "resultado_alocacao.csv")

    linhas = []
    for m in nomes_motoristas:
        for r in nomes_regioes:
            if pulp.value(x[(m, r)]) == 1:
                linhas.append({
                    "motorista":          m,
                    "regiao":             r,
                    "horas_disponiveis":  MOTORISTAS[m]["horas_disponiveis"],
                    "horas_necessarias":  round(horas_necessarias.loc[m, r], 1),
                    "eficiencia_ped_h":   round(eficiencia.loc[m, r], 2),
                    "pedidos_estimados":  round(eficiencia.loc[m, r] * MOTORISTAS[m]["horas_disponiveis"], 1),
                    "nivel_experiencia":  MOTORISTAS[m]["nivel_experiencia"],
                })

    df = pd.DataFrame(linhas)
    df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")
    print(f"\n  ✅ Resultado salvo em: {caminho_saida}")


# ─────────────────────────────────────────────────────────────────────────────
# 4. MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n  Construindo modelo PLI de alocação de motoristas...")
    prob, x = construir_modelo()

    print(f"  Variáveis de decisão: {len(prob.variables())}")
    print(f"  Restrições: {len(prob.constraints)}")

    print("\n  Executando solver CBC (PuLP)...")
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    exibir_relatorio(prob, x)
    salvar_resultado(x)

    return prob, x


if __name__ == "__main__":
    main()
