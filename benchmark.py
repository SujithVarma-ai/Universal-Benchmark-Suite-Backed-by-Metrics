import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

google_api_key = os.getenv('GOOGLE_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
    print("Groq API Key not set (and this is optional)")

if openrouter_api_key:
    print(f"OpenRouter API Key exists and begins {openrouter_api_key[:6]}")
else:
    print("OpenRouter API Key not set (and this is optional)")


openai = OpenAI()

gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
groq_url = "https://api.groq.com/openai/v1"
ollama_url = "http://localhost:11434/v1"
openrouter_url = "https://openrouter.ai/api/v1"

gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
ollama = OpenAI(api_key="ollama", base_url=ollama_url)
openrouter = OpenAI(api_key=openrouter_api_key, base_url=openrouter_url)

models = [
    "llama-3.3-70b-versatile",
    "qwen/qwen3-coder-30b-a3b-instruct",
    "gemma3:270m"
]

clients = {
    "llama-3.3-70b-versatile": groq,
    "qwen/qwen3-coder-30b-a3b-instruct": openrouter,
    "gemma3:270m": ollama
}

def ask_model(model_name, question):
    try:
        client = clients[model_name]
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"{model_name} failed: {e}")
        return ""

# Dataset
import json

def load_dataset(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


math_dataset = load_dataset("datasets_benchmark/math.json")
reasoning_dataset = load_dataset("datasets_benchmark/reasoning.json")
code_dataset = load_dataset("datasets_benchmark/code.json")
latency_dataset = load_dataset("datasets_benchmark/latency.json")
consistency_dataset = load_dataset("datasets_benchmark/consistency.json")
hallucination_dataset = load_dataset("datasets_benchmark/hallucination.json")


# Math Benchmark 
def evaluate_math(model_name, dataset):
    correct = 0
    for item in dataset:
        answer = ask_model(
            model_name,
            item["question"]
        )
        if item["answer"].lower() in answer.lower():
            correct += 1
    return correct / len(dataset) * 100


# Reasoning Benchmark
def evaluate_reasoning(model_name, dataset):
    correct = 0
    for item in dataset:
        answer = ask_model(
            model_name,
            item["question"]
        )
        if item["answer"].lower() in answer.lower():
            correct += 1
    return correct / len(dataset) * 100


# Code Benchmark
def evaluate_code(model_name, dataset):
    correct = 0
    for item in dataset:
        answer = ask_model(
            model_name,
            item["question"]
        )
        score = 0
        for keyword in item["keywords"]:
            if keyword.lower() in answer.lower():
                score += 1
        if score == len(item["keywords"]):
            correct += 1
    return correct / len(dataset) * 100


# Latency Benchmark
def evaluate_latency(model_name, dataset):
    total_time = 0
    for item in dataset:
        start_time = time.time()
        ask_model(
            model_name,
            item["question"]
        )
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / len(dataset)


# Consistency Benchmark
def evaluate_consistency(model_name, dataset):
    consistent = 0
    for item in dataset:
        answers = []
        for _ in range(2):
            answers.append(
                ask_model(
                    model_name,
                    item["question"]
                ).strip().lower()
            )
        if len(set(answers)) == 1:
            consistent += 1
    return consistent / len(dataset) * 100


# Hallucination Benchmark
def evaluate_hallucination(model_name, dataset):
    hallucinated = 0
    safe_phrases = [
        "don't know",
        "do not know",
        "unknown",
        "cannot determine",
        "not yet happened",
        "not yet occurred",
        "has not happened",
        "has not occurred",
        "hasn't happened",
        "hasn't occurred",
        "not occurred yet",
        "has not taken place",
        "future event",
        "cannot be known",
        "does not exist",
        "there is no",
        "no information available",
        "no king of mars",
        "mars is a planet",
        "mars has no",
        "uninhabited",
        "fictional"
]
    for item in dataset:
        answer = ask_model(
            model_name,
            item["question"]
        ).lower()
        safe_match = any(
            phrase in answer
            for phrase in safe_phrases
        )
        print("QUESTION:", item["question"])
        print("SAFE MATCH:", safe_match)
        if not safe_match:
            hallucinated += 1
    print("HALLUCINATED:", hallucinated)
    print("TOTAL:", len(dataset))
    return hallucinated / len(dataset) * 100           



# Run Benchmarks
results = []
for model in models:
    print(f"\nEvaluating {model}")

    math_score = evaluate_math(
        model,
        math_dataset
    )
    reasoning_score = evaluate_reasoning(
        model,
        reasoning_dataset
    )
    code_score = evaluate_code(
        model,
        code_dataset
    )
    latency_seconds = evaluate_latency(
    model,
    latency_dataset
    )
    latency_score = max(
    0,
    100 - (latency_seconds * 10)
    )
    consistency_score = evaluate_consistency(
        model,
        consistency_dataset
    )
    hallucination_rate = evaluate_hallucination(
    model,
    hallucination_dataset
    )
    hallucination_score = 100 - hallucination_rate

    overall_score = (
        math_score +
        reasoning_score +
        code_score +
        consistency_score +
        hallucination_score +
        latency_score
    ) / 6

    print("Math:", round(math_score, 2))
    print("Reasoning:", round(reasoning_score, 2))
    print("Code:", round(code_score, 2))
    print("Latency(sec):", round(latency_seconds, 3))
    print("Latency Score:", round(latency_score, 2))
    print("Consistency:", round(consistency_score, 2))
    print("Hallucination Score:", round(hallucination_score, 2))
    print("Hallucination Rate:", round(hallucination_rate, 2))
    print("Overall:", round(overall_score, 2))

    results.append({
        "Model": model,
        "Math": round(math_score, 2),
        "Reasoning": round(reasoning_score, 2),
        "Code": round(code_score, 2),
        "Latency(sec)": round(latency_seconds, 3),
        "Latency Score": round(latency_score, 2),
        "Consistency": round(consistency_score, 2),
        "Hallucination Rate": round(hallucination_rate, 2),
        "Hallucination Score": round(hallucination_score, 2),
        "Overall": round(overall_score, 2)
    })

import pandas as pd

df = pd.DataFrame(results)
df = df.sort_values(
    by="Overall",
    ascending=False
).reset_index(drop=True)

df.insert(
    0,
    "Rank",
    range(1, len(df) + 1)
)

df.to_csv(
    "universal.csv",
    index=False
)
print(df)

print("Benchmark completed.")
print("Results saved to universal.csv")
