"""
==============================================================================
OptiFlow — Problema 1: Otimização de Rotas de Entrega
Disciplina: Pesquisa Operacional
Método: Programação Linear Inteira (PLI) — PuLP + CBC Solver
==============================================================================
Objetivo: Minimizar o custo total de entrega atribuindo pedidos às rotas
          disponíveis, respeitando restrições de capacidade e distância.

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

np.random.seed(42)  # Reprodutibilidade

# Pedidos a entregar
PEDIDOS = {
    "P001": {"peso_kg": 5.0,  "regiao": "Centro"},
    "P002": {"peso_kg": 3.5,  "regiao": "Norte"},
    "P003": {"peso_kg": 8.0,  "regiao": "Sul"},
    "P004": {"peso_kg": 2.0,  "regiao": "Leste"},
    "P005": {"peso_kg": 6.5,  "regiao": "Oeste"},
    "P006": {"peso_kg": 4.0,  "regiao": "Centro"},
    "P007": {"peso_kg": 7.5,  "regiao": "Norte"},
    "P008": {"peso_kg": 3.0,  "regiao": "Sul"},
    "P009": {"peso_kg": 5.5,  "regiao": "Leste"},
    "P010": {"peso_kg": 2.5,  "regiao": "Oeste"},
    "P011": {"peso_kg": 9.0,  "regiao": "Centro"},
    "P012": {"peso_kg": 4.5,  "regiao": "Norte"},
    "P013": {"peso_kg": 6.0,  "regiao": "Sul"},
    "P014": {"peso_kg": 3.5,  "regiao": "Leste"},
    "P015": {"peso_kg": 5.0,  "regiao": "Oeste"},
}

# Rotas disponíveis
ROTAS = {
    "R1": {"motorista": "M001", "disponivel": True,  "custo_fixo": 25.0},
    "R2": {"motorista": "M003", "disponivel": True,  "custo_fixo": 28.0},
    "R3": {"motorista": "M005", "disponivel": True,  "custo_fixo": 22.0},
    "R4": {"motorista": "M007", "disponivel": False, "custo_fixo": 30.0},  # Indisponível
    "R5": {"motorista": "M009", "disponivel": True,  "custo_fixo": 26.0},
}

# Parâmetros do modelo
PESO_MAXIMO_POR_ROTA  = 20.0   # kg
DISTANCIA_MAXIMA      = 60.0   # km
PARADAS_MAXIMAS       = 5      # pedidos por rota

# Custo por km por região (base)
CUSTO_POR_KM = {
    "Centro": 1.20,
    "Norte":  1.50,
    "Sul":    1.40,
    "Leste":  1.30,
    "Oeste":  1.35,
}

# Distâncias simuladas de cada pedido para cada rota (km)
# Em um sistema real, seriam calculadas via API de geolocalização
np.random.seed(10)
nomes_pedidos = list(PEDIDOS.keys())
nomes_rotas   = list(ROTAS.keys())

distancias = pd.DataFrame(
    np.random.uniform(5, 40, size=(len(nomes_pedidos), len(nomes_rotas))),
    index=nomes_pedidos,
    columns=nomes_rotas
).round(1)

# Custo variável c_ij = distancia_ij * custo_por_km_da_regiao_do_pedido
custos = distancias.copy()
for pedido in nomes_pedidos:
    regiao = PEDIDOS[pedido]["regiao"]
    custo_km = CUSTO_POR_KM[regiao]
    custos.loc[pedido] = distancias.loc[pedido] * custo_km


# ─────────────────────────────────────────────────────────────────────────────
# 2. CONSTRUÇÃO DO MODELO PLI (PuLP)
# ─────────────────────────────────────────────────────────────────────────────

def construir_modelo():
    """
    Constrói o modelo de Programação Linear Inteira para otimização de rotas.
    
    Variáveis:
        x[i][j] = 1 se o pedido i é atribuído à rota j, 0 caso contrário
        y[j]    = 1 se a rota j é ativada, 0 caso contrário
    
    Returns:
        prob: Problema PuLP configurado
        x:    Dicionário de variáveis de decisão x[i][j]
        y:    Dicionário de variáveis de ativação y[j]
    """
    prob = pulp.LpProblem("OptiFlow_Otimizacao_Rotas", pulp.LpMinimize)

    # ── Variáveis de decisão ──────────────────────────────────────────────
    x = pulp.LpVariable.dicts(
        "atribuir",
        [(i, j) for i in nomes_pedidos for j in nomes_rotas],
        cat="Binary"
    )

    y = pulp.LpVariable.dicts(
        "ativar_rota",
        nomes_rotas,
        cat="Binary"
    )

    # ── Função Objetivo: Minimizar custo total ────────────────────────────
    custo_fixo_total    = pulp.lpSum(ROTAS[j]["custo_fixo"] * y[j] for j in nomes_rotas)
    custo_variavel_total = pulp.lpSum(
        custos.loc[i, j] * x[(i, j)]
        for i in nomes_pedidos
        for j in nomes_rotas
    )
    prob += custo_fixo_total + custo_variavel_total, "Custo_Total"

    # ── Restrições ────────────────────────────────────────────────────────

    # R1: Cada pedido atribuído a exatamente 1 rota
    for i in nomes_pedidos:
        prob += pulp.lpSum(x[(i, j)] for j in nomes_rotas) == 1, f"R1_pedido_{i}"

    # R2: Capacidade de peso por rota
    for j in nomes_rotas:
        prob += (
            pulp.lpSum(PEDIDOS[i]["peso_kg"] * x[(i, j)] for i in nomes_pedidos) <= PESO_MAXIMO_POR_ROTA,
            f"R2_peso_rota_{j}"
        )

    # R3: Distância máxima por rota
    for j in nomes_rotas:
        prob += (
            pulp.lpSum(distancias.loc[i, j] * x[(i, j)] for i in nomes_pedidos) <= DISTANCIA_MAXIMA,
            f"R3_distancia_rota_{j}"
        )

    # R4: Número máximo de paradas por rota
    for j in nomes_rotas:
        prob += (
            pulp.lpSum(x[(i, j)] for i in nomes_pedidos) <= PARADAS_MAXIMAS,
            f"R4_paradas_rota_{j}"
        )

    # R5: Vincular x a y (rota ativada se algum pedido atribuído)
    for i in nomes_pedidos:
        for j in nomes_rotas:
            prob += x[(i, j)] <= y[j], f"R5_link_{i}_{j}"

    # R6: Somente rotas disponíveis podem ser ativadas
    for j in nomes_rotas:
        disponivel = 1 if ROTAS[j]["disponivel"] else 0
        prob += y[j] <= disponivel, f"R6_disponibilidade_{j}"

    return prob, x, y


# ─────────────────────────────────────────────────────────────────────────────
# 3. EXECUÇÃO E RELATÓRIO
# ─────────────────────────────────────────────────────────────────────────────

def exibir_relatorio(prob, x, y):
    """Exibe o resultado da otimização de forma estruturada."""
    status = pulp.LpStatus[prob.status]
    print("=" * 65)
    print("  OPTIFLOW — RESULTADO DA OTIMIZAÇÃO DE ROTAS")
    print("=" * 65)
    print(f"\n  Status do solver: {status}")

    if status != "Optimal":
        print("  ❌ Solução ótima não encontrada.")
        return

    custo_total = pulp.value(prob.objective)
    print(f"  💰 Custo Total Mínimo: R$ {custo_total:,.2f}")

    print("\n" + "-" * 65)
    print("  ATRIBUIÇÃO DE PEDIDOS ÀS ROTAS")
    print("-" * 65)

    alocacao = {j: [] for j in nomes_rotas}
    for i in nomes_pedidos:
        for j in nomes_rotas:
            if pulp.value(x[(i, j)]) == 1:
                alocacao[j].append(i)

    for j in nomes_rotas:
        if pulp.value(y[j]) == 1:
            pedidos_rota = alocacao[j]
            peso_total   = sum(PEDIDOS[p]["peso_kg"] for p in pedidos_rota)
            dist_total   = sum(distancias.loc[p, j] for p in pedidos_rota)
            custo_rota   = ROTAS[j]["custo_fixo"] + sum(custos.loc[p, j] for p in pedidos_rota)

            print(f"\n  Rota {j} (Motorista: {ROTAS[j]['motorista']})")
            print(f"  Pedidos: {', '.join(pedidos_rota)}")
            print(f"  Peso total: {peso_total:.1f} kg / {PESO_MAXIMO_POR_ROTA:.0f} kg")
            print(f"  Distância total: {dist_total:.1f} km / {DISTANCIA_MAXIMA:.0f} km")
            print(f"  Custo da rota: R$ {custo_rota:.2f}")

    print("\n" + "-" * 65)
    print(f"  Rotas ativadas: {sum(1 for j in nomes_rotas if pulp.value(y[j]) == 1)} / {len(nomes_rotas)}")
    print(f"  Pedidos atendidos: {len(nomes_pedidos)}")
    print("=" * 65)


def salvar_resultado(x, y, caminho_saida: str = None):
    """Salva o resultado em CSV para análise posterior."""
    if caminho_saida is None:
        base = os.path.dirname(__file__)
        caminho_saida = os.path.join(base, "resultado_otimizacao.csv")

    linhas = []
    for i in nomes_pedidos:
        for j in nomes_rotas:
            if pulp.value(x[(i, j)]) == 1:
                linhas.append({
                    "pedido":    i,
                    "rota":      j,
                    "motorista": ROTAS[j]["motorista"],
                    "regiao":    PEDIDOS[i]["regiao"],
                    "peso_kg":   PEDIDOS[i]["peso_kg"],
                    "distancia_km": round(distancias.loc[i, j], 1),
                    "custo_R$":     round(custos.loc[i, j] + ROTAS[j]["custo_fixo"] / len([
                        k for k in nomes_pedidos
                        if pulp.value(x[(k, j)]) == 1
                    ]), 2),
                })

    df = pd.DataFrame(linhas)
    df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")
    print(f"\n  ✅ Resultado salvo em: {caminho_saida}")


# ─────────────────────────────────────────────────────────────────────────────
# 4. MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n  Construindo modelo de otimização PLI...")
    prob, x, y = construir_modelo()

    print(f"  Variáveis de decisão: {len(prob.variables())}")
    print(f"  Restrições: {len(prob.constraints)}")

    print("\n  Executando solver CBC (PuLP)...")
    # msg=0 suprime output verbose do solver
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    exibir_relatorio(prob, x, y)
    salvar_resultado(x, y)

    return prob, x, y


if __name__ == "__main__":
    main()
