# Cronograma / Gantt — Projeto OptiFlow

**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026  
**Duração Total:** 16 semanas

---

## 1. Visão Geral das Fases

| Fase      | Descrição                          | Semanas | Status        |
|-----------|------------------------------------|---------|---------------|
| Fase 1    | Iniciação do Projeto               | 1–2     | A iniciar     |
| Fase 2    | Planejamento                       | 3–4     | A iniciar     |
| Fase 3    | Análise de Dados                   | 5–9     | A iniciar     |
| Fase 4    | Segurança da Informação            | 10–11   | A iniciar     |
| Fase 5    | Pesquisa Operacional               | 12–14   | A iniciar     |
| Fase 6    | Encerramento                       | 15–16   | A iniciar     |

---

## 2. Cronograma Detalhado (Gantt em Texto)

> Legenda: `█` = Atividade em execução | `─` = Atividade prevista | `✓` = Concluída

```
ATIVIDADE                               | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 |S10 |S11 |S12 |S13 |S14 |S15 |S16 |
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 1 — INICIAÇÃO
1.1 Definição do escopo e contexto     | ── | ── |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
1.2 Elaboração do TAP                  | ── | ── |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
1.3 Identificação de stakeholders      |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 2 — PLANEJAMENTO
2.1 EAP / WBS                          |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |    |
2.2 Matriz RACI                        |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |    |
2.3 Cronograma Gantt                   |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |    |
2.4 Estimativa de Custos               |    |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |
2.5 Plano de Riscos                    |    |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |
2.6 Plano de Comunicação               |    |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |
2.7 Backlog Ágil                       |    |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |    |
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 3 — ANÁLISE DE DADOS
3.1 Definição do schema do dataset     |    |    |    |    | ── |    |    |    |    |    |    |    |    |    |    |    |
3.2 Script gerar_dados.py              |    |    |    |    | ── | ── |    |    |    |    |    |    |    |    |    |    |
3.3 Script limpeza_dados.py            |    |    |    |    |    | ── | ── |    |    |    |    |    |    |    |    |    |
3.4 Script calcular_kpis.py            |    |    |    |    |    |    | ── | ── |    |    |    |    |    |    |    |    |
3.5 Gráfico de faturamento             |    |    |    |    |    |    |    | ── |    |    |    |    |    |    |    |    |
3.6 Gráfico de performance             |    |    |    |    |    |    |    | ── |    |    |    |    |    |    |    |    |
3.7 Notebook Jupyter                   |    |    |    |    |    |    |    |    | ── |    |    |    |    |    |    |    |
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 4 — SEGURANÇA DA INFORMAÇÃO
4.1 Mapeamento de ameaças              |    |    |    |    |    |    |    |    |    | ── |    |    |    |    |    |    |
4.2 Matriz GUT                         |    |    |    |    |    |    |    |    |    | ── |    |    |    |    |    |    |
4.3 Arquitetura de autenticação        |    |    |    |    |    |    |    |    |    |    | ── |    |    |    |    |    |
4.4 Adequação à LGPD                   |    |    |    |    |    |    |    |    |    |    | ── |    |    |    |    |    |
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 5 — PESQUISA OPERACIONAL
5.1 Modelo mat. — Rotas (doc)          |    |    |    |    |    |    |    |    |    |    |    | ── |    |    |    |    |
5.2 Script otimizacao.py (rotas)       |    |    |    |    |    |    |    |    |    |    |    | ── | ── |    |    |    |
5.3 Script analise_cenarios.py (rotas) |    |    |    |    |    |    |    |    |    |    |    |    | ── |    |    |    |
5.4 Modelo mat. — Motoristas (doc)     |    |    |    |    |    |    |    |    |    |    |    |    | ── |    |    |    |
5.5 Script otimizacao.py (motoristas)  |    |    |    |    |    |    |    |    |    |    |    |    | ── | ── |    |    |
5.6 analise_cenarios.py (motoristas)   |    |    |    |    |    |    |    |    |    |    |    |    |    | ── |    |    |
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 6 — ENCERRAMENTO
6.1 Relatório Final Integrador         |    |    |    |    |    |    |    |    |    |    |    |    |    |    | ── | ── |
6.2 Revisão com Orientador             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | ── |
6.3 Roteiro e Vídeo de Apresentação    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | ── | ── |
6.4 Entrega Final no GitHub            |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | ── |
```

---

## 3. Marcos do Projeto (Milestones)

| Marco | Semana | Entrega                                                   |
|-------|--------|-----------------------------------------------------------|
| M1    | S2     | TAP aprovado, Kickoff realizado                           |
| M2    | S4     | Todos os artefatos de planejamento concluídos             |
| M3    | S9     | Pipeline de análise de dados completo                     |
| M4    | S11    | Documentação de segurança completa                        |
| M5    | S14    | Modelos de otimização implementados e validados           |
| M6    | S16    | Relatório final entregue, vídeo gravado                   |

---

## 4. Estimativa de Esforço por Fase

| Fase                        | Horas Estimadas | % do Total |
|-----------------------------|-----------------|------------|
| Gestão de Projetos          | 20 h            | 18%        |
| Análise de Dados            | 35 h            | 31%        |
| Segurança da Informação     | 20 h            | 18%        |
| Pesquisa Operacional        | 25 h            | 22%        |
| Encerramento / Relatório    | 12 h            | 11%        |
| **Total**                   | **112 h**       | **100%**   |

---

## 5. Dependências entre Atividades

| Atividade           | Pré-Requisito                          |
|---------------------|----------------------------------------|
| limpeza_dados.py    | gerar_dados.py concluído               |
| calcular_kpis.py    | limpeza_dados.py concluído             |
| Gráfico receita     | calcular_kpis.py concluído             |
| Notebook Jupyter    | Todos os scripts da análise prontos    |
| otimizacao.py       | modelo_matematico.md redigido          |
| analise_cenarios.py | otimizacao.py funcional                |
| Relatório Final     | Todas as fases anteriores concluídas   |
| Vídeo               | Relatório Final rascunhado             |

---

## 6. Buffer de Contingência

| Risco                         | Buffer Alocado |
|-------------------------------|----------------|
| Atraso na análise de dados    | +3 dias        |
| Dificuldade na otimização     | +4 dias        |
| Revisão do orientador         | +2 dias        |
| Problemas de ambiente técnico | +2 dias        |

*A semana 16 funciona como buffer final para ajustes de última hora.*
