# Modelo Matemático — Problema 2: Alocação de Motoristas por Região

**Disciplina:** Pesquisa Operacional  
**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Tipo de Problema:** Programação Linear Inteira (PLI) — Problema de Designação Generalizado

---

## 1. Descrição do Problema

A OptiFlow precisa determinar a **alocação ótima de motoristas às regiões de entrega**, **maximizando a eficiência operacional**, medida pela razão entre pedidos entregues e horas trabalhadas, respeitando:
- A disponibilidade de horas de cada motorista
- A demanda mínima de entregas por região
- O nível mínimo de experiência do motorista para cada região
- O limite de motoristas simultâneos por região

---

## 2. Conjuntos

| Símbolo | Definição                                                     |
|---------|---------------------------------------------------------------|
| $M$     | Conjunto de motoristas disponíveis: $M = \{1, 2, ..., p\}$   |
| $R$     | Conjunto de regiões de entrega: $R = \{1, 2, ..., q\}$       |

---

## 3. Parâmetros

| Símbolo       | Definição                                                          | Unidade          |
|---------------|--------------------------------------------------------------------|------------------|
| $e_{mr}$      | Eficiência do motorista $m$ na região $r$ (pedidos/hora)           | pedidos/hora     |
| $h_m$         | Horas disponíveis do motorista $m$ no período                      | horas            |
| $t_{mr}$      | Horas necessárias para executar rotas na região $r$ pelo motorista $m$ | horas        |
| $D_r$         | Demanda mínima de entregas na região $r$ (pedidos)                 | pedidos          |
| $E_{\min,r}$  | Nível mínimo de experiência exigido para região $r$                | 1 (baixo) a 3 (alto)|
| $\hat{E}_m$   | Nível de experiência do motorista $m$                              | 1 a 3            |
| $K_r$         | Número máximo de motoristas simultâneos na região $r$              | unidade          |
| $L_{\max}$    | Número máximo de regiões que um motorista pode cobrir              | unidade          |

---

## 4. Variável de Decisão

$$x_{mr} = \begin{cases} 1 & \text{se o motorista } m \text{ é alocado à região } r \\ 0 & \text{caso contrário} \end{cases}$$

---

## 5. Função Objetivo

**Maximizar a eficiência operacional total:**

$$\max Z = \sum_{m \in M} \sum_{r \in R} e_{mr} \cdot h_m \cdot x_{mr}$$

Onde $e_{mr} \cdot h_m$ representa o total de pedidos que o motorista $m$ consegue entregar na região $r$ em $h_m$ horas disponíveis.

---

## 6. Restrições

### R1 — Disponibilidade de horas do motorista:
$$\sum_{r \in R} t_{mr} \cdot x_{mr} \leq h_m, \quad \forall m \in M$$

### R2 — Demanda mínima atendida por região:
$$\sum_{m \in M} e_{mr} \cdot h_m \cdot x_{mr} \geq D_r, \quad \forall r \in R$$

### R3 — Número máximo de motoristas por região:
$$\sum_{m \in M} x_{mr} \leq K_r, \quad \forall r \in R$$

### R4 — Restrição de experiência mínima por região:
$$x_{mr} \leq \mathbb{1}[\hat{E}_m \geq E_{\min,r}], \quad \forall m \in M, \forall r \in R$$

Onde $\mathbb{1}[\cdot]$ é a função indicadora (1 se verdadeiro, 0 se falso).

### R5 — Número máximo de regiões por motorista:
$$\sum_{r \in R} x_{mr} \leq L_{\max}, \quad \forall m \in M$$

### R6 — Domínio das variáveis (integralidade):
$$x_{mr} \in \{0, 1\}, \quad \forall m \in M, \forall r \in R$$

---

## 7. Formulação Compacta

$$\max Z = \sum_{m \in M} \sum_{r \in R} e_{mr} \cdot h_m \cdot x_{mr}$$

$$\text{sujeito a:}$$

$$\sum_{r \in R} t_{mr} \cdot x_{mr} \leq h_m \qquad \forall m \in M \quad (R1)$$

$$\sum_{m \in M} e_{mr} \cdot h_m \cdot x_{mr} \geq D_r \qquad \forall r \in R \quad (R2)$$

$$\sum_{m \in M} x_{mr} \leq K_r \qquad \forall r \in R \quad (R3)$$

$$x_{mr} \leq \mathbb{1}[\hat{E}_m \geq E_{\min,r}] \qquad \forall m,r \quad (R4)$$

$$\sum_{r \in R} x_{mr} \leq L_{\max} \qquad \forall m \in M \quad (R5)$$

$$x_{mr} \in \{0, 1\} \quad (R6)$$

---

## 8. Interpretação da Eficiência

A **eficiência** $e_{mr}$ é calculada com base em histórico operacional:

$$e_{mr} = \frac{\text{Pedidos entregues pelo motorista } m \text{ na região } r}{\text{Horas trabalhadas na região } r}$$

**Fatores que influenciam a eficiência:**
- Familiaridade com a região geográfica
- Histórico de entregas no prazo
- Avaliação dos clientes
- Conhecimento das vias de acesso

---

## 9. Exemplo de Gabarito Esperado

| Motorista | Região   | Horas Alocadas | Eficiência (ped/h) | Pedidos Esperados |
|-----------|----------|----------------|--------------------|-------------------|
| M001      | Centro   | 4h             | 3,5                | 14                |
| M003      | Norte    | 5h             | 2,8                | 14                |
| M005      | Sul      | 4h             | 3,2                | 13                |
| M007      | Leste    | 5h             | 3,0                | 15                |
| M009      | Oeste    | 4h             | 2,9                | 12                |
| **Total** |          | **22h**        | **—**              | **68**            |

---

## 10. Classificação e Complexidade

| Aspecto               | Classificação                                   |
|-----------------------|-------------------------------------------------|
| Tipo de problema      | Programação Linear Inteira Mista (PLIM / MILP)  |
| Natureza da variável  | Binária ($\{0,1\}$)                             |
| Complexidade          | NP-difícil (generalização do Problema de Designação) |
| Solver utilizado      | PuLP + CBC (gratuito e open-source)             |
| Instância do estudo   | 10 motoristas, 5 regiões                        |
| Solução esperada      | Encontrada em < 1 segundo                       |

---

*Referências: Arenales et al. (2011) — Pesquisa Operacional | Goldbarg & Luna (2005) — Otimização Combinatória e Programação Linear*
