# Modelo Matemático — Problema 1: Otimização de Rotas de Entrega

**Disciplina:** Pesquisa Operacional  
**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Tipo de Problema:** Programação Linear Inteira (PLI) — Variante do VRP (Vehicle Routing Problem)

---

## 1. Descrição do Problema

A OptiFlow precisa determinar a **alocação ótima de pedidos a rotas**, minimizando o **custo total de entrega**, respeitando:
- A capacidade máxima de peso por rota (veículo)
- O número máximo de paradas por rota
- A distância máxima percorrida por rota

Este problema é uma variação do **Capacitated Vehicle Routing Problem (CVRP)**, simplificado para o contexto acadêmico como um **Problema de Atribuição com Múltiplas Restrições**.

---

## 2. Conjuntos

| Símbolo | Definição                                           |
|---------|-----------------------------------------------------|
| $I$     | Conjunto de pedidos a entregar: $I = \{1, 2, ..., n\}$ |
| $J$     | Conjunto de rotas disponíveis: $J = \{1, 2, ..., m\}$ |

---

## 3. Parâmetros

| Símbolo         | Definição                                                | Unidade         |
|-----------------|----------------------------------------------------------|-----------------|
| $c_{ij}$        | Custo de executar o pedido $i$ na rota $j$               | R$ (reais)      |
| $d_{ij}$        | Distância associada ao pedido $i$ na rota $j$            | Quilômetros     |
| $p_i$           | Peso/volume do pedido $i$                                | kg              |
| $D_{\max}$      | Distância máxima permitida por rota                      | Quilômetros     |
| $P_{\max}$      | Capacidade de peso máxima por rota                       | kg              |
| $N_{\max}$      | Número máximo de paradas (pedidos) por rota              | Unidade         |
| $f_j$           | Custo fixo de ativar a rota $j$ (combustível base)       | R$ (reais)      |
| $A_j$           | Indicador: rota $j$ disponível (motorista disponível)    | Binário $\{0,1\}$ |

---

## 4. Variável de Decisão

$$x_{ij} = \begin{cases} 1 & \text{se o pedido } i \text{ é atribuído à rota } j \\ 0 & \text{caso contrário} \end{cases}$$

$$y_j = \begin{cases} 1 & \text{se a rota } j \text{ é ativada (ao menos 1 pedido atribuído)} \\ 0 & \text{caso contrário} \end{cases}$$

---

## 5. Função Objetivo

**Minimizar o custo total de entrega:**

$$\min Z = \sum_{j \in J} f_j \cdot y_j + \sum_{i \in I} \sum_{j \in J} c_{ij} \cdot x_{ij}$$

Onde:
- $\sum_{j \in J} f_j \cdot y_j$ = soma dos custos fixos das rotas ativadas
- $\sum_{i \in I} \sum_{j \in J} c_{ij} \cdot x_{ij}$ = soma dos custos variáveis de execução dos pedidos

---

## 6. Restrições

### R1 — Cada pedido deve ser atribuído a exatamente uma rota:
$$\sum_{j \in J} x_{ij} = 1, \quad \forall i \in I$$

### R2 — Capacidade de peso máxima por rota:
$$\sum_{i \in I} p_i \cdot x_{ij} \leq P_{\max}, \quad \forall j \in J$$

### R3 — Distância máxima por rota:
$$\sum_{i \in I} d_{ij} \cdot x_{ij} \leq D_{\max}, \quad \forall j \in J$$

### R4 — Número máximo de paradas por rota:
$$\sum_{i \in I} x_{ij} \leq N_{\max}, \quad \forall j \in J$$

### R5 — Ativar rota apenas se ao menos um pedido for atribuído:
$$x_{ij} \leq y_j, \quad \forall i \in I, \forall j \in J$$

### R6 — Somente rotas disponíveis podem ser ativadas:
$$y_j \leq A_j, \quad \forall j \in J$$

### R7 — Domínio das variáveis (integralidade):
$$x_{ij} \in \{0, 1\}, \quad \forall i \in I, \forall j \in J$$
$$y_j \in \{0, 1\}, \quad \forall j \in J$$

---

## 7. Formulação Compacta

$$\min Z = \sum_{j \in J} f_j y_j + \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}$$

$$\text{sujeito a:}$$

$$\sum_{j \in J} x_{ij} = 1 \qquad \forall i \in I \quad (R1)$$

$$\sum_{i \in I} p_i x_{ij} \leq P_{\max} \qquad \forall j \in J \quad (R2)$$

$$\sum_{i \in I} d_{ij} x_{ij} \leq D_{\max} \qquad \forall j \in J \quad (R3)$$

$$\sum_{i \in I} x_{ij} \leq N_{\max} \qquad \forall j \in J \quad (R4)$$

$$x_{ij} \leq y_j \qquad \forall i,j \quad (R5)$$

$$y_j \leq A_j \qquad \forall j \quad (R6)$$

$$x_{ij}, y_j \in \{0,1\} \quad (R7)$$

---

## 8. Interpretação da Solução

A solução ótima $x^*_{ij}$ indica:
- Para cada pedido $i$, em qual rota $j$ ele deve ser executado
- Quais rotas devem ser ativadas ($y^*_j = 1$)
- O custo total mínimo $Z^*$

**Exemplo de interpretação:**

| Pedido | Rota Atribuída | Custo (R$) | Distância (km) |
|--------|----------------|------------|----------------|
| P001   | R2             | 18,50      | 12,0           |
| P002   | R1             | 22,00      | 15,5           |
| P003   | R2             | 17,80      | 10,0           |
| ...    | ...            | ...        | ...            |

---

## 9. Classificação e Complexidade

| Aspecto               | Classificação                               |
|-----------------------|---------------------------------------------|
| Tipo de problema      | Programação Linear Inteira (PLI / ILP)      |
| Natureza da variável  | Binária ($\{0,1\}$)                         |
| Complexidade          | NP-difícil (para instâncias grandes)        |
| Solver utilizado      | PuLP + CBC (gratuito e open-source)         |
| Instância do estudo   | 15 pedidos, 5 rotas (resolvível em segundos)|

---

*Referências: Hillier & Lieberman (2013) — Introdução à Pesquisa Operacional | Taha (2016) — Operations Research: An Introduction*
