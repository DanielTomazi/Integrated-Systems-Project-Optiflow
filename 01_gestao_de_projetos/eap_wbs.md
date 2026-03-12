# EAP / WBS — Estrutura Analítica do Projeto

**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026

---

## 1. Introdução

A **Estrutura Analítica do Projeto (EAP)**, também conhecida como **WBS (Work Breakdown Structure)**, decompõe hierarquicamente todo o trabalho do projeto em componentes menores e gerenciáveis.

---

## 2. EAP — Representação Hierárquica em Texto

```
0. OPTIFLOW — PROJETO INTEGRADOR
│
├── 1. GESTÃO DO PROJETO
│   ├── 1.1 Iniciação
│   │   ├── 1.1.1 Termo de Abertura do Projeto (TAP)
│   │   └── 1.1.2 Identificação das partes interessadas
│   ├── 1.2 Planejamento
│   │   ├── 1.2.1 EAP / WBS
│   │   ├── 1.2.2 Matriz RACI
│   │   ├── 1.2.3 Cronograma (Gantt)
│   │   ├── 1.2.4 Estimativa de Custos
│   │   ├── 1.2.5 Plano de Riscos
│   │   └── 1.2.6 Plano de Comunicação
│   ├── 1.3 Execução e Monitoramento
│   │   ├── 1.3.1 Backlog Ágil (Sprints)
│   │   └── 1.3.2 Controle de progresso
│   └── 1.4 Encerramento
│       ├── 1.4.1 Lições aprendidas
│       └── 1.4.2 Aprovação final
│
├── 2. ANÁLISE DE DADOS
│   ├── 2.1 Coleta e Geração de Dados
│   │   ├── 2.1.1 Definição do schema do dataset
│   │   ├── 2.1.2 Script de geração de dados simulados (gerar_dados.py)
│   │   └── 2.1.3 Dataset logístico (dataset_logistica.csv)
│   ├── 2.2 ETL — Limpeza e Transformação
│   │   ├── 2.2.1 Tratamento de valores ausentes
│   │   ├── 2.2.2 Normalização de colunas
│   │   └── 2.2.3 Script de limpeza (limpeza_dados.py)
│   ├── 2.3 Cálculo de KPIs
│   │   ├── 2.3.1 Faturamento mensal
│   │   ├── 2.3.2 Tempo médio de entrega
│   │   ├── 2.3.3 Custo médio por entrega
│   │   └── 2.3.4 Script de KPIs (calcular_kpis.py)
│   ├── 2.4 Visualizações
│   │   ├── 2.4.1 Gráfico de faturamento ao longo do tempo
│   │   ├── 2.4.2 Gráfico de performance de entregas
│   │   └── 2.4.3 Análise por região
│   └── 2.5 Notebook de Análise
│       └── 2.5.1 Notebook Jupyter integrado (analise_dados.ipynb)
│
├── 3. SEGURANÇA DA INFORMAÇÃO
│   ├── 3.1 Identificação de Ameaças
│   │   ├── 3.1.1 Mapeamento de ameaças (STRIDE)
│   │   ├── 3.1.2 SQL Injection
│   │   ├── 3.1.3 Vazamento de credenciais
│   │   └── 3.1.4 Indisponibilidade de servidores (DDoS)
│   ├── 3.2 Análise de Riscos
│   │   └── 3.2.1 Matriz GUT
│   ├── 3.3 Arquitetura de Segurança
│   │   ├── 3.3.1 Hash de senhas (bcrypt)
│   │   ├── 3.3.2 Autenticação JWT
│   │   ├── 3.3.3 Autenticação em dois fatores (2FA)
│   │   └── 3.3.4 Controle de acesso por papel (RBAC)
│   └── 3.4 Conformidade LGPD
│       ├── 3.4.1 Inventário de dados pessoais
│       ├── 3.4.2 Base legal para coleta
│       ├── 3.4.3 Mecanismo de exclusão de dados
│       └── 3.4.4 Política de privacidade
│
├── 4. PESQUISA OPERACIONAL
│   ├── 4.1 Problema 1 — Otimização de Rotas
│   │   ├── 4.1.1 Modelagem matemática (modelo_matematico.md)
│   │   ├── 4.1.2 Implementação do modelo (otimizacao.py)
│   │   └── 4.1.3 Análise de cenários (analise_cenarios.py)
│   └── 4.2 Problema 2 — Alocação de Motoristas
│       ├── 4.2.1 Modelagem matemática (modelo_matematico.md)
│       ├── 4.2.2 Implementação do modelo (otimizacao.py)
│       └── 4.2.3 Análise de cenários (analise_cenarios.py)
│
└── 5. ENCERRAMENTO
    ├── 5.1 Relatório Final Integrador
    │   ├── 5.1.1 Redação do relatório (modelo_relatorio_final.md)
    │   └── 5.1.2 Referências bibliográficas
    └── 5.2 Vídeo de Apresentação
        ├── 5.2.1 Roteiro do vídeo
        └── 5.2.2 Gravação e edição
```

---

## 3. Dicionário da EAP

| Código | Nome do Pacote de Trabalho          | Descrição                                                         | Responsável              | Duração Estimada |
|--------|-------------------------------------|-------------------------------------------------------------------|--------------------------|------------------|
| 1.1.1  | Termo de Abertura do Projeto        | Documento formal de autorização e início do projeto               | Daniel Tomazi            | 2 dias           |
| 1.2.1  | EAP / WBS                           | Decomposição hierárquica do trabalho                              | Daniel Tomazi            | 1 dia            |
| 1.2.2  | Matriz RACI                         | Definição de responsabilidades                                    | Daniel Tomazi            | 1 dia            |
| 1.2.3  | Cronograma (Gantt)                  | Sequenciamento e duração das atividades                           | Daniel Tomazi            | 1 dia            |
| 1.2.4  | Estimativa de Custos                | Orçamento e recursos necessários                                  | Daniel Tomazi            | 1 dia            |
| 1.2.5  | Plano de Riscos                     | Identificação, análise e resposta a riscos                        | Daniel Tomazi            | 2 dias           |
| 1.2.6  | Plano de Comunicação                | Estratégia de comunicação do projeto                              | Daniel Tomazi            | 1 dia            |
| 1.3.1  | Backlog Ágil                        | Lista priorizada de requisitos (sprints)                          | Daniel Tomazi            | 1 dia            |
| 2.1.2  | Script gerar_dados.py               | Geração de dataset logístico simulado com 200+ registros          | Daniel Tomazi            | 3 dias           |
| 2.2.3  | Script limpeza_dados.py             | Limpeza, tratamento e transformação dos dados                     | Daniel Tomazi            | 2 dias           |
| 2.3.4  | Script calcular_kpis.py             | Cálculo e exibição dos KPIs operacionais                          | Daniel Tomazi            | 2 dias           |
| 2.4.1  | Gráfico de faturamento              | Gráfico de linha com faturamento mensal                           | Daniel Tomazi            | 2 dias           |
| 2.4.2  | Gráfico de performance              | Gráfico de barras com entregas por período e região               | Daniel Tomazi            | 2 dias           |
| 2.5.1  | Notebook Jupyter                    | Análise exploratória integrada com markdown e código              | Daniel Tomazi            | 3 dias           |
| 3.1.1  | Mapeamento de ameaças               | Identificação de ameaças usando metodologia STRIDE                | Daniel Tomazi            | 2 dias           |
| 3.2.1  | Matriz GUT                          | Priorização de vulnerabilidades (Gravidade, Urgência, Tendência)  | Daniel Tomazi            | 1 dia            |
| 3.3.1  | Arquitetura de autenticação         | Especificação técnica de hash, JWT, 2FA e RBAC                    | Daniel Tomazi            | 2 dias           |
| 3.4.4  | Adequação LGPD                      | Documentação de conformidade com a Lei Geral de Proteção de Dados | Daniel Tomazi            | 2 dias           |
| 4.1.2  | otimizacao.py (rotas)               | Modelo de PL para minimizar custos de entrega                     | Daniel Tomazi            | 4 dias           |
| 4.1.3  | analise_cenarios.py (rotas)         | Análise de sensibilidade do modelo de rotas                       | Daniel Tomazi            | 2 dias           |
| 4.2.2  | otimizacao.py (motoristas)          | Modelo de PL para alocação eficiente de motoristas                | Daniel Tomazi            | 4 dias           |
| 4.2.3  | analise_cenarios.py (motoristas)    | Análise de sensibilidade do modelo de motoristas                  | Daniel Tomazi            | 2 dias           |
| 5.1.1  | Relatório Final                     | Documento integrador de todas as disciplinas                      | Daniel Tomazi            | 5 dias           |
| 5.2.1  | Roteiro do vídeo                    | Roteiro detalhado para o vídeo de apresentação                    | Daniel Tomazi            | 1 dia            |

---

## 4. Critérios de Aceitação por Entrega

| Entrega                  | Critério de Aceitação                                               |
|--------------------------|---------------------------------------------------------------------|
| Análise de Dados         | Scripts executam sem erros; gráficos são gerados corretamente       |
| Pesquisa Operacional     | Modelos retornam solução ótima com PuLP; cenários documentados      |
| Segurança da Informação  | Documentação cobre OWASP Top 10 + LGPD; matriz GUT completa        |
| Gestão de Projetos       | Todos os 8 artefatos presentes e preenchidos                        |
| Relatório Final          | Mínimo 20 páginas; todas as disciplinas integradas                  |
| Vídeo                    | Duração de 5–10 minutos; apresenta todos os entregáveis             |
