# AI Log Analyzer (Hybrid AI Incident Triage Tool)

AI Log Analyzer is a lightweight observability utility that helps engineers quickly diagnose application failures by combining **fast local log pattern detection** with **AI-powered root cause explanations**.

This project demonstrates how AI can augment incident triage workflows in modern cloud environments.

---

## 🚀 Problem

In distributed systems, engineers often spend significant time analyzing logs during production incidents.

Common challenges include:

- Large volumes of unstructured logs  
- Unknown or unfamiliar error patterns  
- Slow manual debugging cycles  
- Delayed incident resolution  

Traditional rule-based systems help detect known failures but struggle with new or complex issues.

---

## ✅ Solution

AI Log Analyzer uses a **hybrid architecture**:

1. Detect known failures locally using rule-based parsing  
2. Invoke an LLM only for unfamiliar errors  
3. Generate human-readable root cause explanations  
4. Suggest potential fixes  

This enables:

- ⚡ Fast triage for common issues  
- 🤖 Intelligent reasoning for unknown failures  
- 💰 Reduced AI cost through selective invocation  

---

## 🧠 Architecture

Log Input
   │
   ▼
Local Rule Engine (`error_rules.py`)
   ├── Known Error → Structured Explanation
   └── Unknown Error
        │
        ▼
     LLM API (Claude)
        │
        ▼
Root Cause + Suggested Fix

---

## 🛠 Tech Stack

- Python  
- Regex / rule-based parsing  
- Claude LLM API  
- CLI interface  

---

## 📂 Project Structure

ai-log-explainer/
├── main.py
├── error_rules.py
├── requirements.txt
├── README.md
└── logs/
    ├── java_error.log
    ├── python_error.log
    └── docker_error.log

---

## ▶️ Run Locally

```bash
git clone https://github.com/msomani25/ai-log-explainer.git
cd ai-log-explainer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

---

## 🔑 **Optional AI Setup**

```bash
export ANTHROPIC_API_KEY="your_api_key_here"

---

## 🎯 Use Cases

- Production incident triage
- Developer debugging workflows
- Support engineering investigations
- AI-assisted observability tooling

---

## 📈 Future Improvements

- Real-time log ingestion
- Kubernetes log integration
- Web dashboard UI
- Slack / alert integrations
- Vector search for semantic log similarity
