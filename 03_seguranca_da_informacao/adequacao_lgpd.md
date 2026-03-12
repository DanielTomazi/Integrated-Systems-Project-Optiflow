# Adequação à LGPD — OptiFlow Logística Inteligente

**Disciplina:** Segurança da Informação  
**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Referência Legal:** Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais)

---

## 1. Introdução

A **Lei Geral de Proteção de Dados Pessoais (LGPD)**, em vigor desde setembro de 2020, regula o tratamento de dados pessoais por pessoas físicas e jurídicas em território brasileiro. Este documento descreve como a **OptiFlow Logística Inteligente** se adequa à legislação, garantindo os direitos dos titulares de dados e adotando medidas técnicas e organizacionais para proteger as informações tratadas.

### 1.1 Definições Importantes (Art. 5º, LGPD)

| Termo                  | Definição                                                                       |
|------------------------|---------------------------------------------------------------------------------|
| **Dado pessoal**       | Informação relacionada à pessoa natural identificada ou identificável            |
| **Dado sensível**      | Origem racial, convicção religiosa, dado genético, biométrico, saúde, etc.       |
| **Titular**            | Pessoa natural a quem se referem os dados pessoais tratados                     |
| **Controlador**        | Quem decide como e por que os dados são tratados (**OptiFlow**)                 |
| **Operador**           | Quem trata dados em nome do controlador (ex.: AWS, provedores SaaS)             |
| **ANPD**               | Autoridade Nacional de Proteção de Dados                                        |
| **Tratamento**         | Qualquer operação com dados: coleta, uso, armazenamento, compartilhamento, etc. |

---

## 2. Inventário de Dados Pessoais Coletados

A OptiFlow coleta dados de três grupos de titulares:

### 2.1 Dados dos Usuários da Plataforma (Gestores/Admin)

| Dado                    | Categoria       | Finalidade                           | Armazenamento        |
|-------------------------|-----------------|--------------------------------------|----------------------|
| Nome completo           | Pessoal comum   | Identificação na plataforma          | Banco de dados       |
| Endereço de e-mail      | Pessoal comum   | Login, notificações                  | Banco de dados       |
| Senha (hash bcrypt)     | Pessoal comum   | Autenticação                         | Banco de dados       |
| Foto de perfil          | Pessoal comum   | Personalização da interface          | Armazenamento S3/CDN |
| Número de telefone      | Pessoal comum   | 2FA via SMS (opcional)               | Banco de dados       |
| IP de acesso            | Pessoal comum   | Segurança e auditoria de logs        | Logs (90 dias)       |
| Data/hora de login      | Pessoal comum   | Auditoria de segurança               | Logs (90 dias)       |

### 2.2 Dados dos Motoristas

| Dado                         | Categoria       | Finalidade                              | Armazenamento  |
|------------------------------|-----------------|-----------------------------------------|----------------|
| Nome completo                | Pessoal comum   | Identificação e alocação de rotas       | Banco de dados |
| CPF                          | Pessoal comum   | Identificação legal                     | Banco de dados |
| CNH (número e validade)      | Pessoal comum   | Habilitação para entrega                | Banco de dados |
| Endereço de e-mail           | Pessoal comum   | Comunicação e login                     | Banco de dados |
| Localização GPS em tempo real| Pessoal comum   | Otimização de rotas ativas              | Temporário (RAM)|
| Histórico de localização     | Pessoal comum   | KPIs de entrega, auditoria             | Banco de dados |
| Avaliações de performance    | Pessoal comum   | Gestão de qualidade                     | Banco de dados |

### 2.3 Dados dos Clientes/Destinatários de Entregas

| Dado                         | Categoria       | Finalidade                              | Armazenamento  |
|------------------------------|-----------------|-----------------------------------------|----------------|
| Nome do destinatário         | Pessoal comum   | Identificação da entrega                | Banco de dados |
| Endereço de entrega          | Pessoal comum   | Roteirização e rastreamento             | Banco de dados |
| Telefone de contato          | Pessoal comum   | Avisos de entrega ao destinatário       | Banco de dados |
| E-mail                       | Pessoal comum   | Notificação de status do pedido         | Banco de dados |
| Histórico de pedidos         | Pessoal comum   | Análise de dados (anonimizado)          | Banco de dados |

> **Nota:** A OptiFlow **não coleta dados sensíveis** conforme definição do Art. 5º, II da LGPD.

---

## 3. Bases Legais para o Tratamento (Art. 7º e Art. 11, LGPD)

| Atividade de Tratamento                         | Base Legal LGPD                          | Artigo    |
|-------------------------------------------------|------------------------------------------|-----------|
| Login e autenticação de usuários                | Execução de contrato                     | Art. 7º, V|
| Rastreamento de motoristas durante entregas     | Execução de contrato                     | Art. 7º, V|
| Envio de notificações de status ao destinatário | Legítimo interesse do controlador        | Art. 7º, IX|
| Análise de KPIs e relatórios gerenciais         | Execução de contrato / legítimo interesse| Art. 7º, V e IX|
| Armazenamento de logs de segurança              | Cumprimento de obrigação legal           | Art. 7º, II|
| Newsletter e comunicações de marketing          | Consentimento                            | Art. 7º, I|
| Compartilhamento com operadores (AWS, etc.)     | Execução de contrato                     | Art. 7º, V|

---

## 4. Direitos dos Titulares (Art. 18, LGPD)

A plataforma OptiFlow disponibiliza os seguintes mecanismos para exercício dos direitos dos titulares:

| Direito                           | Como exercer                                            | Prazo de resposta |
|-----------------------------------|---------------------------------------------------------|-------------------|
| ✅ Confirmação de tratamento      | Painel de privacidade na conta                          | Imediato           |
| ✅ Acesso aos dados               | Botão "Exportar meus dados" (formato JSON/PDF)          | Até 15 dias úteis  |
| ✅ Correção de dados              | Edição no perfil da conta                               | Imediato           |
| ✅ Anonimização ou bloqueio       | Solicitação via e-mail: privacidade@optiflow.com        | Até 15 dias úteis  |
| ✅ Portabilidade                  | "Exportar meus dados" (formato CSV padronizado)         | Até 15 dias úteis  |
| ✅ Exclusão de dados              | "Excluir minha conta" no painel de configurações        | Até 30 dias úteis  |
| ✅ Informação sobre compartilhamento | Política de Privacidade pública                      | Consulta imediata  |
| ✅ Revogação de consentimento     | Toggle "Comunicações de marketing" no painel            | Imediato           |
| ✅ Oposição ao tratamento         | Solicitação via e-mail: privacidade@optiflow.com        | Até 15 dias úteis  |

---

## 5. Mecanismo de Exclusão de Dados

### 5.1 Processo de Exclusão (Right to Erasure)

```
Titular solicita exclusão
         │
         ▼
Sistema verifica pendências
(ex.: entregas em andamento)
         │
    ┌────┴────────────────────────────┐
    │ Pendências?                     │
    ├─ Sim → Notificar titular        │
    │         aguardar conclusão      │
    │                                 │
    └─ Não → Iniciar processo         │
              de anonimização         │
              e exclusão              │
              ─────────────────────── │
              1. Anonimizar dados em  │
                 tabelas de auditoria │
              2. Excluir dados pessoais│
                 identificáveis       │
              3. Manter apenas dados  │
                 estatísticos         │
                 (inidentificáveis)   │
              4. Registrar log da     │
                 exclusão (sem dados  │
                 pessoais)            │
              5. Notificar titular    │
```

### 5.2 Pseudocódigo do Mecanismo de Exclusão

```python
# ── EXCLUSÃO DE DADOS PESSOAIS (LGPD Art. 18, VI) ────────────────────
# Este pseudocódigo ilustra a lógica de exclusão. Adaptar ao ORM/DB real.

def processar_exclusao_titular(usuario_id: int) -> dict:
    """
    Remove dados pessoais identificáveis de um usuário.
    Mantém registros anonimizados para fins estatísticos/auditoria.
    
    Etapas:
    1. Verificar pendências (pedidos em aberto)
    2. Anonimizar registros históricos (manter estatísticas)
    3. Excluir dados pessoais identificáveis
    4. Invalidar todos os tokens de acesso
    5. Registrar evento de exclusão (sem dados pessoais)
    6. Enviar confirmação ao titular
    """
    # Etapa 1: Verificar pendências
    pendencias = verificar_pedidos_em_aberto(usuario_id)
    if pendencias:
        return {"status": "pendente", "mensagem": f"{len(pendencias)} pedidos em aberto. Aguarde a conclusão."}
    
    # Etapa 2: Anonimizar histórico de pedidos (manter KPIs)
    anonimizar_pedidos(usuario_id, valor_anonimo="[DELETADO]")
    
    # Etapa 3: Excluir dados da tabela de usuários
    excluir_usuario(usuario_id)          # Remove nome, e-mail, CPF, etc.
    excluir_dados_motorista(usuario_id)  # Remove CNH, telefone, etc.
    
    # Etapa 4: Invalidar sessões ativas
    revogar_todos_tokens(usuario_id)
    
    # Etapa 5: Registrar evento (sem PII)
    registrar_log_exclusao(
        evento="EXCLUSAO_TITULAR",
        timestamp=datetime.utcnow(),
        user_id_hash=hash_anonimo(usuario_id),  # Hash unidirecional
    )
    
    # Etapa 6: Notificar
    enviar_email_confirmacao_exclusao(email_anonimizado)
    
    return {"status": "concluido", "mensagem": "Dados excluídos com sucesso."}
```

### 5.3 Retenção de Dados

| Categoria de Dado                          | Prazo de Retenção                                  |
|--------------------------------------------|-----------------------------------------------------|
| Dados de conta ativa                       | Enquanto a conta estiver ativa                      |
| Logs de acesso e segurança                 | 90 dias (obrigação legal — Marco Civil da Internet) |
| Histórico de pedidos (anonimizado)         | 5 anos (obrigação fiscal)                           |
| Dados de localização GPS                   | 30 dias (dados brutos); 1 ano (agregados)           |
| Dados após solicitação de exclusão         | Excluídos em até 30 dias (exceto obrigação legal)   |
| Backups                                    | Purgar dados excluídos no próximo ciclo (máx. 30d)  |

---

## 6. Medidas de Segurança Implementadas

### 6.1 Medidas Técnicas (Art. 46, LGPD)

| Medida                             | Implementação                                     |
|------------------------------------|---------------------------------------------------|
| Criptografia em trânsito           | TLS 1.3 em todos os endpoints de API              |
| Criptografia em repouso            | AES-256 para dados sensíveis no banco             |
| Hash de senhas                     | bcrypt (rounds=12)                                |
| Controle de acesso                 | RBAC + autenticação multifator (2FA)              |
| Mascaramento de dados nos logs     | CPF: `***.***.***-**`; E-mail: `u***@dominio.com` |
| Segregação de ambientes            | Produção isolada de dev/staging                   |
| Teste de penetração (Pentest)      | Anual, por empresa especializada                  |

### 6.2 Medidas Organizacionais

| Medida                             | Responsável                  | Frequência     |
|------------------------------------|------------------------------|----------------|
| Treinamento em privacidade         | Gestão de RH + DPO           | Semestral      |
| Revisão da política de privacidade | DPO                          | Anual          |
| Avaliação de impacto (DPIA)        | DPO + Engenharia             | Para cada novo módulo|
| Gestão de terceiros (operadores)   | Jurídico + DPO               | Na contratação |
| Resposta a incidentes de dados     | Equipe de Segurança + DPO    | Conforme necessário|

---

## 7. Encarregado de Dados (DPO)

Conforme Art. 41 da LGPD, a OptiFlow designa um **Encarregado de Dados (DPO)**:

| Campo             | Informação                                        |
|-------------------|---------------------------------------------------|
| Nome              | *A designar na implementação real*                |
| E-mail de contato | privacidade@optiflow.com                          |
| Canais adicionais | Formulário no site > "Privacidade e Dados"        |
| Reporte           | ANPD — quando exigido por lei                     |

---

## 8. Resposta a Incidentes de Segurança (Data Breach)

Em caso de vazamento de dados pessoais, a OptiFlow seguirá este procedimento:

```
Detecção do incidente
       │
       ▼
Contenção imediata (< 1 hora)
• Isolar sistemas afetados
• Revogar credenciais comprometidas
       │
       ▼
Avaliação do impacto (< 24 horas)
• Quais dados foram expostos?
• Quantos titulares afetados?
• Qual o risco aos titulares?
       │
       ▼
Notificação (se risco relevante)
• ANPD: em até 72 horas (Art. 48, LGPD)
• Titulares afetados: em tempo razoável
       │
       ▼
Remediação e Relatório Final
• Corrigir vulnerabilidade
• Documentar lições aprendidas
• Atualizar controles de segurança
```

---

## 9. Política de Privacidade — Resumo Executivo

A **Política de Privacidade completa** da OptiFlow deve ser publicada no site e aceita pelos usuários no cadastro. Os pontos essenciais são:

1. **O que coletamos**: Dados de identificação, localização e comportamento de uso
2. **Por que coletamos**: Para fornecer o serviço de otimização logística
3. **Com quem compartilhamos**: Apenas operadores necessários (ex.: AWS), nunca para publicidade
4. **Por quanto tempo**: Conforme tabela de retenção da Seção 5.3
5. **Como protegemos**: Criptografia, controle de acesso e auditorias regulares
6. **Seus direitos**: Acesso, correção, exclusão e portabilidade (Art. 18, LGPD)
7. **Contato**: privacidade@optiflow.com

---

*Referências: LGPD (Lei 13.709/2018) | ANPD — Guia Orientativo para Definições dos Agentes de Tratamento | ABNT NBR ISO/IEC 27701:2019*
