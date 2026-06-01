# 🚀 Universal LLM Benchmark Suite

A comprehensive benchmarking framework for evaluating Large Language Models (LLMs) across real-world tasks including Mathematics, Reasoning, Coding, Consistency, Hallucination Detection, and Latency Measurement.

The project compares multiple models from different providers such as Groq, OpenRouter, and Ollama, generates benchmark scores, exports results to CSV, and visualizes model performance using an interactive Gradio dashboard.

---

## 📌 Features

* 🧮 Math Benchmark
* 🧠 Logical Reasoning Benchmark
* 💻 Coding Benchmark
* 🔄 Consistency Evaluation
* 🚫 Hallucination Detection
* ⚡ Latency Measurement
* 📊 Overall Performance Scoring
* 📁 CSV Result Export
* 🎨 Interactive Gradio Dashboard
* 🌐 Multi-Provider Model Support

---

## 🏗️ Project Architecture

```text
Datasets
   ↓
Benchmark Engine
   ↓
Model Evaluation
   ↓
CSV Generation
   ↓
Gradio Dashboard
```

---

## 🤖 Supported Models

### Groq

* llama-3.3-70b-versatile

### OpenRouter

* qwen/qwen3-coder-30b-a3b-instruct

### Ollama

* gemma3:270m

---

## 📊 Evaluation Metrics

| Metric              | Description                                    |
| ------------------- | ---------------------------------------------- |
| Math                | Mathematical problem solving accuracy          |
| Reasoning           | Logical reasoning performance                  |
| Code                | Coding task accuracy                           |
| Consistency         | Stability of responses across repeated prompts |
| Hallucination Rate  | Frequency of incorrect fabricated information  |
| Hallucination Score | Inverse hallucination metric                   |
| Latency             | Average response time                          |
| Overall Score       | Combined benchmark score                       |

---

## ⚙️ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## 🦙 Ollama Setup

Install Ollama and download the required models:

```bash
ollama pull gemma3:270m
```

Verify installation:

```bash
ollama list
```

---

## ▶️ Running the Benchmark

Execute:

```bash
python benchmark_project.py
```

The benchmark will:

* Load datasets
* Evaluate all configured models
* Calculate benchmark metrics
* Generate leaderboard rankings
* Export results to `universal.csv`

---

## 📈 Launching the Dashboard

Start the Gradio interface:

```bash
python gradio.py
```

Open:

```text
http://127.0.0.1:7860
```

The dashboard provides:

* Leaderboard View
* Model Selection
* Individual Metric Analysis
* Performance Charts

---
# 📸 Application Screenshot

![App Screenshot](https://github.com/SujithVarma-ai/Universal-Benchmark-Suite-Backed-by-Metrics/blob/main/Screenshot%202026-05-31%20161638.png)

## 🤖 Supported Providers & Models

The benchmark framework is designed to evaluate models from multiple providers and can be easily extended to support additional LLMs.

### Supported Providers

* Google Gemini
* OpenAI
* Anthropic Claude
* Groq
* OpenRouter
* Ollama

### Example Models

| Provider      | Models                                       |
| ------------- | -------------------------------------------- |
| Google Gemini | gemini-2.5-flash, gemini-2.5-pro             |
| OpenAI        | GPT-4o, GPT-4.1, GPT-5                       |
| Anthropic     | Claude Sonnet, Claude Opus                   |
| Groq          | llama-3.3-70b-versatile                      |
| OpenRouter    | qwen3-coder, DeepSeek models, GPT-OSS models |
| Ollama        | llama3.2, deepseek-r1, gemma3, mistral, qwen |

The framework allows benchmarking any compatible LLM by simply adding the model name and API client configuration.

A provider-agnostic benchmarking framework for evaluating Large Language Models (LLMs) across Mathematics, Reasoning, Coding, Consistency, Hallucination Detection, and Latency. The system supports models from Gemini, OpenAI, Claude, Groq, OpenRouter, Ollama, and other compatible providers.

## 🎯 Future Improvements

* More benchmark datasets
* Advanced hallucination detection
* Additional model providers
* Radar chart visualizations
* Benchmark history tracking
* Automated report generation
* Cost analysis per model

---

## 📜 License

MIT License.

---

Developed as a Universal LLM Evaluation Framework for benchmarking and comparing modern Large Language Models across multiple real-world tasks.
