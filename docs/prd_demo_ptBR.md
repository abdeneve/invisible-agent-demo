# Product Requirements Document (PRD): Demo do Agente Invisível B2A

## 1. Visão Geral
O projeto "Invisible Agent B2A" é uma demonstração técnica de uma arquitetura de agentes autônomos invisíveis (sem interface de usuário tradicional) projetados para operar em processos de backend empresariais (B2B/B2A) de forma resiliente e segura. O sistema automatiza fluxos complexos, como conciliação bancária e validação de pagamentos, garantindo tolerância a falhas de infraestrutura, raciocínio determinístico com IA e segurança baseada em zero-trust.

## 2. Objetivos da Demo
- Demonstrar a orquestração de fluxos de trabalho duráveis e à prova de falhas utilizando o **Temporal**.
- Mostrar a tomada de decisão estruturada de um agente de inteligência artificial através do **LangGraph** e esquemas **Pydantic**.
- Implementar e ilustrar conectividade segura via **MCP** (Model Context Protocol) para invocar ferramentas sem abrir vulnerabilidades de injeção de prompts.
- Implementar um mecanismo de validação e ingestão **Zero Trust** baseado em tokens efêmeros.

## 3. Componentes do Sistema

| Módulo | Responsabilidade | Tecnologias Chave |
|--------|-----------------|-------------------|
| **Core** (`/core`) | Define o fluxo da regra de negócio e garante persistência em caso de queda do servidor. | `temporalio` (Workflows, Activities) |
| **Agents** (`/agents`) | Contém a lógica do cérebro do agente. Decide aprovar ou rejeitar faturas usando esquemas JSON rígidos. | `langchain`, `langgraph` |
| **Auth** (`/auth`) | Valida a origem do webhook B2B e emite tokens de autenticação de curta duração limitados à tarefa. | `pydantic` |
| **MCP** (`/mcp`) | Porta de entrada para interação segura (tool calls) com ambientes/serviços externos à IA. | `mcp` |

## 4. Descrição do Fluxo Principal
**Processo: Conciliação Estruturada de Faturas**
1. **Trigger Inicial:** O arquivo `main.py` dispara o worker e inicia um sinal com um `invoice_id` fictício, simulando um ERP recebido.
2. **Obtenção Resiliente:** O workflow ativa a atividade `fetch_erp_data`. Se a conexão falhar, o Temporal automatiza a tentativa da atividade em intervalos (Retry Loop) sem bloquear o processo principal.
3. **Decisão Agêntica:** Os dados obtidos são injetados em `execute_agentic_reasoning`, ativando o grafo do LangGraph pré-estruturado.
4. **Finalização:** Com base na decisão determinística (Fraudulento ou Aprovado), o sistema executa a ação ou falha explicitamente, disparando a invocação final `authorize_secure_payment` protegida por tokens temporários.

## 5. Pré-requisitos Técnicos
- Python 3.10+
- Um servidor local de **Temporal** em execução (ex: `localhost:7233`).
- **Principais bibliotecas:**
  - `langchain==0.1.16` & `langgraph==0.0.38`
  - `temporalio==1.6.0`
  - `pydantic==2.6.4`
  - `pydantic-settings==2.2.1`
  - `mcp>=1.2.0`

## 6. Fases de Desenvolvimento Sugeridas
1. **Fase 1: Infraestrutura e Modelos**. Definir variáveis no arquivo `.env`, levantar um cluster leve do Temporal e completar as configurações (`settings.py`).
2. **Fase 2: Grafo e Lógica do Agente**. Preencher a lógica do `StateGraph` do LangGraph em `agents/reconciliation_agent.py`.
3. **Fase 3: Fluxos do Temporal**. Escrever a lógica resiliente do `ReconciliationWorkflow` e conectar a invocação do agente.
4. **Fase 4: Execução e Testes**. Executar repetidamente o framework completo, derrubando o processo Python no meio para validar a durabilidade do estado.
