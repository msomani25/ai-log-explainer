# 🔍 AI Log Analyzer

> **A hybrid AI incident triage tool that combines fast local log pattern detection with AI-powered root cause explanations.**

AI Log Analyzer helps engineers quickly diagnose application failures during production incidents — without wading through mountains of unstructured logs.

---

## 🚀 Problem

In distributed systems, engineers often spend significant time analyzing logs during incidents.

**Common challenges include:**

- Large volumes of unstructured logs
- Unknown or unfamiliar error patterns
- Slow manual debugging cycles
- Delayed incident resolution

Traditional rule-based systems help detect known failures but struggle with new or complex issues.

---

## ✅ Solution

AI Log Analyzer uses a **hybrid architecture** that combines rule-based speed with LLM intelligence:

1. Detect known failures locally using rule-based parsing
2. Invoke an LLM only for unfamiliar errors
3. Generate human-readable root cause explanations
4. Suggest potential fixes

**Benefits:**

| Benefit | Description |
|---|---|
| ⚡ Fast triage | Instant results for common, known issues |
| 🤖 Smart reasoning | LLM analysis for unknown or complex failures |
| 💰 Cost efficiency | AI is only invoked when necessary |

---

## 🧠 Architecture

```text
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
```

---

## 🛠️ Tech Stack

**Language:** Python

**Parsing:** Regex / rule-based engine

**AI Model:** Claude (Anthropic API)

**Interface:** CLI

---

## 📂 Project Structure

```text
ai-log-explainer/
  ├── main.py
  ├── error_rules.py
  ├── requirements.txt
  ├── README.md
  └── logs/
      ├── java_error.log
      ├── python_error.log
      └── docker_error.log
```
---

## ▶️ Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/msomani25/ai-log-explainer.git
cd ai-log-explainer
```

**2. Set up a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the tool**

```bash
python main.py
```
---

## 🔑 Optional AI Setup

To enable LLM-powered analysis for unknown errors, add your Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Without an API key, the tool will still work for known error patterns using the local rule engine.

---

## 🎯 Use Cases

🔥 Production incident triage

🐛 Developer debugging workflows

🎧 Support engineering investigations

📡 AI-assisted observability tooling

---

## 📈 Future Improvements

Real-time log ingestion

Kubernetes log integration

Web dashboard UI

Slack / alerting integrations

Vector search for semantic log similarity
