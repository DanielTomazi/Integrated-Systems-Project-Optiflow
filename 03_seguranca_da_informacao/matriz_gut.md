# Matriz GUT — Priorização de Vulnerabilidades

**Disciplina:** Segurança da Informação  
**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026

---

## 1. Metodologia GUT

A **Matriz GUT** é uma ferramenta de priorização que avalia cada problema/vulnerabilidade segundo três critérios:

| Critério     | Definição                                                            | Escala |
|--------------|----------------------------------------------------------------------|--------|
| **G**ravidade | Impacto do problema caso ele ocorra (danos, prejuízos, sanções)     | 1–5    |
| **U**rgência  | Pressão do tempo para resolver o problema                            | 1–5    |
| **T**endência | Evolução do problema sem intervenção (piora, mantém, melhora)        | 1–5    |

### Escala de Avaliação

| Nota | Gravidade                        | Urgência                         | Tendência                          |
|------|----------------------------------|----------------------------------|------------------------------------|
| 5    | Extremamente grave               | Ação imediata necessária         | Piora muito rapidamente            |
| 4    | Muito grave                      | Ação necessária em curto prazo   | Piora em pouco tempo               |
| 3    | Grave                            | Ação necessária em médio prazo   | Piora em médio prazo               |
| 2    | Pouco grave                      | Pouco urgente                    | Piora em longo prazo               |
| 1    | Sem gravidade significativa      | Pode aguardar                    | Não irá piorar / pode melhorar     |

**Fórmula:** `Score GUT = G × U × T`  
**Score Máximo:** 125 (5×5×5)

> **Regra de Prioridade:** Quanto maior o score GUT, maior a prioridade de tratamento.

---

## 2. Matriz GUT das Vulnerabilidades OptiFlow

| ID     | Vulnerabilidade / Ameaça               | G | U | T | Score GUT | Prioridade | Plano de Ação                          |
|--------|----------------------------------------|---|---|---|-----------|------------|----------------------------------------|
| V-01   | SQL Injection nos endpoints da API     | 5 | 5 | 5 | **125**   | 🔴 Crítica  | Prepared Statements + WAF imediato    |
| V-02   | Credenciais hardcoded no código-fonte  | 5 | 5 | 5 | **125**   | 🔴 Crítica  | Varredura do repositório + secrets manager |
| V-03   | Dados pessoais armazenados sem criptografia | 5 | 5 | 4 | **100** | 🔴 Crítica  | Criptografia AES-256 em repouso       |
| V-04   | JWT sem validação adequada de assinatura | 5 | 4 | 5 | **100**  | 🔴 Crítica  | Implementar validação RS256 + expiração curta |
| V-05   | Ausência de autenticação em 2 fatores  | 4 | 4 | 4 | **64**    | 🟠 Alta     | Integrar TOTP (Google Authenticator)  |
| V-06   | DDoS sem proteção de rate limiting     | 4 | 4 | 4 | **64**    | 🟠 Alta     | WAF + rate limiting + Cloudflare      |
| V-07   | IDOR nos endpoints de pedidos          | 4 | 4 | 4 | **64**    | 🟠 Alta     | Autorização por objeto (ABAC/RBAC)    |
| V-08   | Ausência de HTTPS/TLS em todas as rotas| 4 | 5 | 3 | **60**    | 🟠 Alta     | Forçar HTTPS + HSTS Header            |
| V-09   | Mensagens de erro verbosas expondo StackTrace | 3 | 4 | 4 | **48** | 🟡 Média  | Handler global de erros + logs privados |
| V-10   | Ausência de logs de auditoria          | 3 | 4 | 4 | **48**    | 🟡 Média   | Implementar audit trail (quem, quando, o quê) |
| V-11   | Sessões sem timeout                    | 3 | 3 | 4 | **36**    | 🟡 Média   | Timeout de inatividade (30 min)       |
| V-12   | Dependências com vulnerabilidades (CVEs)| 3 | 3 | 4 | **36**   | 🟡 Média   | Dependabot + verificação mensal       |
| V-13   | Backup de banco de dados sem criptografia | 3 | 3 | 3 | **27**  | 🟢 Baixa   | Criptografar backups em repouso       |
| V-14   | Falta de política de senhas fortes     | 2 | 3 | 3 | **18**    | 🟢 Baixa   | Política mínima: 12 chars + complexidade |
| V-15   | Ausência de treinamento de segurança   | 2 | 2 | 3 | **12**    | 🟢 Baixa   | Programa de conscientização anual     |

---

## 3. Ranking de Prioridades Consolidado

```
PRIORIDADE      SCORE    VULNERABILIDADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 CRÍTICA     125      V-01: SQL Injection
🔴 CRÍTICA     125      V-02: Credenciais hardcoded
🔴 CRÍTICA     100      V-03: Dados pessoais sem criptografia
🔴 CRÍTICA     100      V-04: JWT sem validação adequada
────────────────────────────────────────────────────────
🟠 ALTA         64      V-05: Ausência de 2FA
🟠 ALTA         64      V-06: DDoS sem rate limiting
🟠 ALTA         64      V-07: IDOR nos endpoints
🟠 ALTA         60      V-08: Ausência de HTTPS/TLS
────────────────────────────────────────────────────────
🟡 MÉDIA        48      V-09: Erros verbosos
🟡 MÉDIA        48      V-10: Ausência de logs de auditoria
🟡 MÉDIA        36      V-11: Sessões sem timeout
🟡 MÉDIA        36      V-12: Dependências com CVEs
────────────────────────────────────────────────────────
🟢 BAIXA        27      V-13: Backup sem criptografia
🟢 BAIXA        18      V-14: Política de senhas fraca
🟢 BAIXA        12      V-15: Falta de treinamento
```

---

## 4. Plano de Tratamento por Prioridade

### 4.1 Vulnerabilidades Críticas (Score ≥ 100) — Tratar Imediatamente

| Vuln. | Ação Principal                         | Responsável       | Prazo     |
|-------|----------------------------------------|-------------------|-----------|
| V-01  | Usar Prepared Statements em todas as queries; adicionar WAF | Dev Back-end | Sprint 1 |
| V-02  | Varrer repositório com TruffleHog; mover credenciais para vault | Dev/DevOps | Imediato |
| V-03  | Criptografar campos sensíveis com AES-256 antes de salvar | Dev Back-end | Sprint 2 |
| V-04  | Validar assinatura JWT com biblioteca oficial; expiração de 15 min | Dev Back-end | Sprint 1 |

### 4.2 Vulnerabilidades Altas (Score 60–99) — Tratar em Curto Prazo

| Vuln. | Ação Principal                         | Responsável       | Prazo     |
|-------|----------------------------------------|-------------------|-----------|
| V-05  | Integrar biblioteca pyotp para TOTP; obrigatório para admin | Dev Back-end | Sprint 3 |
| V-06  | Configurar nginx rate limiting + Cloudflare Free plan | DevOps | Sprint 2 |
| V-07  | Verificar ownership em cada endpoint (user_id == resource.owner_id) | Dev Back-end | Sprint 2 |
| V-08  | Habilitar HSTS + redirecionar HTTP para HTTPS | DevOps | Sprint 1 |

### 4.3 Vulnerabilidades Médias (Score 30–59) — Tratar em Médio Prazo

| Vuln. | Ação Principal                         | Responsável       | Prazo     |
|-------|----------------------------------------|-------------------|-----------|
| V-09  | Criar middleware global de tratamento de erros | Dev Back-end | Sprint 3 |
| V-10  | Implementar tabela de audit_log no banco | Dev Back-end | Sprint 3 |
| V-11  | Configurar JWT com sliding session e timeout de inatividade | Dev Back-end | Sprint 4 |
| V-12  | Configurar Dependabot no GitHub + revisão mensal | DevOps | Sprint 1 |

### 4.4 Vulnerabilidades Baixas (Score < 30) — Monitorar

| Vuln. | Ação Principal                         | Responsável       | Prazo     |
|-------|----------------------------------------|-------------------|-----------|
| V-13  | Script de backup com GPG encryption | DevOps | Sprint 5 |
| V-14  | Adicionar validação de força de senha no cadastro | Dev Front-end | Sprint 4 |
| V-15  | Criar material de onboarding sobre segurança | Dev Lead | Sprint 6 |

---

## 5. Gráfico de Risco (Mapa de Calor)

```
    GRAVIDADE
    5 │ V-02 V-01  .    .   V-03
    4 │  .    .   V-07 V-05 V-04
    3 │  .   V-09  .   V-11  .
    2 │  .    .   V-14  .    .
    1 │  .    .    .    .    .
      └─────────────────────────
        1    2    3    4    5   → URGÊNCIA
        
  🔴 Score ≥ 100 (Crítico)
  🟠 Score 60–99 (Alto)
  🟡 Score 30–59 (Médio)
  🟢 Score < 30  (Baixo)
```

---

## 6. Reavaliação e Monitoramento

| Ação                                      | Frequência      |
|-------------------------------------------|-----------------|
| Revisão da Matriz GUT                     | Trimestral      |
| Varredura de vulnerabilidades (OWASP ZAP) | Mensal          |
| Penetration Testing                       | Semestral       |
| Revisão de dependências (CVE scan)        | A cada release  |
| Auditoria de logs de acesso               | Semanal         |

---

*Referências: OWASP Top 10 (2021), NIST Cybersecurity Framework, ISO/IEC 27001:2022*
