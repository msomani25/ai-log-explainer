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
text```

## 🛠️ Tech Stack

Language: Python
Parsing: Regex / rule-based engine
AI Model: Claude (Anthropic API)
Interface: CLI
