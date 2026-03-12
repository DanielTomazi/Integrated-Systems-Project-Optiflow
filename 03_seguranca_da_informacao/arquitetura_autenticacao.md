# Arquitetura de Autenticação e Controle de Acesso — OptiFlow

**Disciplina:** Segurança da Informação  
**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026

---

## 1. Visão Geral da Arquitetura

A arquitetura de segurança da OptiFlow é baseada nos princípios de **Defense in Depth** (Defesa em Profundidade), com múltiplas camadas de proteção:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CAMADAS DE SEGURANÇA OPTIFLOW                     │
│                                                                       │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────────────────┐  │
│  │   CAMADA 1  │   │   CAMADA 2   │   │        CAMADA 3          │  │
│  │  Perímetro  │   │  Autenticação│   │   Autorização / RBAC     │  │
│  │             │   │              │   │                          │  │
│  │ • HTTPS/TLS │   │ • Hash Senha │   │ • Papéis: Admin, Gestor, │  │
│  │ • WAF       │   │ • JWT        │   │   Motorista, Visualizador│  │
│  │ • Rate Limit│   │ • 2FA (TOTP) │   │ • Verify ownership       │  │
│  └─────────────┘   └──────────────┘   └──────────────────────────┘  │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────────┐│
│  │                        CAMADA 4: DADOS                           ││
│  │  • Criptografia em repouso (AES-256)                             ││
│  │  • Criptografia em trânsito (TLS 1.3)                           ││
│  │  • Mascaramento de dados sensíveis nos logs                      ││
│  └──────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Hash de Senhas

### 2.1 Algoritmo Recomendado: bcrypt / Argon2

A OptiFlow utiliza **bcrypt** (fator de custo = 12) para o hash de senhas, com suporte futuro para **Argon2id** (vencedor do Password Hashing Competition).

**Por que não MD5 ou SHA-1?**
- MD5 e SHA-1 são algoritmos de hash genéricos, não projetados para senhas
- São extremamente rápidos, facilitando ataques de força bruta
- Não possuem salt embutido, tornando-os vulneráveis a rainbow tables

### 2.2 Implementação em Python

```python
# ── HASH DE SENHA ──────────────────────────────────────────────────
# Dependência: pip install bcrypt

import bcrypt

def gerar_hash_senha(senha_plaintext: str) -> str:
    """
    Gera o hash seguro de uma senha usando bcrypt.
    O salt é gerado e incorporado automaticamente no hash.
    
    Args:
        senha_plaintext: Senha em texto plano (NUNCA armazenar este valor)
    
    Returns:
        Hash da senha para armazenamento no banco de dados
    """
    salt = bcrypt.gensalt(rounds=12)  # Fator de custo 12 (recomendado 2026)
    hash_bytes = bcrypt.hashpw(senha_plaintext.encode('utf-8'), salt)
    return hash_bytes.decode('utf-8')


def verificar_senha(senha_plaintext: str, hash_armazenado: str) -> bool:
    """
    Verifica se a senha fornecida corresponde ao hash armazenado.
    Implementa comparação em tempo constante (timing-safe).
    
    Args:
        senha_plaintext: Senha fornecida pelo usuário no login
        hash_armazenado: Hash recuperado do banco de dados
    
    Returns:
        True se a senha estiver correta, False caso contrário
    """
    return bcrypt.checkpw(
        senha_plaintext.encode('utf-8'),
        hash_armazenado.encode('utf-8')
    )


# ── EXEMPLO DE USO ──
# hash_db = gerar_hash_senha("MinhaSenhaForte@2026")
# # Armazenar 'hash_db' — NUNCA 'MinhaSenhaForte@2026'
#
# login_ok = verificar_senha("MinhaSenhaForte@2026", hash_db)
# # login_ok = True
```

### 2.3 Política de Senhas

| Requisito                     | Regra                               |
|-------------------------------|-------------------------------------|
| Tamanho mínimo                | 12 caracteres                       |
| Letras maiúsculas             | Pelo menos 1                        |
| Letras minúsculas             | Pelo menos 1                        |
| Números                       | Pelo menos 1                        |
| Caracteres especiais          | Pelo menos 1 (!@#$%^&*)             |
| Senhas proibidas              | Bloquear as 10.000 senhas mais comuns|
| Reutilização                  | Bloquear últimas 5 senhas           |
| Validade                      | Expirar após 90 dias (usuários admin)|

---

## 3. Autenticação com JWT (JSON Web Token)

### 3.1 Fluxo de Autenticação

```
Cliente                    Servidor OptiFlow               Banco de Dados
  │                               │                               │
  │  POST /auth/login             │                               │
  │  {email, senha}               │                               │
  │───────────────────────────────►                               │
  │                               │  SELECT * WHERE email=?       │
  │                               │───────────────────────────────►
  │                               │  ◄─ {hash_senha, user_id, role}
  │                               │                               │
  │                               │  bcrypt.checkpw() ✓           │
  │                               │                               │
  │  ◄─ {access_token, refresh_token}                             │
  │                               │                               │
  │  GET /api/rotas               │                               │
  │  Authorization: Bearer <AT>   │                               │
  │───────────────────────────────►                               │
  │                               │  Verificar assinatura JWT ✓   │
  │                               │  Verificar expiração ✓        │
  │                               │  Verificar role ✓             │
  │  ◄─ {dados das rotas}         │                               │
```

### 3.2 Estrutura do JWT OptiFlow

```json
// HEADER
{
  "alg": "HS256",
  "typ": "JWT"
}

// PAYLOAD (claims)
{
  "sub": "user_id_42",
  "email": "daniel@optiflow.com",
  "role": "gestor",
  "empresa_id": 7,
  "iat": 1735689600,
  "exp": 1735690500,
  "jti": "uuid-único-para-este-token"
}

// SIGNATURE
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  SECRET_KEY_512_BITS
)
```

### 3.3 Configurações de Segurança do JWT

| Parâmetro               | Valor Recomendado                          |
|-------------------------|--------------------------------------------|
| Algoritmo               | HS256 (interno) ou RS256 (multi-serviço)  |
| Tempo de vida (access)  | 15 minutos                                 |
| Tempo de vida (refresh) | 7 dias                                     |
| Chave secreta           | Mínimo 512 bits gerados aleatoriamente     |
| Campos obrigatórios     | sub, exp, iat, jti (ID único do token)    |
| Blocklist               | Invalidar tokens no logout (via Redis)     |

### 3.4 Implementação em Python

```python
# ── JWT ─────────────────────────────────────────────────────────────
# Dependência: pip install PyJWT cryptography

import jwt
import uuid
from datetime import datetime, timedelta, timezone

SECRET_KEY = "seu_secret_key_de_512_bits_aqui"  # Usar variável de ambiente
ALGORITHM  = "HS256"

def gerar_access_token(user_id: int, role: str, empresa_id: int) -> str:
    """Gera um JWT de acesso com expiração de 15 minutos."""
    payload = {
        "sub":       str(user_id),
        "role":      role,
        "empresa_id": empresa_id,
        "iat":       datetime.now(timezone.utc),
        "exp":       datetime.now(timezone.utc) + timedelta(minutes=15),
        "jti":       str(uuid.uuid4()),   # ID único — permite revogação
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(token: str) -> dict:
    """
    Verifica e decodifica um JWT.
    Lança exceção se o token for inválido, expirado ou adulterado.
    """
    try:
        payload = jwt.decode(
            token, SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"require": ["exp", "iat", "sub", "jti"]}
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado. Faça login novamente.")
    except jwt.InvalidTokenError as e:
        raise ValueError(f"Token inválido: {e}")
```

---

## 4. Autenticação em Dois Fatores (2FA — TOTP)

### 4.1 Visão Geral

A OptiFlow implementa **TOTP (Time-based One-Time Password)**, compatível com:
- Google Authenticator
- Microsoft Authenticator
- Authy

O 2FA é **obrigatório** para contas com papel `admin` e `gestor`, e **opcional** para `motorista`.

### 4.2 Fluxo de Ativação do 2FA

```
1. Usuário acessa Configurações > Segurança > Ativar 2FA
2. Sistema gera secret TOTP (Base32, 160 bits)
3. Sistema exibe QR Code para o usuário escanear
4. Usuário insere o código gerado pelo autenticador
5. Sistema valida o código → 2FA ativado
6. Sistema exibe 8 códigos de backup (imprimir/guardar)
```

### 4.3 Implementação em Python

```python
# ── 2FA / TOTP ───────────────────────────────────────────────────────
# Dependência: pip install pyotp qrcode

import pyotp
import qrcode
import io
import base64

def gerar_secret_totp() -> str:
    """Gera um secret TOTP único para o usuário."""
    return pyotp.random_base32()


def gerar_qr_code(email: str, secret: str, issuer: str = "OptiFlow") -> str:
    """
    Gera o URI para QR Code que o usuário escaneia no autenticador.
    Retorna o URI no formato otpauth://
    """
    totp = pyotp.TOTP(secret)
    uri  = totp.provisioning_uri(name=email, issuer_name=issuer)
    return uri


def verificar_codigo_totp(secret: str, codigo_informado: str) -> bool:
    """
    Verifica se o código TOTP informado pelo usuário é válido.
    Aceita janela de ±1 período (30s) para compensar pequenas diferenças de relógio.
    """
    totp = pyotp.TOTP(secret)
    return totp.verify(codigo_informado, valid_window=1)
```

### 4.4 Fluxo de Login com 2FA

```
POST /auth/login
{email, senha}
  │
  ├─ Senha incorreta? → 401 (mensagem genérica)
  │
  └─ Senha correta?
       │
       ├─ 2FA desativado? → Retorna JWT diretamente
       │
       └─ 2FA ativado?
            │
            └─ Retorna token temporário (2FA pending, 5 min)
                 │
                 └─ POST /auth/2fa/verify {codigo_totp}
                      │
                      ├─ Código inválido? → 401 + registra tentativa
                      └─ Código válido?  → Retorna JWT de acesso
```

---

## 5. Controle de Acesso por Papel (RBAC)

### 5.1 Papéis (Roles)

| Papel          | Descrição                                          |
|----------------|----------------------------------------------------|
| `admin`        | Acesso total ao sistema, incluindo configurações   |
| `gestor`       | Gerencia pedidos, motoristas e visualiza relatórios|
| `motorista`    | Visualiza suas próprias rotas e atualiza status    |
| `visualizador` | Somente leitura de relatórios e KPIs               |

### 5.2 Matriz de Permissões

| Recurso / Ação                  | admin | gestor | motorista | visualizador |
|---------------------------------|:-----:|:------:|:---------:|:------------:|
| Criar/editar usuários           | ✅    | ❌     | ❌        | ❌           |
| Visualizar todos os pedidos     | ✅    | ✅     | ❌        | ✅           |
| Visualizar apenas próprios pedidos | ✅ | ✅     | ✅        | ❌           |
| Criar/editar pedidos            | ✅    | ✅     | ❌        | ❌           |
| Executar otimização de rotas    | ✅    | ✅     | ❌        | ❌           |
| Visualizar KPIs / Relatórios    | ✅    | ✅     | ❌        | ✅           |
| Exportar dados                  | ✅    | ✅     | ❌        | ❌           |
| Configurações do sistema        | ✅    | ❌     | ❌        | ❌           |
| Atualizar status de entrega     | ✅    | ✅     | ✅        | ❌           |
| Excluir registros               | ✅    | ❌     | ❌        | ❌           |

### 5.3 Implementação do RBAC em Python

```python
# ── RBAC ─────────────────────────────────────────────────────────────
from functools import wraps

# Mapa de permissões por papel
PERMISSOES = {
    "admin":       {"pedidos:read", "pedidos:write", "pedidos:delete",
                    "usuarios:read", "usuarios:write", "relatorios:read",
                    "otimizacao:execute", "config:write"},
    "gestor":      {"pedidos:read", "pedidos:write", "relatorios:read",
                    "otimizacao:execute", "motoristas:read"},
    "motorista":   {"pedidos:read_own", "entregas:update_status"},
    "visualizador":{"relatorios:read", "kpis:read"},
}


def requer_permissao(permissao: str):
    """
    Decorator para verificar se o usuário logado tem a permissão necessária.
    Deve ser usado como decorator em endpoints da API.
    
    Exemplo de uso:
        @app.get("/api/pedidos")
        @requer_permissao("pedidos:read")
        def listar_pedidos(usuario_atual):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 'usuario_atual' deve ser injetado pelo middleware de autenticação
            usuario_atual = kwargs.get("usuario_atual")
            if not usuario_atual:
                raise PermissionError("Usuário não autenticado.")
            
            role = usuario_atual.get("role", "")
            permissoes_do_role = PERMISSOES.get(role, set())
            
            if permissao not in permissoes_do_role:
                raise PermissionError(
                    f"Acesso negado. Permissão '{permissao}' necessária."
                )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

---

## 6. Resumo das Boas Práticas de Segurança

| Área                    | Prática Obrigatória                                          |
|-------------------------|--------------------------------------------------------------|
| Senhas                  | bcrypt com rounds=12; nunca armazenar em plaintext           |
| Tokens JWT              | Expiração curta; validação de assinatura; revogação no logout|
| 2FA                     | TOTP obrigatório para admin/gestor; backup codes             |
| HTTPS                   | TLS 1.2+ obrigatório; HSTS habilitado                        |
| RBAC                    | Menor privilégio; verificar ownership de recursos            |
| Credenciais             | Sempre via variáveis de ambiente ou secret manager           |
| Logs                    | Nunca logar senhas, tokens ou dados pessoais completos       |
| Inputs                  | Validar e sanitizar todos os inputs da API                   |

---

*Referências: OWASP Authentication Cheat Sheet, JWT Best Practices (RFC 8725), NIST SP 800-63B*
