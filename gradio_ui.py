### gradio ui configuration 
import os 
import gradio as gr
from main import process_meeting 

with gr.Blocks() as demo:

    gr.Markdown("# 🎙️ Meeting Assistant")

    gr.Markdown(
        "Upload a meeting recording and generate a transcript and structured meeting minutes."
    )

    audio_input = gr.Audio(
        sources=["upload"],
        type="filepath",
        label="Meeting Audio"
    )

    process_button = gr.Button("Process Meeting")

    with gr.Row():

        transcript_output = gr.Textbox(
            label="Transcript",
            lines=20
        )

        summary_output = gr.Markdown(
            label="Meeting Summary"
        )

    download_file = gr.File(
        label="Download Meeting Minutes"
    )

    process_button.click(
        fn=process_meeting,
        inputs=audio_input,
        outputs=[
            transcript_output,
            summary_output,
            download_file
        ]
    )

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)