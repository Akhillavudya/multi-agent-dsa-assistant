#2a  importing all agents
from langgraph.graph import StateGraph, END
from state import GraphState

from agents import (
    planner_agent,
    bruteforce_agent,
    optimizer_agent,
    code_generator_agent,
    reviewer_agent,
    explanation_agent,
)

#2b building Graph using Graph state
builder = StateGraph(GraphState)

#2c  adding all nodes that are present
builder.add_node("planner", planner_agent)
builder.add_node("bruteforce", bruteforce_agent)
builder.add_node("optimizer", optimizer_agent)
builder.add_node("code_generator", code_generator_agent)
builder.add_node("reviewer", reviewer_agent)
builder.add_node("explanation", explanation_agent)

#2d set entry point and add edges
builder.set_entry_point("planner")

builder.add_edge("planner", "bruteforce")
builder.add_edge("bruteforce", "optimizer")
builder.add_edge("optimizer", "code_generator")
builder.add_edge("code_generator", "reviewer")

#2e handling conditional edge if code need_fix is true it will in loop

def route_after_review(state):
    if state["needs_fix"] and state["retry_count"] < 3:
        return "code_generator"
    return "explanation"

builder.add_conditional_edges(
    "reviewer",
    route_after_review,
    {
        "code_generator": "code_generator",
        "explanation": "explanation",
    }
)

#2f connecting final to END and complie graph
builder.add_edge("explanation", END)

graph = builder.compile()


