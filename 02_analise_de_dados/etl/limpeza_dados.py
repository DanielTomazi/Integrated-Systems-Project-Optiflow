"""
OptiFlow Logística Inteligente
==============================
Script: limpeza_dados.py
Módulo: ETL — Limpeza e Tratamento de Dados
Descrição: Carrega o dataset logístico, realiza limpeza, validação e
           transformações e salva a versão limpa pronta para análise.

Uso:
    python limpeza_dados.py

Dependências:
    pip install pandas numpy
"""

import os
import numpy as np
import pandas as pd


# ─────────────────────────────────────────────
# CONFIGURAÇÕES DE CAMINHOS
# ─────────────────────────────────────────────

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
RAW_PATH     = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica.csv")
CLEAN_PATH   = os.path.join(SCRIPT_DIR, "..", "data", "dataset_logistica_limpo.csv")


# ─────────────────────────────────────────────
# VALORES VÁLIDOS ESPERADOS
# ─────────────────────────────────────────────

REGIOES_VALIDAS    = {"Centro", "Norte", "Sul", "Leste", "Oeste"}
DISTANCIA_MIN_KM   = 1.0
DISTANCIA_MAX_KM   = 200.0
TEMPO_MIN_MIN      = 10
TEMPO_MAX_MIN      = 600
CUSTO_MIN_BRL      = 5.0
CUSTO_MAX_BRL      = 500.0
VALOR_MIN_BRL      = 10.0
VALOR_MAX_BRL      = 5000.0


# ─────────────────────────────────────────────
# FUNÇÕES DE LIMPEZA
# ─────────────────────────────────────────────

def carregar_dados(caminho: str) -> pd.DataFrame:
    """Carrega o dataset CSV e faz conversões de tipo básicas."""
    print(f"[LEITURA] Carregando: {caminho}")
    df = pd.read_csv(caminho, encoding="utf-8")
    df["data_pedido"] = pd.to_datetime(df["data_pedido"], format="%Y-%m-%d", errors="coerce")
    print(f"  -> {len(df)} registros carregados, {df.shape[1]} colunas.")
    return df


def relatorio_qualidade(df: pd.DataFrame, etapa: str) -> None:
    """Imprime um relatório resumido da qualidade dos dados."""
    print(f"\n[QUALIDADE — {etapa}]")
    nulos = df.isnull().sum()
    nulos_filtrado = nulos[nulos > 0]
    if nulos_filtrado.empty:
        print("  -> Nenhum valor nulo encontrado.")
    else:
        print("  -> Valores nulos por coluna:")
        print(nulos_filtrado.to_string())
    print(f"  -> Total de registros: {len(df)}")


def tratar_valores_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trata valores ausentes:
      - Colunas numéricas: preenche com a mediana da coluna
      - Colunas categóricas: preenche com a moda ou valor padrão
      - Datas: remove linhas com data inválida (obrigatório)
    """
    print("\n[LIMPEZA] Tratando valores nulos...")

    colunas_numericas   = ["distancia_entrega", "tempo_entrega", "custo_entrega", "valor_pedido"]
    colunas_categoricas = ["regiao_cliente", "id_motorista"]

    for col in colunas_numericas:
        qtd_nulos = df[col].isnull().sum()
        if qtd_nulos > 0:
            mediana = df[col].median()
            df[col] = df[col].fillna(mediana)
            print(f"  -> '{col}': {qtd_nulos} nulos preenchidos com mediana ({mediana:.2f})")

    for col in colunas_categoricas:
        qtd_nulos = df[col].isnull().sum()
        if qtd_nulos > 0:
            moda = df[col].mode()[0]
            df[col] = df[col].fillna(moda)
            print(f"  -> '{col}': {qtd_nulos} nulos preenchidos com moda ('{moda}')")

    # Remover registros com data_pedido inválida
    antes = len(df)
    df = df.dropna(subset=["data_pedido"])
    removidos = antes - len(df)
    if removidos > 0:
        print(f"  -> {removidos} registros removidos por data_pedido inválida.")

    return df


def remover_duplicatas(df: pd.DataFrame) -> pd.DataFrame:
    """Remove registros duplicados com base no id_pedido."""
    antes = len(df)
    df = df.drop_duplicates(subset=["id_pedido"], keep="first")
    removidos = antes - len(df)
    print(f"\n[LIMPEZA] Duplicatas: {removidos} registros removidos.")
    return df


def validar_intervalos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida e filtra registros com valores fora dos intervalos esperados.
    Registros inválidos são marcados, logados e removidos.
    """
    print("\n[VALIDAÇÃO] Verificando intervalos de valores...")
    registros_invalidos = pd.Series(False, index=df.index)

    # Distância de entrega
    mascara = ~df["distancia_entrega"].between(DISTANCIA_MIN_KM, DISTANCIA_MAX_KM)
    if mascara.sum() > 0:
        print(f"  -> distancia_entrega fora do intervalo [{DISTANCIA_MIN_KM}, {DISTANCIA_MAX_KM}]: {mascara.sum()} registros")
        registros_invalidos |= mascara

    # Tempo de entrega
    mascara = ~df["tempo_entrega"].between(TEMPO_MIN_MIN, TEMPO_MAX_MIN)
    if mascara.sum() > 0:
        print(f"  -> tempo_entrega fora do intervalo [{TEMPO_MIN_MIN}, {TEMPO_MAX_MIN}]: {mascara.sum()} registros")
        registros_invalidos |= mascara

    # Custo de entrega
    mascara = ~df["custo_entrega"].between(CUSTO_MIN_BRL, CUSTO_MAX_BRL)
    if mascara.sum() > 0:
        print(f"  -> custo_entrega fora do intervalo [{CUSTO_MIN_BRL}, {CUSTO_MAX_BRL}]: {mascara.sum()} registros")
        registros_invalidos |= mascara

    # Valor do pedido
    mascara = ~df["valor_pedido"].between(VALOR_MIN_BRL, VALOR_MAX_BRL)
    if mascara.sum() > 0:
        print(f"  -> valor_pedido fora do intervalo [{VALOR_MIN_BRL}, {VALOR_MAX_BRL}]: {mascara.sum()} registros")
        registros_invalidos |= mascara

    # Região válida
    mascara = ~df["regiao_cliente"].isin(REGIOES_VALIDAS)
    if mascara.sum() > 0:
        print(f"  -> regiao_cliente inválida: {mascara.sum()} registros")
        registros_invalidos |= mascara

    total_invalidos = registros_invalidos.sum()
    if total_invalidos > 0:
        df = df[~registros_invalidos].copy()
        print(f"  -> {total_invalidos} registros inválidos removidos.")
    else:
        print("  -> Todos os registros estão dentro dos intervalos esperados.")

    return df


def adicionar_colunas_derivadas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona colunas calculadas úteis para análise:
      - ano_mes     : período YYYY-MM para agrupamentos mensais
      - custo_por_km: eficiência de custo (R$/km)
      - entrega_no_prazo: flag booleana (tempo <= 180 min = dentro do prazo)
    """
    print("\n[TRANSFORMAÇÃO] Adicionando colunas derivadas...")

    df["ano_mes"] = df["data_pedido"].dt.to_period("M").astype(str)
    df["custo_por_km"] = (df["custo_entrega"] / df["distancia_entrega"]).round(2)
    df["entrega_no_prazo"] = df["tempo_entrega"] <= 180

    print("  -> 'ano_mes': período mensal (YYYY-MM)")
    print("  -> 'custo_por_km': custo por quilômetro (R$/km)")
    print("  -> 'entrega_no_prazo': True se tempo <= 180 min")

    return df


def padronizar_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """Garante os tipos corretos de cada coluna."""
    df["distancia_entrega"] = df["distancia_entrega"].astype(float)
    df["tempo_entrega"]     = df["tempo_entrega"].astype(int)
    df["custo_entrega"]     = df["custo_entrega"].astype(float)
    df["valor_pedido"]      = df["valor_pedido"].astype(float)
    df["regiao_cliente"]    = df["regiao_cliente"].str.strip().str.title()
    df["id_motorista"]      = df["id_motorista"].str.strip().str.upper()
    return df


def main():
    """Função principal do pipeline de limpeza."""
    print("=" * 55)
    print("  OptiFlow — Limpeza e Tratamento de Dados")
    print("=" * 55)

    # 1. Carregar dados brutos
    df = carregar_dados(RAW_PATH)
    relatorio_qualidade(df, "DADOS BRUTOS")

    # 2. Remover duplicatas
    df = remover_duplicatas(df)

    # 3. Tratar valores nulos
    df = tratar_valores_nulos(df)

    # 4. Validar e filtrar intervalos
    df = validar_intervalos(df)

    # 5. Padronizar tipos
    df = padronizar_tipos(df)

    # 6. Adicionar colunas derivadas
    df = adicionar_colunas_derivadas(df)

    # Relatório final
    relatorio_qualidade(df, "DADOS LIMPOS")

    # 7. Salvar dados limpos
    os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False, encoding="utf-8")

    print(f"\n[OK] Dados limpos salvos em: {os.path.abspath(CLEAN_PATH)}")
    print(f"     Total de registros: {len(df)}")

    # Exibir amostra final
    print("\n[AMOSTRA FINAL — 5 primeiros registros]")
    print(df.head().to_string(index=False))


if __name__ == "__main__":
    main()
