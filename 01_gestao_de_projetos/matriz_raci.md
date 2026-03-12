# Matriz RACI — Responsabilidades do Projeto OptiFlow

**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026

---

## 1. Legenda

| Código | Papel            | Descrição                                                        |
|--------|------------------|------------------------------------------------------------------|
| **R**  | Responsible      | Responsável pela execução da tarefa                              |
| **A**  | Accountable      | Prestador de contas — aprova e é o dono da entrega               |
| **C**  | Consulted        | Consultado — fornece informações e feedback antes da execução    |
| **I**  | Informed         | Informado — recebe comunicação sobre o progresso/resultado       |

---

## 2. Partes Interessadas (Stakeholders)

| ID   | Parte Interessada         | Papel no Projeto                      |
|------|---------------------------|---------------------------------------|
| ST1  | Daniel Tomazi de Oliveira | Gerente e Executor do Projeto (solo)  |
| ST2  | Orientador Acadêmico      | Supervisor e Avaliador                |
| ST3  | Coordenador do Curso      | Aprovador Institucional               |
| ST4  | Banca Avaliadora          | Avaliação Final                       |

---

## 3. Matriz RACI Completa

| Entrega / Atividade                          | Daniel (ST1) | Orientador (ST2) | Coordenador (ST3) | Banca (ST4) |
|----------------------------------------------|:------------:|:----------------:|:-----------------:|:-----------:|
| **GESTÃO DE PROJETOS**                        |              |                  |                   |             |
| 1.1 Termo de Abertura (TAP)                   | R/A          | C                | I                 | I           |
| 1.2 EAP / WBS                                 | R/A          | C                | I                 | I           |
| 1.3 Matriz RACI                               | R/A          | C                | I                 | I           |
| 1.4 Cronograma Gantt                          | R/A          | C                | I                 | I           |
| 1.5 Estimativa de Custos                      | R/A          | C                | I                 | I           |
| 1.6 Plano de Riscos                           | R/A          | C                | I                 | I           |
| 1.7 Plano de Comunicação                      | R/A          | C                | I                 | I           |
| 1.8 Backlog Ágil                              | R/A          | C                | I                 | I           |
| **ANÁLISE DE DADOS**                          |              |                  |                   |             |
| 2.1 Definição do schema do dataset            | R/A          | C                | —                 | I           |
| 2.2 Script gerar_dados.py                     | R/A          | I                | —                 | I           |
| 2.3 Script limpeza_dados.py                   | R/A          | I                | —                 | I           |
| 2.4 Script calcular_kpis.py                   | R/A          | C                | —                 | I           |
| 2.5 Gráfico de faturamento                    | R/A          | I                | —                 | I           |
| 2.6 Gráfico de performance de entregas        | R/A          | I                | —                 | I           |
| 2.7 Notebook Jupyter (analise_dados.ipynb)    | R/A          | C                | —                 | I           |
| **SEGURANÇA DA INFORMAÇÃO**                   |              |                  |                   |             |
| 3.1 Mapeamento de ameaças                     | R/A          | C                | —                 | I           |
| 3.2 Matriz GUT                                | R/A          | C                | —                 | I           |
| 3.3 Arquitetura de autenticação               | R/A          | C                | —                 | I           |
| 3.4 Adequação à LGPD                          | R/A          | C                | I                 | I           |
| **PESQUISA OPERACIONAL**                      |              |                  |                   |             |
| 4.1 Modelo matemático — Rotas                 | R/A          | C                | —                 | I           |
| 4.2 Script otimizacao.py (rotas)              | R/A          | I                | —                 | I           |
| 4.3 Script analise_cenarios.py (rotas)        | R/A          | I                | —                 | I           |
| 4.4 Modelo matemático — Motoristas            | R/A          | C                | —                 | I           |
| 4.5 Script otimizacao.py (motoristas)         | R/A          | I                | —                 | I           |
| 4.6 Script analise_cenarios.py (motoristas)   | R/A          | I                | —                 | I           |
| **ENCERRAMENTO**                              |              |                  |                   |             |
| 5.1 Relatório Final Integrador                | R/A          | C                | I                 | I           |
| 5.2 Revisão do Relatório Final                | A            | R/C              | I                 | I           |
| 5.3 Roteiro do Vídeo                          | R/A          | C                | —                 | I           |
| 5.4 Gravação do Vídeo                         | R/A          | I                | —                 | I           |
| 5.5 Entrega Final (GitHub + documentos)       | R            | I                | A                 | I           |
| 5.6 Apresentação para Banca                   | R            | C                | I                 | A           |

---

## 4. Resumo de Responsabilidades por Stakeholder

### Daniel Tomazi de Oliveira (ST1)
- **Principal executor** de todas as atividades técnicas e de documentação
- Responsável por 100% das entregas do projeto
- Presta contas ao orientador e coordenador

### Orientador Acadêmico (ST2)
- Consultado nas fases-chave de planejamento, análise e modelagem
- Revisa o relatório final antes da entrega
- Informado sobre o progresso geral via reuniões periódicas

### Coordenador do Curso (ST3)
- Aprova o TAP e a entrega final
- Informado sobre o progresso do projeto
- Não participa da execução

### Banca Avaliadora (ST4)
- Recebe informações (relatório, vídeo, repositório) no momento da avaliação final
- Avalia e aprova/reprova as entregas do projeto

---

## 5. Comunicação com as Partes Interessadas

| Parte Interessada  | Formato da Comunicação      | Frequência         |
|--------------------|-----------------------------|--------------------|
| Orientador (ST2)   | Reunião + e-mail            | Quinzenal          |
| Coordenador (ST3)  | E-mail formal               | Por marco (milestone) |
| Banca (ST4)        | Relatório + Vídeo + Defesa  | Entrega final      |
