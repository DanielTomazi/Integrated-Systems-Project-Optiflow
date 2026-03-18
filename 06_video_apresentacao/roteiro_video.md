# Roteiro para Vídeo de Apresentação — OptiFlow Projeto Integrador

**Projeto:** OptiFlow — Plataforma de Otimização Logística  
**Disciplinas:** Projeto Integrador em Gestão de Sistemas Computacionais  
**Duração estimada:** 8–10 minutos  
**Apresentador:** Daniel Tomazi de Oliveira  
**Ferramenta sugerida:** OBS Studio + PowerPoint / Google Slides

---

## Estrutura Geral do Vídeo

| Segmento               | Duração       | Recurso visual sugerido          |
|------------------------|---------------|----------------------------------|
| Abertura e apresentação| 0:00 – 1:00   | Slide de capa + webcam           |
| Empresa e contexto     | 1:00 – 2:00   | Slides + diagrama da empresa     |
| Gestão de Projetos     | 2:00 – 3:30   | Slides + capturas do GitHub      |
| Análise de Dados       | 3:30 – 5:30   | Capturas de tela + gráficos      |
| Segurança da Informação| 5:30 – 7:00   | Slides + captura de código       |
| Pesquisa Operacional   | 7:00 – 8:30   | Terminal Python + gráficos       |
| Conclusão e resultados | 8:30 – 9:30   | Slide de resultados              |
| Encerramento           | 9:30 – 10:00  | Slide final + webcam             |

---

## Roteiro Completo

---

### SEGMENTO 1 — Abertura (0:00 – 1:00)

**[CORTE: Slide de capa com nome do projeto e logo OptiFlow]**

> "Olá! Meu nome é Daniel Tomazi de Oliveira e este é o vídeo de apresentação do meu Projeto Integrador em Gestão de Sistemas Computacionais."

> "O projeto se chama **OptiFlow Logística Inteligente** — uma plataforma de otimização logística para e-commerces de pequeno e médio porte."

> "Ao longo destes 10 minutos, vou mostrar como integrei quatro disciplinas do meu curso: Gestão de Projetos, Análise de Dados, Segurança da Informação e Pesquisa Operacional, todas aplicadas a um contexto real de negócio."

**[CORTE: Slide com os 4 eixos do projeto]**

---

### SEGMENTO 2 — A Empresa e o Problema (1:00 – 2:00)

**[CORTE: Slide com descrição da OptiFlow]**

> "A OptiFlow é uma empresa do setor de logtech — tecnologia aplicada à logística. Seu modelo de negócio é SaaS B2B: vende software de gestão logística para e-commerces que precisam otimizar suas entregas de última milha."

> "O problema de negócio central tem três frentes:"
> - "Custos de entrega acima da média: R$ 32,50 por pedido contra R$ 24,00 da concorrência de grande porte"
> - "Alta taxa de atrasos: 23% das entregas fora do prazo"
> - "Ausência de dados estruturados para tomada de decisão"

**[CORTE: Slide com tabela de problemas e impactos]**

> "O projeto integrador ataca esses três problemas de forma coordenada entre as disciplinas."

---

### SEGMENTO 3 — Gestão de Projetos (2:00 – 3:30)

**[CORTE: Slide com título "Disciplina 1: Gestão de Projetos"]**

> "Na disciplina de Gestão de Projetos, utilizei uma abordagem híbrida combinando PMBOK e Scrum."

**[CORTE: Captura de tela do arquivo `eap_wbs.md` no GitHub]**

> "Desenvolvi a Estrutura Analítica do Projeto com 24 pacotes de trabalho distribuídos em 5 entregas principais."

**[CORTE: Captura de tela do `cronograma_gantt.md`]**

> "O cronograma prevê 16 semanas de execução, com seis fases e marcos mensuráveis. A carga total estimada é de 112 horas."

**[CORTE: Slide com resumo do plano de riscos]**

> "Identifiquei 12 riscos, classificados por probabilidade e impacto. O risco mais crítico foi a disponibilidade de dados reais, mitigado pela geração de dados sintéticos representativos."

**[CORTE: Slide do Backlog]**

> "O backlog ágil contém 29 User Stories organizadas em 10 sprints, totalizando 123 story points, garantindo rastreabilidade total entre requisitos e entregas."

---

### SEGMENTO 4 — Análise de Dados (3:30 – 5:30)

**[CORTE: Slide com título "Disciplina 2: Análise de Dados"]**

> "Para Análise de Dados, segui a metodologia CRISP-DM e trabalhei com um dataset de 200 pedidos logísticos simulados."

**[CORTE: Captura de tela do arquivo `dataset_logistica.csv`]**

> "O dataset contém 8 variáveis: ID do pedido, região, distância, tempo de entrega, custo, motorista, valor e data."

**[CORTE: Executar `calcular_kpis.py` ao vivo no terminal]**
```
python 02_analise_de_dados/kpis/calcular_kpis.py
```

> "Os KPIs calculados mostram faturamento mensal, tempo médio de entrega e custo médio por pedido."

**[CORTE: Mostrar o gráfico `grafico_receita.png`]**

> "Este painel mostra a evolução do faturamento, distribuição por região, comparação faturamento versus custo e o ticket médio."

**[CORTE: Mostrar `grafico_performance_entregas.png`]**

> "Já este painel foca na performance de entregas: tempo médio por região, taxa de pontualidade e volume ao longo do tempo. O insight mais relevante: a região Norte tem custo 18% acima da média e eficiência 12% abaixo."

---

### SEGMENTO 5 — Segurança da Informação (5:30 – 7:00)

**[CORTE: Slide com título "Disciplina 3: Segurança da Informação"]**

> "Na Segurança da Informação, utilizei STRIDE para mapeamento de ameaças, Matriz GUT para priorização de vulnerabilidades, e as diretrizes da LGPD para conformidade legal."

**[CORTE: Captura de tela do `mapeamento_ameacas.md`]**

> "O mapeamento STRIDE identificou 22 ameaças em 6 categorias. As mais críticas: injeção de SQL, exposição de credenciais e ataques DDoS."

**[CORTE: Captura da Matriz GUT]**

> "A Matriz GUT priorizou as vulnerabilidades por Gravidade, Urgência e Tendência. As 3 com score máximo de 125 foram: SQL Injection, credenciais hardcoded e dados pessoais em texto plano."

**[CORTE: Slide do diagrama de autenticação]**

> "A arquitetura de autenticação usa 4 camadas: hash bcrypt, JWT com expiração de 15 minutos, 2FA por TOTP e controle de acesso por papel, o RBAC."

**[CORTE: Slide sobre LGPD]**

> "Na adequação à LGPD, mapeei todos os dados pessoais, defini bases legais de tratamento e documentei os 9 direitos dos titulares com mecanismos reais de exercício."

---

### SEGMENTO 6 — Pesquisa Operacional (7:00 – 8:30)

**[CORTE: Slide com título "Disciplina 4: Pesquisa Operacional"]**

> "Na Pesquisa Operacional, formulei e resolvi dois problemas de Programação Linear Inteira com a biblioteca PuLP do Python."

**[CORTE: Slide com a fórmula do Problema 1]**

> "O Problema 1 é a Otimização de Rotas de Entrega. O objetivo é minimizar o custo total, respeitando restrições de peso, distância e número de paradas por rota."

**[CORTE: Executar `otimizacao.py` do Problema 1 ao vivo]**
```
python 04_pesquisa_operacional/problema_1_otimizacao_entregas/otimizacao.py
```

> "O solver encontra a solução ótima em milissegundos, indicando qual pedido vai para qual rota e o custo total mínimo."

**[CORTE: Gráfico de análise de cenários]**

> "A análise de 5 cenários mostra como diferentes restrições operacionais afetam o custo final. A redução para 2 rotas disponíveis é o cenário mais crítico."

**[CORTE: Slide com a fórmula do Problema 2]**

> "O Problema 2 é a Alocação de Motoristas por Região. O objetivo agora é maximizar a eficiência operacional, garantindo que a demanda mínima de cada região seja atendida."

**[CORTE: Executar `otimizacao.py` do Problema 2 ao vivo]**
```
python 04_pesquisa_operacional/problema_2_alocacao_motoristas/otimizacao.py
```

> "O modelo aloca cada motorista à região onde ele tem maior eficiência histórica, respeitando disponibilidade de horas e nível de experiência exigido por cada região."

---

### SEGMENTO 7 — Resultados e Conclusão (8:30 – 9:30)

**[CORTE: Slide de resumo de resultados]**

> "Consolidando: o projeto entregou..."

| Disciplina            | Entregas                                       |
|-----------------------|------------------------------------------------|
| Gestão de Projetos    | 8 artefatos PMBOK/Scrum; 29 User Stories       |
| Análise de Dados      | 200 registros; 4 KPIs; 6 gráficos em Python   |
| Segurança             | 22 ameaças mapeadas; conformidade com LGPD     |
| Pesquisa Operacional  | 2 modelos PLI; 10 cenários analisados          |

**[CORTE: Slide com diagrama de integração entre disciplinas]**

> "O diferencial está na integração real: os dados da análise alimentam os parâmetros de eficiência dos modelos de otimização; os riscos de segurança foram incorporados ao backlog ágil; e a Matriz GUT foi inserida no Plano de Riscos do projeto."

**[CORTE: Slide de KPI final]**

> "Com a plataforma, a simulação aponta potencial de redução de 26% no custo médio de entrega — de R$ 32,50 para R$ 24,00 — e elevação da taxa de entregas no prazo de 77% para 93%."

---

### SEGMENTO 8 — Encerramento (9:30 – 10:00)

**[CORTE: Slide final com link do repositório GitHub]**

> "Todo o código, documentação e relatórios estão disponíveis no GitHub. O link está na descrição."

> "Foi um projeto desafiador que me fez enxergar como as quatro disciplinas se conectam na prática. Uma plataforma como a OptiFlow só é viável quando gestão, dados, segurança e otimização trabalham juntos desde o início."

> "Obrigado pela atenção!"

**[CORTE: Fade out]**

---

## Checklist de Produção

| Item                                                   | Status |
|--------------------------------------------------------|--------|
| ☐ Preparar slides com template do projeto              | —      |
| ☐ Testar execução de todos os scripts antes de gravar  | —      |
| ☐ Configurar iluminação adequada (webcam)              | —      |
| ☐ Usar microfone externo para áudio limpo              | —      |
| ☐ Gravar em resolução mínima 1080p (1920×1080)         | —      |
| ☐ OBS: janela de slides + câmera (Picture-in-Picture)  | —      |
| ☐ Editar: cortar pausas longas, adicionar zoom         | —      |
| ☐ Exportar em MP4 (H.264), máximo 500 MB               | —      |
| ☐ Fazer upload no YouTube/Drive e gerar link           | —      |

---

## Dicas de Apresentação

1. **Mostre o código rodando ao vivo** — mais convincente do que slides estáticos
2. **Conecte os eixos** — enfatize como as disciplinas se integram umas às outras
3. **Seja objetivo** — 10 minutos passa rápido; vá direto ao ponto em cada segmento
4. **Mantenha contato visual** com a câmera ao falar, não com a tela
5. **Tenha um backup gravado** do terminal, caso algo falhe durante a gravação ao vivo

---

*Roteiro desenvolvido para o Projeto Integrador em Gestão de Sistemas Computacionais — OptiFlow Logística Inteligente.*
