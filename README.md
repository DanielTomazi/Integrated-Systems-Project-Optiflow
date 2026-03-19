# OptiFlow — Projeto Integrador em Gestão de Sistemas Computacionais

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-green)

> 🌐 **Site institucional:** [opti-flow-site.vercel.app](https://opti-flow-site.vercel.app/)  
> 💻 **Repositório do site:** [github.com/DanielTomazi/OptiFlow-Site](https://github.com/DanielTomazi/OptiFlow-Site)

---

## Identificação

| Campo              | Informação                                              |
|--------------------|--------------------------------------------------------|
| **Aluno**          | Daniel Tomazi de Oliveira                               |
| **RA**             | A preencher                                             |
| **Curso**          | Gestão de Sistemas Computacionais                       |
| **Período**        | 2026 - 8º semestre                                   |
| **Empresa**        | OptiFlow Logística Inteligente                          |
| **Disciplinas**    | Gestão de Projetos · Análise de Dados · Segurança da Informação · Pesquisa Operacional |

---

## Descrição da Empresa

**OptiFlow Logística Inteligente** é uma plataforma tecnológica SaaS voltada para a otimização logística de pequenas e médias empresas de e-commerce. A empresa atua como intermediadora entre lojistas e operações de última milha, fornecendo:

- Roteamento inteligente de entregas
- Alocação eficiente de motoristas
- Painel de monitoramento de KPIs logísticos
- Análise de desempenho operacional em tempo real
- Infraestrutura segura de dados conforme a LGPD

---

## Problema de Negócio

Pequenas e médias empresas de e-commerce enfrentam desafios críticos na operação logística:

| Problema                             | Impacto                                        |
|--------------------------------------|------------------------------------------------|
| Rotas de entrega ineficientes        | Aumento de 20–35% no custo de combustível      |
| Má alocação de motoristas            | Ociosidade e sobrecarga operacional            |
| Atrasos nas entregas                 | Queda no NPS e aumento de devoluções           |
| Falta de análise de dados            | Decisões baseadas em intuição, não em dados    |
| Processos manuais e sem rastreamento | Erros, retrabalho e falta de visibilidade      |

A OptiFlow resolve esses problemas combinando análise de dados, algoritmos de otimização, segurança da informação e gestão estruturada de projetos.

---

## Arquitetura Geral do Projeto

```
┌────────────────────────────────────────────────────────────┐
│                  OptiFlow — Visão Sistêmica                │
├──────────────┬──────────────┬──────────────┬───────────────┤
│  Gestão de   │  Análise de  │  Segurança   │   Pesquisa    │
│  Projetos    │   Dados      │     Info.    │  Operacional  │
│              │              │              │               │
│ TAP · EAP    │ ETL · KPIs   │ Ameaças · GUT│ Otimização    │
│ RACI · Gantt │ Gráficos     │ Auth · LGPD  │ de Rotas e    │
│ Riscos · Ágil│ Notebooks    │              │ Motoristas    │
└──────────────┴──────────────┴──────────────┴───────────────┘
        │               │               │              │
        └───────────────┴───────────────┴──────────────┘
                                │
                    ┌───────────▼────────────┐
                    │   Documento Final +    │
                    │   Vídeo de Apresentação│
                    └────────────────────────┘
```

---

## Estrutura do Repositório

```
OptiFlow-Projeto-Integrador/
│
├── README.md
│
├── docs/
│   ├── visao_geral_projeto.md
│   ├── descricao_empresa.md
│   └── problema_negocio.md
│
├── 01_gestao_de_projetos/
│   ├── termo_de_abertura.md
│   ├── eap_wbs.md
│   ├── matriz_raci.md
│   ├── cronograma_gantt.md
│   ├── estimativa_custos.md
│   ├── plano_riscos.md
│   ├── plano_comunicacao.md
│   └── backlog_agil.md
│
├── 02_analise_de_dados/
│   ├── data/
│   │   └── dataset_logistica.csv
│   ├── etl/
│   │   ├── gerar_dados.py
│   │   └── limpeza_dados.py
│   ├── kpis/
│   │   └── calcular_kpis.py
│   ├── visualizacao/
│   │   ├── grafico_receita.py
│   │   └── grafico_performance_entregas.py
│   └── notebooks/
│       └── analise_dados.ipynb
│
├── 03_seguranca_da_informacao/
│   ├── mapeamento_ameacas.md
│   ├── matriz_gut.md
│   ├── arquitetura_autenticacao.md
│   └── adequacao_lgpd.md
│
├── 04_pesquisa_operacional/
│   ├── problema_1_otimizacao_entregas/
│   │   ├── modelo_matematico.md
│   │   ├── otimizacao.py
│   │   └── analise_cenarios.py
│   └── problema_2_alocacao_motoristas/
│       ├── modelo_matematico.md
│       ├── otimizacao.py
│       └── analise_cenarios.py
│
├── 05_documento_final/
│   ├── modelo_relatorio_final.md
│   ├── relatorio_final_PENDENTE_PDF.md
│   └── referencias.md
│
└── 06_video_apresentacao/
    └── roteiro_video.md
```

---

## Como Executar os Scripts Python

### Pré-requisitos

Certifique-se de ter **Python 3.10+** instalado. Em seguida, instale as dependências:

```bash
pip install pandas numpy matplotlib seaborn pulp jupyter
```

### Passo a Passo

#### 1. Gerar o Dataset Simulado
```bash
cd 02_analise_de_dados/etl
python gerar_dados.py
```
> Gera o arquivo `data/dataset_logistica.csv` com 200 registros logísticos simulados.

#### 2. Limpeza e Tratamento dos Dados
```bash
python limpeza_dados.py
```

#### 3. Calcular KPIs
```bash
cd ../kpis
python calcular_kpis.py
```

#### 4. Gerar Visualizações
```bash
cd ../visualizacao
python grafico_receita.py
python grafico_performance_entregas.py
```

#### 5. Abrir o Notebook de Análise
```bash
cd ../notebooks
jupyter notebook analise_dados.ipynb
```

#### 6. Executar Otimização de Rotas
```bash
cd ../../04_pesquisa_operacional/problema_1_otimizacao_entregas
python otimizacao.py
python analise_cenarios.py
```

#### 7. Executar Alocação de Motoristas
```bash
cd ../problema_2_alocacao_motoristas
python otimizacao.py
python analise_cenarios.py
```

---

## Disciplinas Integradas

| # | Disciplina               | Entregáveis Principais                                            |
|---|--------------------------|-------------------------------------------------------------------|
| 1 | Gestão de Projetos       | TAP, EAP, RACI, Gantt, Riscos, Comunicação, Backlog               |
| 2 | Análise de Dados         | Dataset, ETL, KPIs, Gráficos, Notebook                           |
| 3 | Segurança da Informação  | Mapeamento de Ameaças, Matriz GUT, Autenticação, LGPD            |
| 4 | Pesquisa Operacional     | Otimização de Rotas, Alocação de Motoristas, Análise de Cenários |

---

## Links do Projeto

| Recurso | URL |
|---------|-----|
| Site institucional | [opti-flow-site.vercel.app](https://opti-flow-site.vercel.app/) |
| Repositório do site (Angular) | [github.com/DanielTomazi/OptiFlow-Site](https://github.com/DanielTomazi/OptiFlow-Site) |
| Repositório do projeto integrado | [github.com/DanielTomazi](https://github.com/DanielTomazi/Integrated-Systems-Project-Optiflow) |

---

## Licença

Este projeto é desenvolvido para fins acadêmicos.  
© 2026 Daniel Tomazi de Oliveira — OptiFlow Logística Inteligente.
