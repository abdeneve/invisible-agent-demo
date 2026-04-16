from typing import TypedDict, Annotated, Sequence, Any
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """Estado estruturado para o grafo de invocação do Agente."""
    messages: Annotated[Sequence[BaseMessage], operator.add]
    invoice_id: str
    is_fraudulent: bool

def build_reconciliation_graph() -> Any:
    """
    Constrói o StateGraph do LangGraph. O agente decidirá mediante
    schemas JSON estritos se aprova ou rejeita uma fatura.
    """
    # TODO: Implementar lógica de Construção do Grafo (LangGraph) 
    pass
