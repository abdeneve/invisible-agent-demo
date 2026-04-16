# 🕵️‍♂️ Invisible Agent B2A (Backend-to-Agent)

![Invisible Agent Hero](file:///C:/Users/Legion/.gemini/antigravity/brain/b4c5d782-04b1-4077-8ffa-ffb194733224/invisible_agent_hero_1776288059961.png)

> **"Automação resiliente, decisões determinísticas e segurança zero-trust para processos de backend complexos."**

---

## 🌟 Visão Geral

O **Invisible Agent B2A** é uma demonstração técnica de ponta que ilustra como arquitetar agentes de IA autônomos e "invisíveis" (sem interface humana) para operar em fluxos críticos de backend empresarial. 

Focado em **conciliação bancária**, o sistema garante que processos complexos sejam executados de forma durável, segura e à prova de falhas, mesmo em cenários de instabilidade de infraestrutura.

---

## 🛠️ Destaques Tecnológicos

Este projeto utiliza o que há de mais moderno na engenharia de software e inteligência artificial:

- **[Temporal.io](https://temporal.io/)**: Orquestração de workflows duráveis que sobrevivem a reinicializações de servidores e falhas de rede.
- **[LangGraph](https://python.langchain.com/docs/langgraph/)**: Grafos de estado estruturados para tomadas de decisão de IA determinísticas e repetíveis.
- **[MCP (Model Context Protocol)](https://modelcontextprotocol.io/)**: Interface segura para chamadas de ferramentas (tool calls) externas, mitigando riscos de injeção de prompt.
- **Zero Trust Security**: Autenticação baseada em tokens efêmeros de curta duração para validação de pagamentos.

---

## 📂 Estrutura do Projeto

```bash
├── 🤖 agents/   # Cérebro do agente (LangGraph + LangChain)
├── 🔐 auth/     # Segurança e validação Zero Trust
├── 🏗️ config/   # Configurações dinâmicas e variáveis de ambiente
├── ⚡ core/     # Workflows e Actividades (Temporal Engine)
├── 📚 docs/     # PRD e documentação detalhada
├── 🔌 mcp/      # Conectores seguros (Tool calling)
├── 📜 main.py   # Ponto de entrada da Demo
└── 📋 requirements.txt
```

---

## 🚀 Como Iniciar

### 1. Pré-requisitos
- Python **3.10 ou superior**
- Docker (opcional, para rodar o Temporal Server localmente)
- Uma chave de API da **OpenAI** (configurada no `.env`)

### 2. Instalação
```powershell
# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração
Renomeie o arquivo `.env.exemplo` para `.env` e preencha suas chaves:
```env
OPENAI_API_KEY=sua_chave_aqui
TEMPORAL_ADDRESS=localhost:7233
```

### 4. Executando a Demo
```powershell
# Inicie o worker do Temporal
python main.py
```

---

## 🔄 Fluxo da Demo: Conciliação de Faturas

1. **Trigger Resiliente**: O sistema recebe um `invoice_id` via sinal ERP.
2. **Ingestão com Retry**: Se o ERP estiver offline, o Temporal tenta automaticamente em intervalos exponenciais.
3. **Raciocínio Estruturado**: O agente analisa os dados usando o `StateGraph`, decidindo entre aprovação, fraude ou revisão manual.
4. **Pagamento Seguro**: A invocação final é protegida por um token efêmero gerado dinamicamente para aquela transação específica.

---

## 🗺️ Roadmap de Desenvolvimento

- [ ] **Fase 1**: Infraestrutura e Modelos (Em andamento)
- [ ] **Fase 2**: Grafo e Lógica do Agente
- [ ] **Fase 3**: Implementação dos Workflows Temporal
- [ ] **Fase 4**: Testes de Stress e Validação Zero-Trust

---

### 🛡️ Sobre o Projeto
Desenvolvido como parte do programa **A SALA DE IA**, focado em ensinar profissionais a construir ecossistemas de IA empresariais de alto valor.

---
<sub>© 2026 Invisible Agent B2A Demo. Todos os direitos reservados.</sub>
