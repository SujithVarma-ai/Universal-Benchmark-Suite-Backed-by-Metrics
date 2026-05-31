import gradio as gr
import pandas as pd
import plotly.express as px

CSV_FILE = "universal.csv"

def load_data():
    return pd.read_csv(CSV_FILE)

def get_model_details(model_name):
    df = load_data()
    row = df[df["Model"] == model_name].iloc[0]
    return (
        row["Math"],
        row["Reasoning"],
        row["Code"],
        row["Latency(sec)"],
        row["Latency Score"],
        row["Consistency"],
        row["Hallucination Rate"],
        row["Hallucination Score"],
        row["Overall"]
    )

def get_leaderboard():
    return load_data()

def get_chart():
    df = load_data()
    fig = px.bar(
        df,
        x="Model",
        y="Overall",
        title="Overall Benchmark Scores"
    )

    return fig

with gr.Blocks(title="Universal LLM Benchmark Suite") as demo:

    gr.Markdown(
        """
        # Universal LLM Benchmark Suite
        
        Compare LLM performance across:
        - Math
        - Reasoning
        - Coding
        - Consistency
        - Hallucination
        - Latency
        """
    )

    with gr.Tab("Leaderboard"):
        leaderboard = gr.Dataframe(
            value=get_leaderboard(),
            interactive=False
        )
        refresh_btn = gr.Button("Refresh CSV")
        refresh_btn.click(
            fn=get_leaderboard,
            outputs=leaderboard
        )

    with gr.Tab("Model Analysis"):
        models = load_data()["Model"].tolist()
        model_dropdown = gr.Dropdown(
            choices=models,
            value=models[0],
            label="Select Model"
        )

        with gr.Row():
            math_box = gr.Number(label="Math")
            reasoning_box = gr.Number(label="Reasoning")
            code_box = gr.Number(label="Code")

        with gr.Row():
            latency_sec_box = gr.Number(label="Latency(sec)")
            latency_score_box = gr.Number(label="Latency Score")

        with gr.Row():
            consistency_box = gr.Number(label="Consistency")
            hallucination_rate_box = gr.Number(label="Hallucination Rate")

        with gr.Row():
            hallucination_score_box = gr.Number(
                label="Hallucination Score"
            )
            overall_box = gr.Number(label="Overall")

        model_dropdown.change(
            fn=get_model_details,
            inputs=model_dropdown,
            outputs=[
                math_box,
                reasoning_box,
                code_box,
                latency_sec_box,
                latency_score_box,
                consistency_box,
                hallucination_rate_box,
                hallucination_score_box,
                overall_box
            ]
        )
    with gr.Tab("Charts"):
        chart = gr.Plot(
            value=get_chart()
        )
demo.launch()
