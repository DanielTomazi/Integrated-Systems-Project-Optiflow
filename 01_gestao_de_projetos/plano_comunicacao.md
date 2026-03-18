# Plano de Comunicação — Projeto OptiFlow

**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Versão:** 1.0  
**Data:** 2026

---

## 1. Objetivo

Estabelecer a estratégia de comunicação do projeto, definindo o que, quando, como e para quem as informações serão comunicadas durante a execução do Projeto Integrador OptiFlow.

---

## 2. Partes Interessadas e Necessidades de Comunicação

| Stakeholder               | Interesse no Projeto                         | Necessidade de Informação                       | Preferência de Comunicação |
|---------------------------|----------------------------------------------|-------------------------------------------------|---------------------------|
| Daniel Tomazi (Executor)  | Acompanhar e executar o projeto              | Progresso, bloqueios, decisões                  | Autogestão via GitHub      |
| Orientador Acadêmico      | Avaliar qualidade técnica e acadêmica         | Status das entregas, dúvidas técnicas           | Reunião presencial/online  |
| Coordenador do Curso      | Verificar cumprimento dos requisitos          | Status geral, marcos atingidos                  | E-mail formal              |
| Banca Avaliadora          | Avaliar o projeto final                       | Relatório final, código, vídeo                  | Repositório GitHub + Defesa|

---

## 3. Matriz de Comunicação

| ID  | O Que Comunicar                          | Para Quem              | Por Quem          | Quando              | Como                    | Formato               |
|-----|------------------------------------------|------------------------|-------------------|---------------------|-------------------------|-----------------------|
| C01 | Kickoff — início do projeto              | Orientador, Coord.     | Daniel Tomazi     | Semana 1            | E-mail + reunião         | E-mail formal         |
| C02 | Entrega dos artefatos de gestão          | Orientador             | Daniel Tomazi     | Fim Semana 4        | E-mail + link GitHub     | Markdown no GitHub    |
| C03 | Reunião quinzenal de acompanhamento      | Orientador             | Daniel Tomazi     | Semanas pares       | Videoconferência/presen. | Ata de reunião        |
| C04 | Entrega da Análise de Dados              | Orientador             | Daniel Tomazi     | Fim Semana 9        | E-mail + link GitHub     | Scripts + Notebook    |
| C05 | Entrega da Segurança da Informação       | Orientador             | Daniel Tomazi     | Fim Semana 11       | E-mail + link GitHub     | Markdown no GitHub    |
| C06 | Entrega da Pesquisa Operacional          | Orientador             | Daniel Tomazi     | Fim Semana 14       | E-mail + link GitHub     | Scripts Python        |
| C07 | Relatório final para revisão             | Orientador             | Daniel Tomazi     | Semana 15           | E-mail com anexo         | PDF + Markdown        |
| C08 | Entrega final completa                   | Orientador, Coord.     | Daniel Tomazi     | Semana 16           | E-mail formal            | Link GitHub + PDF     |
| C09 | Disponibilização para Banca              | Banca Avaliadora       | Coordenação       | Antes da defesa     | Portal/e-mail            | ZIP do repositório    |
| C10 | Defesa/Apresentação                      | Banca, Orientador      | Daniel Tomazi     | Semana 16           | Apresentação oral        | Slides + Vídeo        |

---

## 4. Templates de Comunicação

### 4.1 Ata de Reunião Quinzenal

```
────────────────────────────────────────────────
ATA DE REUNIÃO — PROJETO INTEGRADOR OPTIFLOW
────────────────────────────────────────────────
Data:        ___/___/2026
Horário:     ___ às ___
Local:       _______________________
Participantes:
  - Daniel Tomazi de Oliveira
  - [Nome do Orientador]

PAUTA:
1. Status das entregas desde a última reunião
2. Dúvidas técnicas e acadêmicas
3. Próximos passos

ANDAMENTO:
Status atual: _________________________________
Atividades concluídas:
  1. _________________________________________
  2. _________________________________________
Atividades em andamento:
  1. _________________________________________
Bloqueios / Issues:
  1. _________________________________________

DECISÕES TOMADAS:
  1. _________________________________________

PRÓXIMOS PASSOS:
  Prazo: ___/___/2026
  1. _________________________________________
  2. _________________________________________

Assinaturas:
Daniel Tomazi: _______________
Orientador:    _______________
────────────────────────────────────────────────
```

### 4.2 E-mail de Entrega de Marco

```
Assunto: [OptiFlow] Entrega de Marco — [Nome do Marco] — [Data]

Prezado(a) Professor(a) [Nome],

Informo a conclusão das entregas do Marco [Número] do Projeto Integrador OptiFlow.

Entregas realizadas:
• [Entrega 1]
• [Entrega 2]
• [Entrega 3]

Link para o repositório GitHub:
https://github.com/[usuario]/[repositorio]

Aguardo seu feedback até [data].

Atenciosamente,
Daniel Tomazi de Oliveira
RA:
```

---

## 5. Canais de Comunicação

| Canal                    | Uso Principal                              | Tempo de Resposta Esperado |
|--------------------------|--------------------------------------------|----------------------------|
| E-mail institucional     | Comunicações formais; entregas             | 48 horas úteis             |
| GitHub (Issues)          | Controle de tarefas e dúvidas técnicas     | Autogestão                 |
| GitHub (README)          | Documentação pública do projeto            | Sempre atualizado          |
| WhatsApp / Teams         | Comunicação rápida / agendamento           | 24 horas                   |
| Reunião presencial/vídeo | Reuniões quinzenais formais                | Conforme agendamento       |

---

## 6. Gestão do Repositório GitHub como Canal de Comunicação

O repositório GitHub serve como o **canal central de comunicação técnica** do projeto:

| Funcionalidade GitHub     | Uso no Projeto                                      |
|---------------------------|-----------------------------------------------------|
| `README.md`               | Apresentação e instruções do projeto                |
| `commits`                 | Registro histórico de todas as atividades           |
| `Issues`                  | Registro de tarefas, dúvidas e bloqueios            |
| `Tags / Releases`         | Marcação dos marcos do projeto                      |
| Estrutura de pastas       | Organização clara dos artefatos por disciplina      |

---

## 7. Frequência de Atualização do GitHub

| Ação                               | Frequência Mínima    |
|------------------------------------|----------------------|
| Push de novos arquivos             | Por entrega          |
| Commit com mensagem descritiva     | Ao menos 3x/semana   |
| Atualização do README              | Por marco concluído  |
| Criação de tag de release          | Por marco (M1–M6)    |

---

## 8. Registro de Comunicações

| Data | Tipo         | Destinatário | Assunto                              | Status     |
|------|--------------|--------------|--------------------------------------|------------|
|      | E-mail       | Orientador   | Kickoff do Projeto                   | A enviar   |
|      | Reunião      | Orientador   | Acompanhamento Quinzenal 1           | A realizar |
|      | E-mail       | Orientador   | Entrega Marco 2 — Planejamento       | A enviar   |
|      | Reunião      | Orientador   | Acompanhamento Quinzenal 2           | A realizar |
|      | E-mail       | Orientador   | Entrega Marco 3 — Análise de Dados   | A enviar   |
|      | E-mail       | Orientador   | Entrega Marco 4 — Segurança          | A enviar   |
|      | E-mail       | Orientador   | Entrega Marco 5 — Pesquisa Operac.   | A enviar   |
|      | E-mail       | Coord. Curso | Entrega Final Completa               | A enviar   |
