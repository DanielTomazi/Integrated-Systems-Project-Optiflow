# Modelo de Relatório Final — Projeto Integrador em Gestão de Sistemas Computacionais

**Aluno:** Daniel Tomazi de Oliveira  
**Empresa Fictícia:** OptiFlow Logística Inteligente  
**Curso:** Gestão de Sistemas Computacionais  
**Período:** 2026  

---

> **Instruções de uso:** Este documento é o modelo/template para o relatório final integrador. Substitua as seções marcadas com `[PREENCHER]` pelo conteúdo real desenvolvido durante o projeto. O relatório final deve ter no mínimo 20 páginas.

---

## CAPA

```
┌────────────────────────────────────────────────────────┐
│              NOME DA INSTITUIÇÃO DE ENSINO              │
│                                                        │
│                 CURSO DE GRADUAÇÃO EM                  │
│         GESTÃO DE SISTEMAS COMPUTACIONAIS              │
│                                                        │
│                                                        │
│              PROJETO INTEGRADOR — 2026                 │
│                                                        │
│     OPTIFLOW LOGÍSTICA INTELIGENTE: UM ESTUDO          │
│     INTEGRADO DE GESTÃO, DADOS, SEGURANÇA E            │
│     OTIMIZAÇÃO EM LOGÍSTICA DE ÚLTIMA MILHA            │
│                                                        │
│                                                        │
│                 Daniel Tomazi de Oliveira              │
│                                                        │
│                   [Cidade], [Mês] 2026                 │
└────────────────────────────────────────────────────────┘
```

---

## FOLHA DE ROSTO

**Título:** OptiFlow Logística Inteligente: um Estudo Integrado de Gestão, Análise de Dados, Segurança e Otimização em Logística de Última Milha

**Aluno:** Daniel Tomazi de Oliveira  
**Orientador:** [PREENCHER — Nome do orientador]  
**Disciplinas integradas:**
1. Gestão de Projetos
2. Análise de Dados
3. Segurança da Informação
4. Pesquisa Operacional

**Tipo de trabalho:** Projeto Integrador — Trabalho de Conclusão  
**Instituição:** [PREENCHER]  
**Data de entrega:** [PREENCHER]

---

## RESUMO

[PREENCHER — 150 a 250 palavras]

*Este projeto integrador apresenta o desenvolvimento de uma plataforma de otimização logística denominada OptiFlow Logística Inteligente, concebida para auxiliar e-commerces de pequeno e médio porte na gestão eficiente de entregas de última milha. O trabalho integra quatro disciplinas do curso: Gestão de Projetos, Análise de Dados, Segurança da Informação e Pesquisa Operacional.*

*Na disciplina de Gestão de Projetos, foram elaborados escopo, cronograma, análise de riscos e backlog ágil seguindo as metodologias PMBOK e Scrum. Na Análise de Dados, foram coletados e processados dados logísticos simulados de 200 pedidos, calculando KPIs essenciais como faturamento mensal, tempo médio de entrega e custo por pedido, com visualizações em Python (pandas, matplotlib e seaborn). No eixo de Segurança da Informação, foram realizados mapeamento de ameaças (STRIDE), priorização de vulnerabilidades (GUT), projeto de arquitetura de autenticação (bcrypt + JWT + 2FA + RBAC) e análise de adequação à LGPD. Por fim, na Pesquisa Operacional, foram formulados e resolvidos dois problemas de otimização via Programação Linear Inteira com a biblioteca PuLP: otimização de rotas de entrega e alocação de motoristas por região.*

*Os resultados demonstram reduções simuladas de [X]% nos custos de entrega e [Y]% no tempo médio, além da viabilidade técnica e econômica da plataforma.*

**Palavras-chave:** logística; otimização; análise de dados; segurança da informação; PuLP; LGPD; Gestão de Projetos.

---

## ABSTRACT

[PREENCHER — Tradução para inglês do Resumo]

**Keywords:** logistics; optimization; data analysis; information security; PuLP; GDPR; Project Management.

---

## LISTA DE FIGURAS

| Nº  | Título                                               | Página |
|-----|------------------------------------------------------|--------|
| 1   | Diagrama de arquitetura da plataforma OptiFlow       | [XX]   |
| 2   | Estrutura Analítica do Projeto (EAP/WBS)             | [XX]   |
| 3   | Cronograma de Gantt — 16 semanas                     | [XX]   |
| 4   | Gráfico de faturamento mensal (jan–out 2025)         | [XX]   |
| 5   | Desempenho de entregas por região                    | [XX]   |
| 6   | Diagrama de Fluxo de Dados (DFD) — STRIDE           | [XX]   |
| 7   | Arquitetura de autenticação JWT + 2FA                | [XX]   |
| 8   | Resultado da otimização de rotas — Problema 1        | [XX]   |
| 9   | Análise de cenários — Otimização de rotas            | [XX]   |
| 10  | Resultado da alocação de motoristas — Problema 2     | [XX]   |

---

## LISTA DE TABELAS

| Nº  | Título                                               | Página |
|-----|------------------------------------------------------|--------|
| 1   | Descrição da empresa OptiFlow                        | [XX]   |
| 2   | Problemas de negócio e soluções propostas            | [XX]   |
| 3   | Matriz RACI — Responsabilidades                      | [XX]   |
| 4   | Estimativa de custos do projeto                      | [XX]   |
| 5   | KPIs calculados — Período jan–out 2025               | [XX]   |
| 6   | Matriz GUT — Vulnerabilidades priorizadas            | [XX]   |
| 7   | Parâmetros do Modelo 1 — Otimização de Rotas         | [XX]   |
| 8   | Comparativo de cenários — Problema 1                 | [XX]   |
| 9   | Parâmetros do Modelo 2 — Alocação de Motoristas      | [XX]   |
| 10  | Comparativo de cenários — Problema 2                 | [XX]   |

---

## SUMÁRIO

1. [Introdução](#1-introdução)
2. [Empresa e Contexto](#2-empresa-e-contexto)
3. [Gestão de Projetos](#3-gestão-de-projetos)
4. [Análise de Dados](#4-análise-de-dados)
5. [Segurança da Informação](#5-segurança-da-informação)
6. [Pesquisa Operacional](#6-pesquisa-operacional)
7. [Integração entre Disciplinas](#7-integração-entre-disciplinas)
8. [Resultados e Discussão](#8-resultados-e-discussão)
9. [Conclusão](#9-conclusão)
10. [Referências](#10-referências)
11. [Apêndices](#11-apêndices)

---

## 1. INTRODUÇÃO

### 1.1 Contextualização

[PREENCHER — Contextualizar o setor de logística no Brasil, crescimento do e-commerce, desafios da última milha]

O setor de logística no Brasil movimenta cerca de R$ 350 bilhões por ano, representando aproximadamente 12% do PIB nacional. O crescimento acelerado do e-commerce, impulsionado pela pandemia de 2020 e pela digitalização do varejo, impôs novos desafios às operações de entrega de última milha — o trecho final da cadeia logística, entre o centro de distribuição e o consumidor final.

Pequenas e médias empresas de e-commerce enfrentam barreiras tecnológicas significativas para implementar soluções de otimização logística: custos elevados de software especializado, ausência de dados estruturados e falta de capacidade técnica interna. Este cenário justifica o desenvolvimento da **OptiFlow Logística Inteligente**, proposta deste projeto integrador.

### 1.2 Problema de Pesquisa

[PREENCHER — Enunciar claramente o problema central que o projeto resolve]

### 1.3 Objetivos

**Objetivo Geral:**
Desenvolver o projeto conceitual e técnico de uma plataforma SaaS de otimização logística para e-commerces de pequeno e médio porte, integrando gestão de projetos, análise de dados, segurança da informação e pesquisa operacional.

**Objetivos Específicos:**
1. Aplicar metodologias de gestão de projetos (PMBOK/Scrum) no planejamento da plataforma
2. Analisar dados logísticos simulados e calcular KPIs operacionais estratégicos
3. Projetar arquitetura de segurança alinhada à LGPD e às boas práticas OWASP
4. Formular e resolver problemas de otimização de rotas e alocação de motoristas via PLI

### 1.4 Justificativa

[PREENCHER — Justificar a relevância acadêmica e prática do projeto]

### 1.5 Metodologia

Este projeto adota uma abordagem metodológica híbrida:

| Disciplina               | Metodologia Aplicada             |
|--------------------------|----------------------------------|
| Gestão de Projetos       | PMBOK 6ª Edição + Scrum          |
| Análise de Dados         | CRISP-DM                         |
| Segurança da Informação  | STRIDE + OWASP Top 10 + LGPD    |
| Pesquisa Operacional     | Programação Linear Inteira (PLI) |

### 1.6 Estrutura do Trabalho

[PREENCHER — Breve descrição de cada capítulo]

---

## 2. EMPRESA E CONTEXTO

### 2.1 Descrição da Empresa

A **OptiFlow Logística Inteligente** é uma empresa fictícia criada para fins acadêmicos neste projeto integrador, mas baseada em características reais de startups logtech do mercado brasileiro.

| Campo             | Informação                                              |
|-------------------|---------------------------------------------------------|
| Nome              | OptiFlow Logística Inteligente                          |
| Setor             | Tecnologia da Informação / Logística (Logtech)          |
| Modelo de negócio | SaaS B2B (Software como Serviço)                        |
| Público-alvo      | E-commerces de pequeno e médio porte                    |
| Proposta de valor | Reduzir custos e tempo de entrega via IA e otimização   |
| Fundação (fictícia)| Janeiro de 2025                                        |

### 2.2 Módulos da Plataforma

[PREENCHER — Descrever os 4 módulos da plataforma]

### 2.3 Problemas de Negócio Identificados

[PREENCHER — Inserir tabela de problemas com impactos medidos, conforme docs/problema_negocio.md]

---

## 3. GESTÃO DE PROJETOS

### 3.1 Metodologia Adotada

[PREENCHER — Descrever a abordagem híbrida PMBOK + Scrum]

### 3.2 Termo de Abertura do Projeto (TAP)

[PREENCHER — Resumir os principais elementos do TAP]

### 3.3 Estrutura Analítica do Projeto (EAP)

[PREENCHER — Inserir o diagrama WBS e descrição dos pacotes de trabalho principais]

### 3.4 Cronograma

[PREENCHER — Inserir Gantt simplificado e marcos principais]

### 3.5 Análise de Riscos

[PREENCHER — Descrever os principais riscos identificados e estratégias de resposta]

### 3.6 Backlog Ágil

[PREENCHER — Apresentar as user stories mais relevantes e a organização em sprints]

### 3.7 Análise Crítica da Gestão de Projetos

[PREENCHER — Reflexão sobre o que funcionou, desafios e aprendizados]

---

## 4. ANÁLISE DE DADOS

### 4.1 Metodologia CRISP-DM

[PREENCHER — Descrever as 6 fases do CRISP-DM aplicadas]

### 4.2 Dataset Utilizado

O dataset `dataset_logistica.csv` foi gerado sinteticamente para simular 200 pedidos da OptiFlow entre janeiro e outubro de 2025, com as seguintes variáveis:

| Variável           | Tipo        | Descrição                              |
|--------------------|-------------|----------------------------------------|
| id_pedido          | Categórica  | Identificador único do pedido (P001–P200)|
| regiao_cliente     | Categórica  | Região geográfica (5 regiões)          |
| distancia_entrega  | Numérica    | Distância em quilômetros (5–45 km)     |
| tempo_entrega      | Numérica    | Tempo em minutos (36–225 min)          |
| custo_entrega      | Numérica    | Custo em R$ (9,50–56,10)              |
| id_motorista       | Categórica  | Identificador do motorista (M001–M010) |
| valor_pedido       | Numérica    | Valor do pedido em R$ (48,90–790,00)  |
| data_pedido        | Data        | Data do pedido (jan–out 2025)          |

### 4.3 Pipeline ETL

[PREENCHER — Descrever o processo de limpeza e transformação de dados]

### 4.4 KPIs Calculados

[PREENCHER — Inserir tabela com os KPIs calculados e valores obtidos]

### 4.5 Visualizações

[PREENCHER — Inserir e comentar os gráficos gerados pelos scripts Python]

### 4.6 Insights Obtidos

[PREENCHER — Principais descobertas da análise de dados]

---

## 5. SEGURANÇA DA INFORMAÇÃO

### 5.1 Mapeamento de Ameaças (STRIDE)

[PREENCHER — Resumir as principais ameaças identificadas]

### 5.2 Priorização com Matriz GUT

[PREENCHER — Apresentar o top 5 de vulnerabilidades priorizadas]

### 5.3 Arquitetura de Autenticação

[PREENCHER — Descrever os mecanismos implementados: bcrypt, JWT, 2FA, RBAC]

### 5.4 Adequação à LGPD

[PREENCHER — Descrever os dados coletados, bases legais e mecanismos de compliance]

### 5.5 Análise Crítica da Segurança

[PREENCHER — Reflexão sobre riscos residuais e trabalhos futuros]

---

## 6. PESQUISA OPERACIONAL

### 6.1 Introdução à Programação Linear Inteira

[PREENCHER — 1 parágrafo contextualizando PLI e sua aplicação em logística]

### 6.2 Problema 1 — Otimização de Rotas

#### 6.2.1 Formulação Matemática

[PREENCHER — Transcrever o modelo matemático do arquivo modelo_matematico.md]

#### 6.2.2 Implementação Computacional

[PREENCHER — Descrever o código PuLP e resultados obtidos]

#### 6.2.3 Análise de Cenários

[PREENCHER — Comparar os 5 cenários e discutir implicações]

### 6.3 Problema 2 — Alocação de Motoristas

#### 6.3.1 Formulação Matemática

[PREENCHER — Transcrever o modelo matemático do arquivo modelo_matematico.md]

#### 6.3.2 Implementação Computacional

[PREENCHER — Descrever o código PuLP e resultados obtidos]

#### 6.3.3 Análise de Cenários

[PREENCHER — Comparar os 5 cenários e discutir implicações]

---

## 7. INTEGRAÇÃO ENTRE DISCIPLINAS

[PREENCHER — Descrever como as 4 disciplinas se relacionam e se complementam no contexto da OptiFlow]

Exemplo de tabela de integração:

| Eixo de Integração                     | Disciplinas Envolvidas             |
|-----------------------------------------|------------------------------------|
| KPIs de análise alimentam modelo de otimização | Análise de Dados + P. Operacional |
| Gestão de riscos inclui riscos de segurança | Gestão de Projetos + Segurança  |
| Backlog ágil inclui requisitos de segurança | G. Projetos + Segurança         |
| Dados de produção exigem LGPD          | Análise de Dados + Segurança       |

---

## 8. RESULTADOS E DISCUSSÃO

### 8.1 Resultados por Disciplina

[PREENCHER — Tabela consolidada de resultados]

| Disciplina               | Meta Inicial                  | Resultado Obtido        |
|--------------------------|-------------------------------|-------------------------|
| Gestão de Projetos       | 8 artefatos PMBOK/Scrum       | [PREENCHER]             |
| Análise de Dados         | 4 KPIs + 5 visualizações      | [PREENCHER]             |
| Segurança da Informação  | 4 documentos de segurança     | [PREENCHER]             |
| Pesquisa Operacional     | 2 modelos PLI resolvidos      | [PREENCHER]             |

### 8.2 Discussão

[PREENCHER — Analisar os resultados em relação às hipóteses iniciais e literatura]

---

## 9. CONCLUSÃO

### 9.1 Considerações Finais

[PREENCHER — Síntese dos principais resultados e contribuições]

### 9.2 Limitações do Estudo

[PREENCHER — Reconhecer as limitações: dados simulados, escopo acadêmico, etc.]

### 9.3 Trabalhos Futuros

[PREENCHER — Sugerir extensões do trabalho]

Possíveis extensões:
- Implementação real da API REST com FastAPI
- Integração com APIs de geolocalização (Google Maps / OSRM)
- Expansão do modelo PLI para VRP completo com janelas de tempo (VRPTW)
- Aplicação de Machine Learning para previsão de demanda por região

---

## 10. REFERÊNCIAS

*Ver arquivo [`referencias.md`](referencias.md) para lista completa.*

---

## 11. APÊNDICES

### Apêndice A — Estrutura do Repositório GitHub

```
DanielTomazi-Integrated-Systems-Project-Optiflow/
├── README.md
├── docs/
│   ├── visao_geral_projeto.md
│   ├── descricao_empresa.md
│   └── problema_negocio.md
├── 01_gestao_de_projetos/
│   ├── termo_de_abertura.md
│   ├── eap_wbs.md
│   ├── matriz_raci.md
│   ├── cronograma_gantt.md
│   ├── estimativa_custos.md
│   ├── plano_riscos.md
│   ├── plano_comunicacao.md
│   └── backlog_agil.md
├── 02_analise_de_dados/
│   ├── data/dataset_logistica.csv
│   ├── etl/{gerar_dados,limpeza_dados}.py
│   ├── kpis/calcular_kpis.py
│   ├── visualizacao/{grafico_receita,grafico_performance_entregas}.py
│   └── notebooks/analise_dados.ipynb
├── 03_seguranca_da_informacao/
│   ├── mapeamento_ameacas.md
│   ├── matriz_gut.md
│   ├── arquitetura_autenticacao.md
│   └── adequacao_lgpd.md
├── 04_pesquisa_operacional/
│   ├── problema_1_otimizacao_entregas/
│   │   ├── modelo_matematico.md
│   │   ├── otimizacao.py
│   │   └── analise_cenarios.py
│   └── problema_2_alocacao_motoristas/
│       ├── modelo_matematico.md
│       ├── otimizacao.py
│       └── analise_cenarios.py
├── 05_documento_final/
│   ├── modelo_relatorio_final.md
│   └── referencias.md
└── 06_video_apresentacao/
    └── roteiro_video.md
```

### Apêndice B — Instruções de Execução

```bash
# 1. Clonar repositório
git clone https://github.com/SEU_USUARIO/DanielTomazi-Integrated-Systems-Project-Optiflow.git
cd DanielTomazi-Integrated-Systems-Project-Optiflow

# 2. Instalar dependências
pip install pandas numpy matplotlib seaborn pulp jupyter

# 3. Gerar dataset
python 02_analise_de_dados/etl/gerar_dados.py

# 4. Executar ETL
python 02_analise_de_dados/etl/limpeza_dados.py

# 5. Calcular KPIs
python 02_analise_de_dados/kpis/calcular_kpis.py

# 6. Gerar visualizações
python 02_analise_de_dados/visualizacao/grafico_receita.py
python 02_analise_de_dados/visualizacao/grafico_performance_entregas.py

# 7. Executar otimizações
python 04_pesquisa_operacional/problema_1_otimizacao_entregas/otimizacao.py
python 04_pesquisa_operacional/problema_2_alocacao_motoristas/otimizacao.py

# 8. Análise de cenários
python 04_pesquisa_operacional/problema_1_otimizacao_entregas/analise_cenarios.py
python 04_pesquisa_operacional/problema_2_alocacao_motoristas/analise_cenarios.py
```

---

*Este documento é um template acadêmico desenvolvido para o Projeto Integrador em Gestão de Sistemas Computacionais — OptiFlow Logística Inteligente.*
