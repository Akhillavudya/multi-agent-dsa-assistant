# Multi-Agent DSA Assistant

Multi-Agent DSA Assistant is an AI-powered coding interview assistant built using **LangGraph**, **Streamlit**, **Hugging Face**, and **LangSmith**. 

It solves Data Structures and Algorithms (DSA) problems step-by-step using multiple specialized agents instead of a single prompt execution. 

The goal is to accurately simulate the thought process of a strong technical candidate during a coding interview:
- What is the problem truly asking?
- Which DSA pattern fits optimally?
- What is the baseline brute-force approach?
- How can we optimize its space and time complexity?
- Is the generated code bug-free and efficient?
- How can the solution be communicated clearly?

---

## 🚀 Features

* **Multi-Agent Workflow:** Built with LangGraph to orchestrate stateful, multi-turn agent execution.
* **Planner Agent:** Accurately detects topics and core patterns.
* **Brute Force Agent:** Brainstorms the simplest baseline approach first.
* **Optimizer Agent:** Optimizes the brute force approach to reach ideal time complexity.
* **C++ Code Generator Agent:** Outputs clean, idiomatic C++ code based on the optimized strategy.
* **Reviewer Agent:** Critiques the code for logical bugs, syntax issues, and edge cases.
* **Smart Retry Loop:** Uses conditional routing to automatically rewrite code if bugs are flagged.
* **Explanation Agent:** Distills the logic into a highly readable, interview-friendly explanation.
* **Streamlit Chat Interface:** A clean, minimal UI for seamless user interaction.
* **LangSmith Tracing:** Deep visibility into prompt execution, state shifts, and agent performance.

---

## 🧠 Core Idea & Workflow

The assistant breaks down the monolithic task of problem-solving into a structured multi-agent reasoning pipeline:

```text
       [ User DSA Problem ]
                │
                ▼
         [ Planner Agent ]
                │
                ▼
      [ Brute Force Agent ]
                │
                ▼
        [ Optimizer Agent ]
                │
                ▼
     [ Code Generator Agent ] ◄─────────────────┐
                │                               │
                ▼                               │ (if bug found)
        [ Reviewer Agent ]                      │
                │                               │
                ├─► [ Flagged: Needs Fix ] ─────┘
                │
                └─► [ Approved ]
                        │
                        ▼
              [ Explanation Agent ]
                        │
                        ▼
         [ Final Solution + Code + Review ]
