# Task Planner

**AI-powered project planner that breaks down any task into organized, prioritized subtasks using LangChain, Streamlit, and Mistral via Ollama.**  
Perfect for students, developers, and project managers to turn vague ideas into actionable roadmaps — instantly.

---

## Features

✅ **Natural Language Input** – Just type your goal like “Build a Resume Analyzer with frontend, backend, and Docker”.  
✅ **Auto Task Breakdown** – Generates a prioritized task list with time estimates using an LLM.  
✅ **Memory & Context** – Stores prior task breakdowns and understands them in context.  
✅ **Similar Task Retrieval** – Searches related tasks from a vector database using semantic similarity.  
✅ **Modular & Extensible** – Cleanly separated logic for planning, memory, and vector search.  
✅ **Beautiful UI** – Built with Streamlit for a smooth user experience.

---

## Tech Stack

| Layer            | Tech                                                                 |
|------------------|----------------------------------------------------------------------|
| **Frontend**     | `Streamlit`                                                          |
| **Backend**      | `LangChain`, `LangGraph`, `Langchain-Ollama`, `Vector DB (FAISS)`    |
| **LLM**          | `Mistral` via `Ollama` (locally running model)                        |
| **Embeddings**   | `HuggingFace Embeddings (all-MiniLM-L6-v2)`                          |
| **Memory**       | `ConversationSummaryBufferMemory`                                    |
| **Task Engine**  | `LangGraph` nodes with conditional routing (`StateGraph`)            |
| **Persistence**  | FAISS saved locally at `faiss_index/`                                |

---

## 🛠️ Project Structure

```

📁 Task\_Tracker/
├── app.py                  ← LangChain console-based interface (optional)
├── streamlit.py            ← Streamlit frontend UI
├── planner\_graph.py        ← LangGraph pipeline & intent classification
├── llm\_utils.py            ← Uses Mistral to generate subtasks
├── memory\_store.py         ← Manages memory with ConversationSummaryBuffer
├── vector\_store.py         ← FAISS vector store setup & query
├── screenshots/            ← UI screenshot (add your png here)
└── faiss\_index/            ← Stores FAISS index on disk

````
---
## Prerequisites
### 🔧 **System Requirements**

* **Python** `3.10+` (avoid 3.12+ for compatibility issues with some libs like FAISS)
* **Git**
* **Ollama** installed and running

  * Install from: [https://ollama.com](https://ollama.com)
  * Run:

    ```bash
    ollama pull mistral
    ollama run mistral
    ```

---

### 📦 **Python Libraries (via pip)**

Make sure the following are installed:

```bash
pip install \
  streamlit \
  langchain \
  langgraph \
  langchain-ollama \
  langchain-community \
  langchain-core \
  langchain-huggingface \
  huggingface-hub \
  faiss-cpu \
  scikit-learn \
  numpy \
  pandas \
  torch \
  transformers \
  sentence-transformers \
  pydantic \
  tf-keras \
  tensorflow
```

These cover:

| Dependency               | Purpose                                                  |
| ------------------------ | -------------------------------------------------------- |
| `streamlit`              | Frontend UI                                              |
| `langchain`, `langgraph` | Task orchestration and memory                            |
| `langchain-ollama`       | LLM wrapper for Mistral via Ollama                       |
| `langchain-huggingface`  | Embeddings (`all-MiniLM-L6-v2`)                          |
| `faiss-cpu`              | Local vector database                                    |
| `huggingface-hub`        | Model/tokenizer downloads                                |
| `torch`, `transformers`  | Underlying model backend (used in embeddings, LLMs)      |
| `sentence-transformers`  | Semantic similarity (used internally by some embeddings) |
| `tensorflow`, `tf-keras` | Required by some memory models and legacy dependencies   |
| `pydantic`               | TypedDict validation for `GraphState`, etc.              |

---

### Optional (but Recommended)

* Enable **Windows Developer Mode** (for symlinks with HuggingFace cache)
* Run Streamlit in polling mode (you're already doing this):

  ```python
  os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"
  ```

---

### Run the App

```bash
streamlit run streamlit.py
```
---

## 💬 Sample Prompts

Try entering one of these:

* **“Build a resume analyzer with frontend, backend, and Docker”**
* **“Create a chatbot with LangChain and Streamlit”**
* **“What are my past tasks related to Django?”**

---

## 🧪 Example Output

```
✅ Created:
Title: Sample Project - Cross-Platform Fitness Tracking App Development

Subtasks (Estimated Days):

1. Research and Planning (3 days)
   - Understand the requirements and objectives of the project.
   - Study existing fitness tracking apps for inspiration and best practices.
   - Identify key features, user flows, and design elements.
   - Create a detailed project plan and timeline.

2. Design and Prototyping (5 days)
   - Sketch initial app layouts and wireframes.
   - Develop clickable prototypes to demonstrate the functionality of the app.
   - Collaborate with design team for visual consistency across platforms.

3. Development Setup (2 days)
   - Set up development environments for Flutter, Google Fit, and Apple HealthKit.
   - Configure project structure and dependencies.
   - Ensure compatibility across targeted platforms (iOS, Android).

4. Cross-Platform Integration with Google Fit & Apple HealthKit (10 days)
   - Implement integration of Google Fit and Apple HealthKit to access user activity data.
   - Write platform-specific code for both iOS and Android.
   - Develop strategies to handle differences between the two platforms.
...
```

---

## 🔄 Memory & Vector Search

* **LangChain Memory** stores previous task input-output.
* **FAISS VectorStore** indexes all tasks and allows similarity search on new input.

---

## ❤ Why This Project Is Useful

* **AI-Powered Productivity** — Translates natural ideas into planned execution.
* **Great for Students** — Use it for project planning, hackathons, or capstone ideas.
* **Fully Modular** — Swap models, vector store, UI, or backend independently.
* **Deployable Anywhere** — Run locally with Ollama or host on cloud (Streamlit Community Cloud, Render, etc.).

---

## 📌 Future Improvements

* [ ] Export tasks as `.csv` or `.md`
* [ ] Support multiple LLMs (OpenAI, Claude)
* [ ] Add real-time collaboration

---
