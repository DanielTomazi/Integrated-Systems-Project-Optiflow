# Mapeamento de Ameaças — OptiFlow Logística Inteligente

**Disciplina:** Segurança da Informação  
**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026  
**Metodologia:** STRIDE (Microsoft Threat Modeling)

---

## 1. Introdução

O mapeamento de ameaças é um processo sistemático para identificar, categorizar e avaliar as potenciais ameaças à segurança de um sistema. Para a plataforma OptiFlow, este mapeamento segue a metodologia **STRIDE**, que categoriza ameaças em seis tipos:

| Inicial | Categoria                         | Descrição                                              |
|---------|-----------------------------------|--------------------------------------------------------|
| **S**   | Spoofing (Falsificação)           | Fingir ser outra entidade (usuário, sistema)           |
| **T**   | Tampering (Adulteração)           | Modificar dados ou código sem autorização              |
| **R**   | Repudiation (Repúdio)             | Negar ter realizado uma ação                           |
| **I**   | Information Disclosure (Exposição)| Acessar informações confidenciais sem autorização      |
| **D**   | Denial of Service (DoS)           | Negar serviço a usuários legítimos                     |
| **E**   | Elevation of Privilege (Escalada) | Obter permissões além do autorizado                    |

---

## 2. Ativos Críticos do Sistema

| ID    | Ativo                             | Descrição                                      | Classificação |
|-------|-----------------------------------|------------------------------------------------|---------------|
| A-01  | Banco de Dados de Pedidos         | Dados logísticos de clientes e entregas        | Confidencial  |
| A-02  | Credenciais de Usuários           | Senhas e tokens de autenticação                | Secreto       |
| A-03  | Dados Pessoais (LGPD)             | CPF, endereço, telefone de clientes e motori.  | Confidencial  |
| A-04  | API de Roteirização               | Endpoints de otimização de rotas               | Restrito      |
| A-05  | Painel Administrativo             | Interface de gestão da plataforma              | Restrito      |
| A-06  | Logs de Operação                  | Registros de atividades do sistema             | Interno       |
| A-07  | Configurações de Infraestrutura   | Variáveis de ambiente, chaves de API           | Secreto       |

---

## 3. Diagrama de Fluxo de Dados (DFD — Simplificado)

```
┌──────────────┐   HTTPS    ┌──────────────────┐   SQL     ┌─────────────┐
│   Usuário    │ ─────────► │  API OptiFlow     │ ────────► │  Banco de   │
│  (Navegador/ │            │  (Servidor Web)   │           │   Dados     │
│   App Móvel) │ ◄───────── │                  │ ◄──────── │             │
└──────────────┘            └────────┬─────────┘           └─────────────┘
                                     │
                              ┌──────▼──────┐
                              │  Serviço de │
                              │  Otimização │
                              │  (PuLP/OR)  │
                              └─────────────┘
                                     │
                              ┌──────▼──────┐
                              │   Serviço   │
                              │  de Email/  │
                              │    SMS      │
                              └─────────────┘
```

---

## 4. Catálogo de Ameaças STRIDE

### 4.1 Spoofing — Falsificação de Identidade

| ID     | Vetor de Ataque         | Descrição                                                                   | Impacto  |
|--------|-------------------------|-----------------------------------------------------------------------------|----------|
| A-S-01 | Credential Stuffing     | Atacante usa listas de senhas vazadas para tentar acessar contas            | Alto     |
| A-S-02 | Session Hijacking       | Roubo de token de sessão via XSS ou sniffing de rede                       | Alto     |
| A-S-03 | Phishing                | E-mail falso fingindo ser da OptiFlow para capturar credenciais             | Médio    |
| A-S-04 | API Key Spoofing        | Uso indevido de chaves de API vazadas para autenticar como serviço legítimo | Alto     |

### 4.2 Tampering — Adulteração de Dados

| ID     | Vetor de Ataque         | Descrição                                                                   | Impacto  |
|--------|-------------------------|-----------------------------------------------------------------------------|----------|
| A-T-01 | SQL Injection           | Inserção de comandos SQL maliciosos nos campos de entrada da API            | Crítico  |
| A-T-02 | Man-in-the-Middle       | Interceptação e modificação de dados em trânsito sem HTTPS/TLS adequado    | Alto     |
| A-T-03 | Parameter Tampering     | Manipulação de parâmetros da requisição HTTP para alterar resultados        | Médio    |
| A-T-04 | Dados de Rota Adulterados | Modificação maliciosa dos dados de otimização de rotas                    | Alto     |

### 4.3 Repudiation — Repúdio

| ID     | Vetor de Ataque         | Descrição                                                                   | Impacto  |
|--------|-------------------------|-----------------------------------------------------------------------------|----------|
| A-R-01 | Logs Insuficientes      | Ausência de audit trail para rastrear ações críticas do sistema             | Médio    |
| A-R-02 | Ausência de Assinatura  | Transações sem assinatura digital permitem negar autoria de operações       | Médio    |

### 4.4 Information Disclosure — Exposição de Informações

| ID     | Vetor de Ataque              | Descrição                                                              | Impacto  |
|--------|------------------------------|------------------------------------------------------------------------|----------|
| A-I-01 | SQL Injection (read)         | Extração de dados confidenciais via injeção SQL                        | Crítico  |
| A-I-02 | Vazamento de Credenciais     | Hardcoding de senhas no código-fonte ou em repositórios públicos       | Crítico  |
| A-I-03 | API Verbose Error Messages   | Mensagens de erro detalhadas expõem estrutura interna do sistema       | Médio    |
| A-I-04 | Dados Pessoais sem Criptografia | Armazenamento de dados pessoais em texto plano no banco de dados    | Alto     |
| A-I-05 | Exposição de Variáveis de Env| Arquivo `.env` ou configurações expostos em repositório público        | Crítico  |

### 4.5 Denial of Service — Negação de Serviço

| ID     | Vetor de Ataque              | Descrição                                                              | Impacto  |
|--------|------------------------------|------------------------------------------------------------------------|----------|
| A-D-01 | DDoS na API                  | Flood de requisições para saturar o servidor da API                    | Alto     |
| A-D-02 | Slowloris Attack             | Manter conexões abertas até esgotar o pool de conexões                 | Alto     |
| A-D-03 | Resource Exhaustion          | Requisições de otimização com parâmetros extremos sobrecarregam CPU    | Médio    |
| A-D-04 | Database Connection Flooding | Abertura massiva de conexões ao banco de dados                         | Alto     |

### 4.6 Elevation of Privilege — Escalada de Privilégios

| ID     | Vetor de Ataque              | Descrição                                                              | Impacto  |
|--------|------------------------------|------------------------------------------------------------------------|----------|
| A-E-01 | IDOR (Insecure Direct Object) | Acesso a recursos de outros usuários via manipulação de IDs            | Alto     |
| A-E-02 | JWT Tampering                | Modificação do payload do token JWT para elevar permissões             | Crítico  |
| A-E-03 | Broken Access Control        | Usuário comum acessa endpoints administrativos                         | Alto     |
| A-E-04 | Path Traversal               | Acesso a arquivos do servidor via manipulação de caminho               | Médio    |

---

## 5. Detalhamento das Ameaças Críticas

### 5.1 SQL Injection (A-T-01 / A-I-01)

**Cenário de Ataque:**
```
URL legítima : /api/pedidos?regiao=Centro
URL maliciosa: /api/pedidos?regiao=Centro' OR '1'='1
```

**Impacto:** Exposição de todos os dados do banco de dados, incluindo dados pessoais de clientes e motoristas, potencialmente violando a LGPD com multas de até R$ 50 milhões.

**Controles Mitigadores:**
- Uso exclusivo de Prepared Statements / Parameterized Queries
- Validação e sanitização de todas as entradas
- Princípio do menor privilégio no usuário de banco de dados
- ORM com proteção nativa (SQLAlchemy, Django ORM)

---

### 5.2 Vazamento de Credenciais (A-I-02 / A-I-05)

**Cenário de Ataque:**
```python
# VULNERÁVEL (NUNCA FAZER):
DATABASE_URL = "postgresql://admin:senha123@prod-db.optiflow.com/optiflow"

# SEGURO:
DATABASE_URL = os.environ.get("DATABASE_URL")
```

**Impacto:** Acesso total ao banco de dados de produção, comprometimento da plataforma e violação de dados de todos os clientes e motoristas.

**Controles Mitigadores:**
- Variáveis de ambiente para credenciais (`.env` no `.gitignore`)
- Uso de secret managers (AWS Secrets Manager, HashiCorp Vault)
- Rotação periódica de credenciais
- Scan automático de secrets no repositório (git-secrets, TruffleHog)

---

### 5.3 Indisponibilidade de Servidores (A-D-01)

**Cenário de Ataque:**
- Atacante utiliza botnet para enviar 100.000 req/s à API de roteirização
- Servidor satura e nega serviço a todos os clientes legítimos
- Empresa sofre perda de receita e dano à reputação

**Impacto:** Interrupção completa do serviço, SLA violado, potencial rescisão de contratos.

**Controles Mitigadores:**
- WAF (Web Application Firewall) com detecção de DDoS
- Rate Limiting por IP e por usuário autenticado
- CDN com proteção DDoS (Cloudflare, AWS Shield)
- Auto-scaling da infraestrutura em nuvem
- Circuit Breaker pattern na API

---

### 5.4 JWT Tampering (A-E-02)

**Cenário de Ataque:**
```
Token JWT legítimo (base64decode do payload):
  {"user_id": 42, "role": "driver", "exp": 1735689600}

Token adulterado:
  {"user_id": 42, "role": "admin", "exp": 9999999999}
```

**Impacto:** Usuário comum obtém acesso de administrador, podendo alterar dados de todos os clientes e motoristas.

**Controles Mitigadores:**
- Algoritmo HS256 ou RS256 com chave secreta forte
- Verificação rigorosa da assinatura no servidor
- Tokens de curta duração (15–60 min) com refresh token
- Blocklist de tokens revogados (Redis)

---

## 6. Superfície de Ataque Consolidada

| Camada          | Ameaças Identificadas | Nível Geral |
|-----------------|-----------------------|-------------|
| Autenticação    | A-S-01, A-S-02, A-E-02| Alto        |
| API / Endpoints | A-T-01, A-T-03, A-E-01| Crítico     |
| Dados em repouso| A-I-02, A-I-04, A-I-05| Alto        |
| Dados em trânsito| A-T-02, A-I-03       | Médio       |
| Disponibilidade | A-D-01, A-D-02, A-D-03| Alto        |
| Controle acesso | A-E-01, A-E-03, A-E-04| Alto        |

---

*Este mapeamento deve ser revisado a cada nova funcionalidade adicionada ao sistema e ao menos anualmente.*  
*Referências: OWASP Top 10 (2021), STRIDE (Microsoft SDL), NIST SP 800-30*
