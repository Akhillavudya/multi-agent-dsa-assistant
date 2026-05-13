from typing import TypedDict

#things we need and what things we are building along with their type also
class GraphState(TypedDict):
    problem: str
    topic: str
    bruteforce: str
    optimized: str
    code: str
    review: str
    explanation: str
    needs_fix: bool
    retry_count: int