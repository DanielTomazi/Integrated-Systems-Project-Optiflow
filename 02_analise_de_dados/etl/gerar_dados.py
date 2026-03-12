"""
OptiFlow Logística Inteligente
==============================
Script: gerar_dados.py
Módulo: ETL — Geração de Dados Simulados
Descrição: Gera um dataset logístico sintético com 200 registros e salva em CSV.

Uso:
    python gerar_dados.py

Dependências:
    pip install pandas numpy
"""

import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


# ─────────────────────────────────────────────
# CONFIGURAÇÕES
# ─────────────────────────────────────────────

SEED = 42          # Semente para reprodutibilidade
NUM_PEDIDOS = 200  # Quantidade de registros a gerar

# Caminho de saída relativo ao script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica.csv")


# ─────────────────────────────────────────────
# PARÂMETROS DO DATASET LOGÍSTICO
# ─────────────────────────────────────────────

REGIOES = ["Centro", "Norte", "Sul", "Leste", "Oeste"]
MOTORISTAS = [f"M{str(i).zfill(3)}" for i in range(1, 16)]  # M001 a M015

# Custo por km (R$/km) — varia por região
CUSTO_POR_KM = {
    "Centro": 1.20,
    "Norte":  1.45,
    "Sul":    1.30,
    "Leste":  1.50,
    "Oeste":  1.35,
}

# Velocidade média (km/h) — afeta o tempo de entrega
VELOCIDADE_MEDIA_KMH = {
    "Centro": 25,
    "Norte":  20,
    "Sul":    22,
    "Leste":  18,
    "Oeste":  21,
}


def gerar_data_pedidos(num_pedidos: int, ano: int = 2025) -> list:
    """
    Gera uma lista de datas de pedidos distribuídas ao longo de um ano,
    excluindo domingos e feriados simplificados.
    """
    data_inicio = datetime(ano, 1, 1)
    datas = []
    tentativas = 0

    while len(datas) < num_pedidos and tentativas < 10000:
        delta = timedelta(days=np.random.randint(0, 365))
        data_candidata = data_inicio + delta
        # Excluir domingos (weekday 6)
        if data_candidata.weekday() != 6:
            datas.append(data_candidata.strftime("%Y-%m-%d"))
        tentativas += 1

    datas.sort()
    return datas[:num_pedidos]


def gerar_dataset(num_pedidos: int, seed: int = SEED) -> pd.DataFrame:
    """
    Gera um DataFrame com dados logísticos simulados.

    Colunas geradas:
        id_pedido        : identificador único (P001, P002, ...)
        regiao_cliente   : região de entrega (Centro, Norte, Sul, Leste, Oeste)
        distancia_entrega: distância em km (distribuição normal por região)
        tempo_entrega    : tempo em minutos calculado com base na distância e velocidade + ruído
        custo_entrega    : custo em R$ baseado na distância × custo/km + taxa fixa
        id_motorista     : motorista responsável (M001 a M015)
        valor_pedido     : valor do pedido em R$ (correlacionado parcialmente com distância)
        data_pedido      : data do pedido em formato YYYY-MM-DD
    """
    np.random.seed(seed)

    # IDs dos pedidos
    ids_pedidos = [f"P{str(i).zfill(3)}" for i in range(1, num_pedidos + 1)]

    # Região: distribuição não uniforme (Centro tem mais pedidos)
    pesos_regiao = [0.30, 0.20, 0.20, 0.15, 0.15]
    regioes = np.random.choice(REGIOES, size=num_pedidos, p=pesos_regiao)

    # Distância: varia por região (km)
    distancias = []
    for regiao in regioes:
        if regiao == "Centro":
            dist = max(2.0, np.random.normal(15, 7))
        elif regiao in ["Norte", "Leste"]:
            dist = max(5.0, np.random.normal(30, 10))
        else:
            dist = max(3.0, np.random.normal(22, 8))
        distancias.append(round(dist, 1))

    # Tempo de entrega: distância / velocidade_media + ruído de trânsito (em minutos)
    tempos = []
    for regiao, dist in zip(regioes, distancias):
        velocidade = VELOCIDADE_MEDIA_KMH[regiao]
        tempo_base = (dist / velocidade) * 60  # converter para minutos
        ruido = np.random.normal(0, 10)        # variação de ±10 min
        tempo_final = max(20, round(tempo_base + ruido))
        tempos.append(tempo_final)

    # Custo de entrega: taxa fixa + custo por km + ruído
    custos = []
    for regiao, dist in zip(regioes, distancias):
        taxa_fixa = 8.00
        custo_variavel = dist * CUSTO_POR_KM[regiao]
        ruido = np.random.normal(0, 1.5)
        custo_final = max(8.0, round(taxa_fixa + custo_variavel + ruido, 2))
        custos.append(custo_final)

    # Motorista: alocado com viés por região
    motoristas = np.random.choice(MOTORISTAS, size=num_pedidos)

    # Valor do pedido: correlacionado com distância + aleatoriedade
    valores_pedido = []
    for dist in distancias:
        valor_base = 50 + dist * 8 + np.random.normal(0, 50)
        valor_final = max(30.0, round(valor_base, 2))
        valores_pedido.append(valor_final)

    # Datas dos pedidos
    datas = gerar_data_pedidos(num_pedidos)

    # Montar o DataFrame
    df = pd.DataFrame({
        "id_pedido":         ids_pedidos,
        "regiao_cliente":    regioes,
        "distancia_entrega": distancias,
        "tempo_entrega":     tempos,
        "custo_entrega":     custos,
        "id_motorista":      motoristas,
        "valor_pedido":      valores_pedido,
        "data_pedido":       datas,
    })

    return df


def main():
    """Função principal: gera o dataset e salva em CSV."""
    print("=" * 55)
    print("  OptiFlow — Gerador de Dados Logísticos Simulados")
    print("=" * 55)

    print(f"\n[INFO] Gerando {NUM_PEDIDOS} registros com seed={SEED}...")
    df = gerar_dataset(NUM_PEDIDOS, SEED)

    # Exibir prévia dos dados
    print(f"\n[PRÉVIA] Primeiros 5 registros:")
    print(df.head().to_string(index=False))

    print(f"\n[ESTATÍSTICAS BÁSICAS]")
    print(df[["distancia_entrega", "tempo_entrega", "custo_entrega", "valor_pedido"]].describe().round(2))

    # Salvar em CSV
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

    print(f"\n[OK] Dataset salvo em: {os.path.abspath(OUTPUT_PATH)}")
    print(f"     Total de registros: {len(df)}")
    print(f"     Período: {df['data_pedido'].min()} a {df['data_pedido'].max()}")
    print(f"     Regiões: {sorted(df['regiao_cliente'].unique())}")
    print(f"     Motoristas: {df['id_motorista'].nunique()} únicos")


if __name__ == "__main__":
    main()
