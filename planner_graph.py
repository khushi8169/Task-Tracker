from llm_utils import generate_subtasks
from vector_store import add_to_vector_store, search_similar
from memory_store import memory
from task_utils import save_task

from langgraph.graph import StateGraph, END
from typing import TypedDict

class GraphState(TypedDict):
    input: str
    result: str


def input_handler(state):
    return {"input": state["input"]}  # Return a dict with the same schema as the GraphState

def classify_intent(state):
    input_text = state["input"]  # ✅ Extract the actual string from the dict
    if any(keyword in input_text.lower() for keyword in ["create", "new", "build"]):
        return "create"
    elif any(keyword in input_text.lower() for keyword in ["what", "show", "find", "search"]):
        return "query"
    else:
        return "unknown"


def create_task(state):
    title = "Sample Project"
    subtasks = generate_subtasks(title, state['input'])
    task = save_task(title, state['input'], subtasks)
    memory.save_context({"input": state['input']}, {"output": str(subtasks)})
    add_to_vector_store(state['input'])
    return {"result": f"✅ Created: {subtasks}"}

def query_task(state):
    results = search_similar(state['input'])
    return {"result": "📄 Similar Tasks:\n" + "\n".join([doc.page_content for doc in results])}

def default_response(state):
    return {"result": "🤔 Sorry, I didn’t understand that."}

# LangGraph Definition
planner = StateGraph(GraphState)
planner.add_node("input_handler", input_handler)
planner.add_node("create_task", create_task)
planner.add_node("query_task", query_task)
planner.add_node("default_response", default_response)
planner.set_entry_point("input_handler")

planner.add_conditional_edges(
    "input_handler",
    classify_intent,
    {
        "create": "create_task",
        "query": "query_task",
        "unknown": "default_response"
    }
)

planner.add_edge("create_task", END)
planner.add_edge("query_task", END)
planner.add_edge("default_response", END)
planner = planner.compile()
