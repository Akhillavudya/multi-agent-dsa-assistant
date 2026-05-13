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
```
📁 Project Structure
```text
 multi-agent-dsa-assistant/
│
├── app.py              # Streamlit frontend & web UI
├── graph.py            # LangGraph state machine configuration and workflow paths
├── agents.py           # Individual agent definitions and LLM configurations
├── prompts.py          # System instructions and engineered prompts for each agent
├── state.py            # Shared graph memory state definitions
├── requirements.txt    # Python dependencies
├── .gitignore          # Version control ignore rules
└── README.md           # Documentation
```

🖥️ Setup Instructions
1. Clone the Repositor
```text 
git clone <your-repo-url>
cd multi-agent-dsa-assistant
```
3. Configure a Virtual Environment
Bash
```text 
# Create the environment
python -m venv myenv

# Activate it (Windows)
myenv\Scripts\activate

# Activate it (Linux / Mac)
source myenv/bin/activate
```
3. Install Dependencies
 ```text 
Bash
pip install -r requirements.txt
```
5. Environment Variables Configuration
Create a .env file in the root directory and populate it with your environment keys:
```text 
Ini, TOML
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=multi-agent-dsa-assistant

```
5. Launch the Application
```text
Bash
streamlit run app.py
```
Open your browser and navigate to the default address: http://localhost:8501
