# Plano de Riscos — Projeto OptiFlow

**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026

---

## 1. Metodologia de Gestão de Riscos

Este plano adota a metodologia do **PMBOK** para identificação, análise qualitativa, planejamento e monitoramento de riscos:

1. **Identificar** os riscos potenciais
2. **Analisar** probabilidade e impacto (Matriz P×I)
3. **Planejar respostas** (evitar, mitigar, transferir, aceitar)
4. **Monitorar** o status dos riscos ao longo do projeto

---

## 2. Escala de Probabilidade

| Código | Nível       | Descrição                              | Probabilidade |
|--------|-------------|----------------------------------------|---------------|
| P1     | Muito Baixa | Evento quase improvável                | < 10%         |
| P2     | Baixa       | Evento improvável, mas possível        | 10–30%        |
| P3     | Média       | Evento possível com certa frequência   | 30–60%        |
| P4     | Alta        | Evento provável de ocorrer             | 60–80%        |
| P5     | Muito Alta  | Evento muito provável de ocorrer       | > 80%         |

---

## 3. Escala de Impacto

| Código | Nível       | Impacto no Prazo | Impacto na Qualidade   |
|--------|-------------|------------------|------------------------|
| I1     | Muito Baixo | < 1 dia          | Mínimo                 |
| I2     | Baixo       | 1–3 dias         | Pequeno                |
| I3     | Médio       | 3–7 dias         | Significativo          |
| I4     | Alto        | 7–14 dias        | Importante             |
| I5     | Muito Alto  | > 14 dias        | Comprometedor          |

---

## 4. Matriz de Probabilidade × Impacto

```
           I1 (M.Baixo) | I2 (Baixo) | I3 (Médio) | I4 (Alto) | I5 (M.Alto)
P5 (M.Alta)    MÉDIO    |    ALTO    |    ALTO    |  CRÍTICO  |   CRÍTICO
P4 (Alta)      BAIXO    |   MÉDIO    |    ALTO    |   ALTO    |   CRÍTICO
P3 (Média)     BAIXO    |   BAIXO    |   MÉDIO    |   ALTO    |    ALTO
P2 (Baixa)   ACEITÁVEL  |   BAIXO    |   BAIXO    |  MÉDIO    |    ALTO
P1 (M.Baixa) ACEITÁVEL  | ACEITÁVEL  |   BAIXO    |  BAIXO    |   MÉDIO
```

---

## 5. Registro de Riscos

| ID   | Categoria     | Descrição do Risco                                        | Prob. | Impacto | Nível    | Estratégia  | Ação de Resposta                                                     | Gatilho                               | Responsável     |
|------|---------------|-----------------------------------------------------------|-------|---------|----------|-------------|----------------------------------------------------------------------|---------------------------------------|-----------------|
| R001 | Prazo         | Atraso nas entregas por subestimativa de esforço          | P3    | I4      | ALTO     | Mitigar     | Adicionar buffer de 20% nas estimativas; priorizar itens críticos    | Entrega com > 3 dias de atraso        | Daniel Tomazi   |
| R002 | Técnico       | Dificuldade com PuLP/OR-Tools nos modelos de otimização  | P4    | I3      | ALTO     | Mitigar     | Estudar documentação antecipadamente; usar problemas simplificados   | Eror ao executar o script             | Daniel Tomazi   |
| R003 | Dados         | Dataset insuficiente ou incoerente para análise           | P2    | I4      | MÉDIO    | Mitigar     | Usar geração de dados sintéticos com numpy; validar schema antes     | Gráficos sem padrão identificável     | Daniel Tomazi   |
| R004 | Scope Creep   | Mudança de escopo solicitada pelo orientador              | P2    | I4      | MÉDIO    | Evitar      | TAP assinado com escopo definido; documentar mudanças formalmente    | Solicitação de novo artefato          | Orientador      |
| R005 | Técnico       | Ambiente Python com dependências incompatíveis            | P3    | I2      | BAIXO    | Mitigar     | Usar requirements.txt; testar em virtualenv antes de iniciar         | Erro de import ao executar script     | Daniel Tomazi   |
| R006 | Dados         | Perda de código ou arquivos por falha no disco            | P1    | I5      | MÉDIO    | Mitigar     | Commit diário no GitHub; backup local semanal                        | Arquivo não encontrado                | Daniel Tomazi   |
| R007 | Qualidade     | Relatório final sem nível de qualidade acadêmica          | P2    | I4      | MÉDIO    | Mitigar     | Revisar com orientador nas semanas 14 e 15                           | Feedback negativo na revisão           | Daniel + Orient.|
| R008 | Prazo         | Acúmulo de disciplinas no semestre impede dedicação       | P3    | I3      | MÉDIO    | Aceitar     | Planejar horários fixos de trabalho; priorizar entregas críticas     | Ausência de progresso por 1 semana    | Daniel Tomazi   |
| R009 | Técnico       | Notebook Jupyter com células com erro                     | P2    | I2      | BAIXO    | Mitigar     | Executar todas as células antes da entrega; usar `Restart & Run All` | Célula com traceback                  | Daniel Tomazi   |
| R010 | Comunicação   | Orientador indisponível para reuniões no prazo            | P2    | I3      | BAIXO    | Aceitar     | Agendar reuniões com 2 semanas de antecedência; usar e-mail backup   | Reunião cancelada 2x consecutivas     | Orientador      |
| R011 | Qualidade     | Modelos de otimização com resultados incorretos           | P3    | I4      | ALTO     | Mitigar     | Validar soluções com exemplos acadêmicos; verificar restrições       | Solução infeasible no PuLP            | Daniel Tomazi   |
| R012 | Acadêmico     | Plágio não intencional na documentação                    | P1    | I5      | MÉDIO    | Evitar      | Citar todas as referências; usar próprias palavras; revisar antes     | Similaridade > 20% no detector        | Daniel Tomazi   |

---

## 6. Riscos por Nível (Priorização)

### Riscos Críticos
Nenhum risco nível crítico identificado.

### Riscos Altos (Atenção Imediata)
- **R001** — Atraso por subestimativa de esforço
- **R002** — Dificuldade com PuLP nos modelos de otimização
- **R011** — Soluções incorretas nos modelos

### Riscos Médios (Monitorar)
- **R003** — Dataset insuficiente
- **R004** — Scope Creep
- **R006** — Perda de dados
- **R007** — Qualidade do relatório
- **R008** — Acúmulo de disciplinas
- **R012** — Plágio não intencional

### Riscos Baixos (Acompanhar)
- **R005** — Dependências incompatíveis
- **R009** — Notebook com erros
- **R010** — Orientador indisponível

---

## 7. Plano de Resposta a Emergências

| Situação de Emergência                  | Resposta Imediata                                                        |
|-----------------------------------------|--------------------------------------------------------------------------|
| Perda total do repositório GitHub       | Restaurar do backup local; recriar repositório; notificar orientador     |
| Modelo de otimização sem solução válida | Simplificar o problema; adicionar comentários explicando a limitação     |
| Doença/impedimento pessoal grave        | Comunicar orientador imediatamente; solicitar prorrogação de prazo       |
| Computador com defeito                  | Usar computador da instituição ou laboratório                            |

---

## 8. Monitoramento de Riscos

| Frequência | Ação                                                              |
|------------|-------------------------------------------------------------------|
| Semanal    | Revisar o status dos riscos altos e médios                        |
| Quinzenal  | Atualizar o registro de riscos com novos itens identificados      |
| Por marco  | Avaliar se novos riscos emergiram com o avanço do projeto         |

---

*Este plano deve ser revisado sempre que houver mudança de escopo, prazo ou surgimento de novo risco relevante.*
