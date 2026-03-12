# Problema de Negócio — OptiFlow Logística Inteligente

## 1. Contexto

O setor de e-commerce brasileiro cresceu mais de **300%** na última década. Com esse crescimento, a operação de entrega tornou-se um dos maiores gargalos para PMEs: enquanto grandes marketplaces possuem tecnologia proprietária de roteamento e gestão, pequenas e médias empresas ainda operam de forma manual ou com ferramentas básicas.

---

## 2. Diagnóstico dos Problemas

### Problema 1 — Rotas de Entrega Ineficientes

**Descrição:**  
A ausência de roteirização inteligente leva motoristas a percorrerem trajetos com backtracking (ida e volta desnecessária), sem considerar trânsito, janelas de tempo ou capacidade de carga.

**Impactos Mensurados:**
- Desperdício de combustível estimado em 20–35% acima do necessário
- Aumento médio de 40 min por rota não otimizada
- Desgaste prematuro da frota

---

### Problema 2 — Altos Custos Logísticos

**Descrição:**  
Sem visibilidade de custos por entrega, pedido ou região, os gestores não conseguem identificar onde o dinheiro está sendo perdido. O custo logístico chega a representar 15–25% do valor do pedido em alguns casos.

**Impactos Mensurados:**
- Margem operacional reduzida em até 12 pontos percentuais
- Precificação incorreta dos fretes
- Impossibilidade de comparar desempenho de motoristas

---

### Problema 3 — Atrasos nas Entregas

**Descrição:**  
A falta de planejamento de capacidade gera sobrecarga em alguns motoristas enquanto outros ficam ociosos. Isso resulta em atrasos sistemáticos que impactam diretamente a satisfação do cliente.

**Impactos Mensurados:**
- Taxa de atraso média de 23% dos pedidos
- Queda no NPS (Net Promoter Score) de 12–18 pontos
- Aumento de 30% nas solicitações de reembolso

---

### Problema 4 — Má Alocação de Motoristas

**Descrição:**  
A distribuição de motoristas entre regiões é feita de forma empírica, sem considerar a demanda histórica por área, disponibilidade dos motoristas ou eficiência individual.

**Impactos Mensurados:**
- 18% dos motoristas trabalhando abaixo de 60% da capacidade
- 25% trabalhando acima do limite legal de jornada
- Custo com horas extras desnecessárias

---

### Problema 5 — Falta de Análise de Dados para Tomada de Decisão

**Descrição:**  
Os gestores não possuem acesso a indicadores operacionais em tempo real. Decisões são tomadas com base em planilhas manuais, relatos verbais ou intuição, sem embasamento analítico.

**Impactos Mensurados:**
- Tempo médio para identificar problemas operacionais: 7–14 dias
- 60% das decisões estratégicas sem embasamento em dados
- Impossibilidade de detectar tendências e sazonalidades

---

## 3. Causa Raiz (Diagrama de Ishikawa Simplificado)

```
                              ┌─────────────────┐
                              │   ALTA INEFICI- │
                              │   ÊNCIA LOGÍS-  │
                              │   TICA          │
                              └────────┬────────┘
              ┌─────────────┬──────────┴──────────┬──────────────┐
      ┌───────▼──────┐ ┌───▼─────┐          ┌────▼────┐  ┌──────▼─────┐
      │  PROCESSOS   │ │ PESSOAS │          │TECNOLO- │  │INFORMAÇÃO  │
      │              │ │         │          │  GIA    │  │            │
      │• Sem rotei-  │ │•Aloca-  │          │•Sem     │  │• Sem KPIs  │
      │  rização     │ │  ção    │          │ sistema │  │• Sem rela- │
      │• Manual      │ │  empí-  │          │ de      │  │  tórios    │
      │• Reativo     │ │  rica   │          │ rotei-  │  │• Dados não │
      │              │ │         │          │  riza-  │  │  integrados│
      └──────────────┘ └─────────┘          └─────────┘  └────────────┘
```

---

## 4. Solução Proposta pela OptiFlow

| Problema                         | Solução OptiFlow                                         |
|----------------------------------|----------------------------------------------------------|
| Rotas ineficientes               | Algoritmo de otimização (VRP — Vehicle Routing Problem)  |
| Altos custos sem visibilidade    | Dashboard de KPIs com custo por entrega/região           |
| Atrasos nas entregas             | Planejamento de capacidade com dados históricos          |
| Má alocação de motoristas        | Modelo de programação linear para alocação otimizada     |
| Falta de análise de dados        | Pipeline ETL + relatórios automáticos + gráficos         |

---

## 5. Indicadores de Sucesso (KPIs Meta)

| KPI                              | Situação Atual | Meta com OptiFlow | Prazo     |
|----------------------------------|----------------|-------------------|-----------|
| Custo médio por entrega          | R$ 32,50       | R$ 24,00          | 6 meses   |
| Tempo médio de entrega           | 4h 20min       | 2h 50min          | 6 meses   |
| Taxa de entregas no prazo        | 77%            | 93%               | 3 meses   |
| Utilização da frota              | 65%            | 88%               | 4 meses   |
| Horas extras por motorista/mês   | 18h            | 5h                | 3 meses   |

---

## 6. Justificativa para o Projeto Integrador

Este problema de negócio é ideal para o Projeto Integrador pois exige a aplicação simultânea e interdependente de quatro áreas do conhecimento:

1. **Gestão de Projetos**: estruturar as entregas, prazos, recursos e riscos
2. **Análise de Dados**: entender o comportamento operacional via dados
3. **Segurança da Informação**: proteger dados sensíveis de clientes e motoristas
4. **Pesquisa Operacional**: resolver matematicamente os problemas de rota e alocação
