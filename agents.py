import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

from prompts import(
    PLANNER_PROMPT,
    BRUTEFORCE_PROMPT,
    OPTIMIZER_PROMPT,
    CODE_GENERATOR_PROMPT,
    REVIEWER_PROMPT,
    EXPLANATION_PROMPT,
)

client = InferenceClient(
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    # if not token:
    #     raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env file")
)

def llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
    )
    return response.choices[0].message.content

def planner_agent(state):
    prompt = PLANNER_PROMPT.format(
        problem = state["problem"]
    )
    result = llm(prompt)
    return { "topic": result}

def bruteforce_agent(state):
    prompt = BRUTEFORCE_PROMPT.format(
        problem=state["problem"]
    )
    result = llm(prompt)
    return {"bruteforce": result}


def optimizer_agent(state):
    prompt = OPTIMIZER_PROMPT.format(
        problem=state["problem"],
        bruteforce=state["bruteforce"]
    )
    result = llm(prompt)
    return {"optimized": result}

def code_generator_agent(state):
    prompt = CODE_GENERATOR_PROMPT.format(
        problem=state["problem"],
        optimized=state["optimized"]
    )
    result = llm(prompt)
    return {"code": result}

def reviewer_agent(state):
    prompt = REVIEWER_PROMPT.format(
        problem=state["problem"],
        code=state["code"]
    )
    result = llm(prompt)

    needs_fix = "needs_fix: true" in result.lower()

    return {
        "review": result,
        "needs_fix": needs_fix,
        "retry_count": state.get("retry_count", 0) + 1
    }


def explanation_agent(state):
    prompt = EXPLANATION_PROMPT.format(
        problem=state["problem"],
        code=state["code"]
    )
    result = llm(prompt)
    return {"explanation": result}