# AI Log Analyzer (Hybrid Local + LLM Error Diagnosis)

An intelligent log analysis system that combines fast local error detection with LLM-powered root cause analysis to help developers quickly understand and resolve failures.

## 🚀 Overview

Modern applications generate large volumes of logs, making debugging time-consuming and inefficient.
This project introduces a hybrid approach to that:

* Detects known error patterns using local rule-based parsing
* Uses an LLM to explain unknown or complex errors
* Provides structured, human-readable diagnostics
* Enables faster debugging workflows for developers and support engineers

## 🧠 Architecture

Hybrid pipeline:

1. Log ingestion
2. Local pattern detection (regex-based)
3. Error classification
4. LLM-based explanation generation
5. Structured output

This approach ensures:

* ⚡ Low latency for known errors
* 🤖 Intelligent reasoning for new failures
* 💰 Reduced LLM cost via selective invocation

## 🛠 Tech Stack

* Python
* Regex pattern engine
* OpenAI / Claude API (LLM reasoning)
* CLI interface

## 📂 Project Structure

```
logs/               # Sample log files  
patterns/           # Known error patterns  
analyzer.py         # Main execution pipeline  
llm_explainer.py    # LLM integration  
utils.py            # Helper utilities  
```

## ▶️ How to Run

```bash
git clone <repo>
cd ai-log-analyzer
pip install -r requirements.txt
python analyzer.py logs/sample.log
```

## 📈 Future Improvements

* Add vector database for semantic log search
* Web UI dashboard
* Real-time log streaming support
* Kubernetes log ingestion
* Observability tool integrations

## 🎯 Use Cases

* Developer debugging
* Production incident triage
* Support engineering workflows
* AI-assisted observability tooling

## 🤝 Contributions

Open to suggestions and improvements.
