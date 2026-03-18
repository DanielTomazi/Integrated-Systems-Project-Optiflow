# Visão Geral do Projeto — OptiFlow

## 1. Identificação

| Campo          | Informação                                       |
|----------------|--------------------------------------------------|
| Nome do Projeto| OptiFlow Logística Inteligente                   |
| Aluno          | Daniel Tomazi de Oliveira                        |
| RA             | A preencher                                      |
| Curso          | Gestão de Sistemas Computacionais                |
| Período        | 2026 — Semestre Letivo                           |
| Orientador     | A preencher                                      |
| Data de Início | 2026                                             |

---

## 2. Objetivo Geral

Desenvolver a concepção, planejamento, análise e modelagem de uma plataforma tecnológica chamada **OptiFlow**, que resolve problemas de logística de última milha enfrentados por pequenas e médias empresas de e-commerce, por meio da integração de:

- **Gestão de Projetos**: planejamento e controle estruturado
- **Análise de Dados**: extração de insights operacionais
- **Segurança da Informação**: proteção de dados e conformidade com a LGPD
- **Pesquisa Operacional**: otimização matemática de rotas e alocação de recursos

---

## 3. Escopo do Projeto

### 3.1 Incluso no Escopo

- Documentação completa de gestão de projetos (TAP, EAP, RACI, Gantt, Riscos)
- Pipeline de análise de dados com ETL, KPIs e visualizações
- Modelos matemáticos de otimização com implementação em Python
- Documentação de segurança da informação e conformidade LGPD
- Relatório final integrador
- Vídeo de apresentação acadêmica

### 3.2 Fora do Escopo

- Desenvolvimento de aplicação web funcional (front-end/back-end)
- Integração com sistemas de ERP reais
- Infraestrutura de cloud em produção
- Testes de carga e penetração em ambiente real

---

## 4. Disciplinas Integradas

```
┌─────────────────────────────────────────────────────────────┐
│                 OPTIFLOW — INTEGRAÇÃO DE DISCIPLINAS         │
├──────────────┬──────────────┬─────────────────┬─────────────┤
│ GESTÃO DE    │ ANÁLISE DE   │   SEGURANÇA DA  │  PESQUISA   │
│ PROJETOS     │ DADOS        │   INFORMAÇÃO    │ OPERACIONAL │
│              │              │                 │             │
│ • TAP        │ • ETL Python │ • Mapeamento de │ • Otimiz.   │
│ • EAP/WBS    │ • KPIs       │   Ameaças       │   de Rotas  │
│ • RACI       │ • Dashboard  │ • Matriz GUT    │ • Alocação  │
│ • Gantt      │ • Gráficos   │ • Auth/JWT/2FA  │   Motori-   │
│ • Riscos     │ • Notebook   │ • LGPD          │   stas      │
│ • Backlog    │              │                 │ • Cenários  │
└──────────────┴──────────────┴─────────────────┴─────────────┘
```

---

## 5. Metodologia

O projeto adota uma abordagem **híbrida** combinando:

- **PMBOK** (Project Management Body of Knowledge): para estrutura de gestão de projetos
- **Scrum/Ágil**: para o backlog e organização em sprints
- **CRISP-DM**: para o pipeline de análise de dados
- **PO/PuLP**: para modelagem e solução dos problemas de otimização
- **OWASP Top 10 + ISO 27001**: como referência para segurança da informação

---

## 6. Cronograma Macro

| Fase            | Período       | Descrição                                      |
|-----------------|---------------|------------------------------------------------|
| Fase 1 — Início | Semana 1–2    | Definição do escopo, TAP, EAP, equipe          |
| Fase 2 — Plan.  | Semana 3–5    | Cronograma, riscos, comunicação, backlog       |
| Fase 3 — Dados  | Semana 6–9    | ETL, KPIs, visualizações, notebook             |
| Fase 4 — Seg.   | Semana 10–11  | Ameaças, GUT, autenticação, LGPD               |
| Fase 5 — PO     | Semana 12–14  | Modelos de otimização, cenários                |
| Fase 6 — Fecho  | Semana 15–16  | Relatório final, vídeo, entrega                |

---

## 7. Resultados Esperados

1. **Repositório GitHub** completo com toda a documentação e código-fonte
2. **Scripts Python** funcionais para análise de dados e otimização
3. **Documentação de segurança** com matriz GUT e diretrizes LGPD
4. **Relatório final** integrador com todos os entregáveis
5. **Vídeo de apresentação** de até 10 minutos

---

## 8. Riscos Principais

| Risco                                   | Probabilidade | Impacto | Mitigação                          |
|-----------------------------------------|---------------|---------|------------------------------------|
| Atraso na entrega dos artefatos         | Média         | Alto    | Cronograma com buffer e milestones |
| Complexidade dos modelos de otimização  | Alta          | Médio   | Usar PuLP com problemas simplificados |
| Dataset insuficiente para análise       | Baixa         | Alto    | Geração de dados sintéticos        |
| Mudança de escopo                       | Média         | Alto    | Controle via backlog               |
